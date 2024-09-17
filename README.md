### Arithmetic Progression Calculator

A minimal Telegram bot that calculates the n'th term of an arithmetic progression (AP) based on the values provided by the user.

---

## A Minimal Telegram Bot for Arithmetic Progression Calculation

This Telegram bot calculates the n'th term of an arithmetic progression (AP) based on the values provided by the user.

## Features
- Accepts three inputs: `first_term`, `common_difference`, and `num_terms`.
- Calculates the n'th term of the arithmetic progression.
- Provides an interactive interface via Telegram.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Local Host](#local-host)
3. [Running the Bot in the Background](#running-the-bot-in-the-background)
4. [License](#license)

---

## Prerequisites

To set up and run this bot, you will need:
- A Telegram account.
- A bot token from [BotFather](https://core.telegram.org/bots#botfather).
- Python 3.x installed on your local or remote machine.
- Access to a VPS (if deploying the bot on a server) or Local Host.

### Required Python Libraries
Make sure to install the following Python library:
```bash
pip install python-telegram-bot --upgrade
```

---

## Local Host

### 1. Clone the Repository

```bash
git clone https://github.com/iSamarthDubey/APCalcBot.git
cd APCalcBot
```

### 2. Set up the Bot

1. Go to Telegram and create a new bot using **BotFather**. Follow the instructions and obtain the **API token**.
2. Replace `YOUR_API_TOKEN` in `bot.py` with your actual bot token.

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Bot

```bash
python bot.py
```

Now, your bot should be up and running locally. You can interact with it using the Telegram app.

---

## Running the Bot in the Background

To keep your bot running after disconnecting from the VPS, you can use one of the following options:

### Option 1: `nohup`

`nohup` allows your bot to keep running in the background:
```bash
nohup python3 bot.py &
```

### Option 2: `screen`

`screen` allows you to create a persistent session that you can reconnect to:
1. Install `screen`:
   ```bash
   sudo apt install screen
   ```

2. Create a new screen session:
   ```bash
   screen -S APCalcBot
   ```

3. Run your bot inside the screen:
   ```bash
   python3 bot.py 
   ```

4. Detach from the screen (leave it running in the background):
   ```bash
   Ctrl + A, then D
   ```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

### Notes:
- Make sure to edit `.env` using `nano .env` with the correct values.
- After deployment, your bot will remain operational and available for users to interact with on Telegram.

---
