# Crypto Telegram Reporter

Automated crypto price reporting bot that sends formatted market updates to Telegram.

## 🚀 Features
- Fetches live crypto data (BTC, ETH, SOL, XRP)
- Calculates 24h changes
- Detects trend (UP / DOWN / MOON / FLAT)
- Sends formatted report to Telegram
- Daily scheduled execution

## 🛠 Tech Stack
- Python
- Requests
- Telegram Bot API
- Schedule
- dotenv

## 📊 Example Output
COIN | PRICE | CHG | TR

ETH  | $2161 | +5.1% | MOON
BTC  | $70030 | +4.0% | UP
…
## ⚙️ Setup
1. Clone repo
2. Create `.env` file:
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id
3. Install dependencies:
pip install -r requirements.txt
4. Run:
python telegram_bot.py
## 🔁 Automation
Runs daily using schedule.

---

Built as part of AI Automation Engineering portfolio.
