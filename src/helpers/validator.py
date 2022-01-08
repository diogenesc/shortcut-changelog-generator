import re

def check_if_tags_empty(tags):
    return tags is None

def check_if_ids_empty(ids):
    return ids is None

def check_if_tag_not_changed(file_lines, insert_index, last_tag):
    last_tag_on_changelog = ''
    if len(file_lines) > insert_index:
        search = re.search('### (.+) -', file_lines[insert_index])
        if search:
            last_tag_on_changelog = search.group(1)

    return last_tag.name == last_tag_on_changelog