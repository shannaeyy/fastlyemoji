# Telegram Emoji Challenge Bot

This Telegram bot runs in groups and starts an emoji challenge every 20 minutes. The first person to respond with the correct emoji wins!

## Features

- Emoji challenge every 20 minutes.
- First correct reply wins the round.
- Leaderboard per group.
- Persistent scores using MongoDB.
- Inline button to promote a Telegram channel.

## Setup

### Locally

1. Clone this repo.
2. Create a `.env` file from `.env.example`.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the bot:
   ```bash
   python main.py
   ```

### On Render

1. Create a new **Web Service** on [Render](https://render.com/).
2. Choose your repo and select the `Docker` environment.
3. Set environment variables:
   - `TELEGRAM_TOKEN`
   - `MONGODB_URI`
4. Deploy.

## Docker

To run locally with Docker:

```bash
docker build -t telegram-emoji-bot .
docker run --env-file .env telegram-emoji-bot
```

## License

MIT
