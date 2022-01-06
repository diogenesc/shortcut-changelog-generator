import requests
import helpers.settings as settings
from models.story import Story

api_url = 'https://api.app.shortcut.com/api/v3/stories/'

def stories_list(ids):
    headers = {'Shortcut-Token': settings.api_token}

    stories_list = []
    for story_id in ids:
        story_dict = requests.get(api_url + story_id, headers=headers).json()

        story_name = story_dict['name']
        story_url = story_dict['app_url']

        stories_list.append(Story(story_id, story_name, story_url))

    return stories_list