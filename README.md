# AI Omni 🤖

![Static Badge](https://img.shields.io/badge/Python-3\.12-blue)
![Static Badge](https://img.shields.io/badge/Telegram_API-7\.4-re)

This is the GPT-4 Omni model integrated into the Telegram bot via the ProxyAPI service.

![logo](./assets/logo.jpg)

## How to Run

### Step 1: Create Environment Variables

Create a **.env** file in the root directory of your project and add the following environment variables:

- `tg_token` - Your Telegram bot token
- `tg_ids` - User IDs for authentication
- `ai_token` - Your ProxyAPI token
- `ai_base_url` - Base URL of ProxyAPI
- `pg_url` - PostgreSQL URL
- `pg_user` - PostgreSQL User
- `pg_password` - PostgreSQL Password
- `pg_db_name` - PostgreSQL DB Name

### Step 2: Create a Server Session

Before running the bot, create a session on the server:\

```bash
tmux new -s ai-omni
```

### Step 3: Run the Bot with Docker

To build and run the project using Docker, execute:\

```bash
docker compose up -d
```

### Your bot is now ready to use. Enjoy! 💫
