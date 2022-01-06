
# Shortcut Changelog Generator

A Python script to generate changelog based on shortcut stories referenced in commit messages


## Dependencies

- Python 3.8+
- Poetry
## Usage/Examples

```bash
poetry run python src/main.py
```

A changelog will be generated/updated at `$REPO_PATH` and 
a diff will be sended to Telegram if configured.

### Docker
```bash
docker container run -v repo_path/:/app --env-file=.env diogenesc/shortcut-changelog-generator
```
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

| Variable           | Required | Description                       | Default      |
|--------------------|----------|-----------------------------------|--------------|
| DRY_RUN            | no       | Execute without save the file     | false        |
| REPO_PATH          | yes      | Git repository path               | .             |
| SHORTCUT_TOKEN     | yes      | Shortcut API Token                |              |
| TELEGRAM_CHAT_ID   | no       | Telegram chat ID                  |              |
| TELEGRAM_BOT_TOKEN | no       | Telegram Bot Token                |              |
| TELEGRAM_SEND_DIFF | no       | Active telegram notifier          | false        |
| IGNORE_LAST_TAG    | no       | Use all commits until last commit | false        |
| CHANGELOG_PATH     | no       | Changelog path                    | CHANGELOG.md |

## Bitbucket Pipelines

This program can be used as a Bitbucket Pipe.

```yml
- pipe: docker://diogenesc/shortcut-changelog-generator
  variables:
    SHORTCUT_TOKEN: XXXXXXXXXXXXXXX
    TELEGRAM_CHAT_ID: 0000000
    TELEGRAM_BOT_TOKEN: XXXXXXXXXXXXXXX
    TELEGRAM_SEND_DIFF: true
    REPO_PATH: /opt/atlassian/pipelines/agent/build
```