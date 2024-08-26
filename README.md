# AI Omni 🤖

![Static Badge](https://img.shields.io/badge/Python-3\.12-blue)
![Static Badge](https://img.shields.io/badge/Telegram_API-7\.4-re)

This is a GPT-4 Omni version chat integrated into a Telegram bot via the ProxyAPI service, featuring user authentication and a database for calculating token usage.

![logo](./assets/logo.jpg)

## How to Run

### Step 1: Create Environment Variables

Create a **.env** file in the root directory of your project and add the following environment variables:

- `TG_TOKEN` - Your Telegram bot token
- `AI_TOKEN` - Your ProxyAPI token
- `AI_BASE_URL` - Base URL of ProxyAPI
- `USERS` - User IDs for authentication
- `DATABASE_URL` - PostgreSQL URL
- `POSTGRES_USER` - PostgreSQL User
- `POSTGRES_PASSWORD` - PostgreSQL Password
- `POSTGRES_DB` - PostgreSQL DB Name

### Step 2: Create a Server Session

Before running the bot, create a session on the server:\

```
tmux new -s ai-omni
```

### Step 3: Run the Bot with Docker

To build and run the project using Docker, execute:\

```
docker compose up -d
```


### Your bot is now ready to use. Enjoy! 💫
