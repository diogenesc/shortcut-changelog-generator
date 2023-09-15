import re
import helpers.settings as settings
from git import Repo

def get_repo_from_workdir():
    return Repo(settings.repo_path)

def tags_sorted():
    repo = get_repo_from_workdir()
    print("DEBUG AQUI: ")
    print(repo)
    print(repo.tags)
    return repo.tags

def filter_stories_id_between_tags():
    repo = get_repo_from_workdir()
    tags = tags_sorted()

    if len(tags) < 2:
        return None

    last_tag = tags[-1].name
    previous_tag = tags[-2].name

    ids = set()
    for commit in repo.iter_commits(rev=(previous_tag + '..' + last_tag)):
        search = re.search('\[sc-(.+)\]', commit.message)
        if search:
            ids.add(search.group(1))

    return ids

def filter_stories_id_after_last_tag():
    repo = get_repo_from_workdir()
    tags = tags_sorted()

    if len(tags) < 1:
        return None

    last_revision = 'HEAD'
    previous_tag = tags[-1].name

    ids = set()
    for commit in repo.iter_commits(rev=(previous_tag + '..' + last_revision)):
        search = re.search('\[sc-(.+)\]', commit.message)
        if search:
            ids.add(search.group(1))

def last_tag():
    tags = tags_sorted()

    if len(tags) < 1:
        return None

    return tags[-1]