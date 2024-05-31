# AI Omni

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
- `POSTGRES_URL` - PostgreSQL URL

### Step 2: Install Dependencies

Run the following commands to install the necessary dependencies and activate the virtual environment:

```
poetry install
poetry shell
```

### Step 3: Create a Server Session

Before running the bot, create a session on the server. For example, using tmux:

```
tmux new-session -s ai-omni
```

### Step 4: Run the Makefile

To build and run the project, execute:

```
make all
```

### Step 5: Individual Commands

Alternatively, you can run the following commands individually:

```
make lint
make run
```

Your bot is now ready to use. Enjoy!



