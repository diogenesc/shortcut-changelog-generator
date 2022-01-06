import helpers.git as git
import helpers.file as file
import helpers.settings as settings
import helpers.shortcut as shortcut
import helpers.notifier as notifier
import helpers.validator as validator
from termcolor import colored

def init():
    old_file = file.get_file_lines()
    insert_index = file.find_insert_index(old_file)
    last_tag = git.last_tag()

    if validator.check_if_tags_empty(last_tag):
        print(colored(f'No tags', 'red'))
        return

    ids = None
    if settings.ignore_last_tag == True:
        ids = git.filter_stories_id_after_last_tag()
    else:
        ids = git.filter_stories_id_between_tags()

    if validator.check_if_ids_empty(ids):
        print(colored(f'No stories to add', 'yellow'))
        return

    if validator.check_if_tag_not_changed(old_file, insert_index, last_tag):
        print(colored(f'No new tag created', 'yellow'))
        return

    stories_list = shortcut.stories_list(ids)

    count = file.insert_stories_on_changelog(old_file, insert_index, last_tag, stories_list)
    print(colored(f'Added tag {last_tag} with {count} shortcut stories', 'green'))

    if settings.telegram_send_diff == True:
        message = file.build_diff_message(last_tag, stories_list)
        notifier.telegram(message)


if __name__ == '__main__':
    init()