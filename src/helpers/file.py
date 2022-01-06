import os
import datetime
import helpers.settings as settings
from telegram.utils.helpers import escape_markdown

os.chdir(settings.work_dir)

changelog_header_line = '# CHANGELOG\n'
release_header_line = '## Releases\n'

def get_file_lines():
    file_lines = []
    try:
        with open(settings.changelog_path, "r") as f:
            file_lines = f.readlines()
    except FileNotFoundError:
        f = open(settings.changelog_path, 'w')
        f.close()

    return file_lines

def find_insert_index(file_lines):
    insert_index = 0
    try:
        insert_index = file_lines.index(release_header_line)
    except ValueError:
        file_lines.append(changelog_header_line)
        file_lines.append(release_header_line)
        insert_index = file_lines.index(release_header_line)

    return insert_index + 1

def build_diff_message(last_tag, stories_list):
    tag_date = datetime.datetime.fromtimestamp(last_tag.tag.tagged_date).strftime('%d/%m/%Y')

    text = escape_markdown(last_tag.name + ' - ' + tag_date + '\n\n', 2)

    for story_line in stories_list:
        escaped_id = story_line.id
        escaped_name = escape_markdown(story_line.name, 2)
        text = text + '\- [\[sc\-' + escaped_id + '\]](' + story_line.url + ') ' + escaped_name + '\n'

    return text


def insert_stories_on_changelog(file_lines, insert_index, last_tag, stories_list):
    tag_date = datetime.datetime.fromtimestamp(last_tag.tag.tagged_date).strftime('%d/%m/%Y')

    file_lines.insert(insert_index, '### ' + last_tag.name + ' - ' + tag_date + '\n')
    insert_index = insert_index + 1

    stories_count = 0
    for story_line in stories_list:
        file_lines.insert(insert_index, '- [\[sc\-' + story_line.id + '\]](' + story_line.url + ') ' + story_line.name + '\n')

        insert_index = insert_index + 1
        stories_count = stories_count + 1

    if settings.dry_run == False:
        with open(settings.changelog_path, "w") as f:
            f.writelines(file_lines)

    return stories_count