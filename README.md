## Arithmetic Progression Calculator

A minimal Telegram bot that calculates the n'th term of an arithmetic progression (AP) based on the values provided by the user.

---

### A Minimal Telegram Bot for Arithmetic Progression Calculation

This Telegram bot calculates the n'th term of an arithmetic progression (AP) based on the values provided by the user.

## Features
- Accepts three inputs: `first_term`, `common_difference`, and `num_terms`.
- Calculates the n'th term of the arithmetic progression.
- Provides an interactive interface via Telegram.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Local Host](#local-host)
3. [License](#license)

---

## Prerequisites

To set up and run this bot, you will need:
- A Telegram account.
- A bot token from [BotFather](https://core.telegram.org/bots#botfather).
- Python 3.x installed on your local or remote machine.
- Access to a VPS (if deploying the bot on a server) or Local Host.


## Local Host

### 1. Clone the Repository

```bash
git clone https://github.com/iSamarthDubey/APCalcBot.git
cd APCalcBot
```

### 2. Edit the .env with correct Values
Edit `.env` using `nano .env` with the correct value (Bot token).

### 3. Setup Required Dependencies

1. Create a new screen session:
   ```bash
   screen -S APCalcBot
   ```
2. **Create a virtual environment** in your project directory:
   ```bash
   virtualenv venv
   ```

3. **Activate the virtual environment**:
     ```bash
     source venv/bin/activate
     ```
Once activated, you will see the virtual environment name in your terminal prompt.

4. **Install Requirements**:
With the virtual environment activated, install the required Python libraries.
   ```bash
   pip install -r requirements.txt
   ```

5. **Run your bot inside the screen**:
   ```bash
   python3 bot.py 
   ```
Now, your bot should be up and running locally. You can interact with it using the Telegram app.

6. **Detach from the screen (leave it running in the background)**:
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
