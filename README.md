# Crypto Telegram Reporter

Automated crypto price reporting bot that sends formatted market updates to Telegram.

## 📌 Project Purpose
This project demonstrates building an automated data pipeline:
API → processing → formatted output → Telegram delivery.

## 🚀 Features
- Fetches live crypto data (BTC, ETH, SOL, XRP)
- Calculates 24h changes
- Detects trend (UP / DOWN / MOON / FLAT)
- Sends formatted report to Telegram
- Supports one-time run and scheduled execution

## 🛠 Tech Stack
- Python
- Requests
- Telegram Bot API
- Schedule
- python-dotenv

## 📊 Example Output
```
COIN | PRICE  | CHG   | TR
ETH  | $2161  | +5.1% | MOON
BTC  | $70030 | +4.0% | UP
```

## ⚙️ Setup

1. Clone the repository
```bash
git clone https://github.com/rory1337-prog/crypto-telegram-reporter.git
cd crypto-telegram-reporter
```

2. Create `.env` file
```env
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run once:
```bash
python telegram_bot.py once
```

Run with scheduler:
```bash
python telegram_bot.py run
```

## 🔁 Automation
Uses Python scheduler to send daily reports at a fixed time.

---

Built as part of AI Automation Engineering portfolio.


