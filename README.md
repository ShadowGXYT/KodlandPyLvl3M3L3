# Portfolio Telegram Bot

This project is part of a Python course for students. It manages information about projects, skills, and project statuses in a SQLite database.

## Features

- Creates tables for projects, skills, project skills, and statuses
- Adds default skills and project statuses
- Manages project data in a local SQLite database
- Provides the basic structure for a Telegram bot

## Files

- `bot.py` — Telegram bot configuration
- `config.py` — Environment and database configuration
- `logic.py` — Database table creation
- `logic2.py` — Database management for projects and skills

## Requirements

- Python 3
- `pyTelegramBotAPI` package (`telebot`)

## Set the Telegram token

The bot token is not stored in the source code. Before starting the bot, set the environment variable:

```bash
export TELEGRAM_BOT_TOKEN="your_bot_token"
python bot.py
```

## Prepare the database

```bash
python logic.py
# or
python logic2.py
```

The local SQLite file `portfolio.db` is intentionally ignored by this repository.
