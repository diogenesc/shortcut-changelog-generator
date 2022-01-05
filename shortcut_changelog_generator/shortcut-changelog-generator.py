import os
import re
import datetime
import requests
from git import Repo
from datetime import datetime

changelogPath = os.environ.get('CHANGELOG_PATH', 'CHANGELOG.md')
shortcutToken = os.environ.get('SHORTCUT_TOKEN')
ignoreLastTag = os.environ.get('IGNORE_LAST_TAG', False)

changelogHeaderLine = '# CHANGELOG\n'
releaseHeaderLine = '## Releases\n'
shortcutApiUrl = 'https://api.app.shortcut.com/api/v3/stories/'

def getStoriesIdsAndLatestTag():
    repo = Repo('./')
    tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)

    if len(tags) < 2:
        return None, None

    latestTag = tags[-1]
    lastRevision = latestTag.name

    previousRevision = tags[-2].name

    if ignoreLastTag:
        lastRevision = 'HEAD'

    rev = previousRevision + '..' + lastRevision

    ids = set()
    for commit in repo.iter_commits(rev=rev):
        search = re.search('\[sc-(.+)\]', commit.message)
        if search:
            ids.add(search.group(1))

    return ids, latestTag

def getCurrentFileAsList():
    old = []
    try:
        with open(changelogPath, "r") as f:
            old = f.readlines()
    except FileNotFoundError:
        f = open(changelogPath, 'w')
        f.close()

    return old

def findInsertIndex(old):
    indexToInsert = 0
    try:
        indexToInsert = old.index(releaseHeaderLine)
    except ValueError:
        old.append(changelogHeaderLine)
        old.append(releaseHeaderLine)
        indexToInsert = old.index(releaseHeaderLine)

    return indexToInsert + 1

def insertStoriesName(old, insertIndex, latestTag, ids):
    old.insert(insertIndex, '### ' + latestTag.name + ' - ' + datetime.fromtimestamp(latestTag.tag.tagged_date).strftime('%d/%m/%Y') + '\n')
    insertIndex = insertIndex + 1

    storiesCount = 0
    headers = {'Shortcut-Token': shortcutToken}
    for storyId in ids:
        story_dict = requests.get(shortcutApiUrl + storyId, headers=headers).json()
        story_name = story_dict['name']
        old.insert(insertIndex, '- [sc-' + storyId + '] ' + story_name + '\n')
        insertIndex = insertIndex + 1
        storiesCount = storiesCount + 1

    with open(changelogPath, "w") as f:
        f.writelines(old)

    return storiesCount

def init():
    old = getCurrentFileAsList()
    insertIndex = findInsertIndex(old)
    ids, latestTag = getStoriesIdsAndLatestTag()

    if ids is None or latestTag is None:
        print('Not enough tags created')
        return

    if len(old) > insertIndex:
        search = re.search('### (.+) -', old[insertIndex])

        lastTagRecorded = ''
        if search:
            lastTagRecorded = search.group(1)

        if latestTag.name == lastTagRecorded:
            print('No new tag available')
            return

    count = insertStoriesName(old, insertIndex, latestTag, ids)

    print('Added tag', latestTag, 'with', count, 'shortcut stories')

if __name__ == '__main__':
    init()