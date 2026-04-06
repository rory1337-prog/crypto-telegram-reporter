import schedule
import time
import requests
import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(dotenv_path=Path(__file__).with_name(".env"), override=True)

bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()

telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

def get_trend(change):
    if change > 5:
        return "MOON"
    elif change > 1:
        return "UP"
    elif abs(change) < 1:
        return "FLAT"
    else:
        return "DOWN"


def build_report(portfolio, changes):
    valid_items = [
        (coin, price)
        for coin, price in portfolio.items()
        if changes[coin] is not None
        ]
    if not valid_items:
        return "⚠️ No valid market data"
    
    sorted_portfolio = sorted(
        valid_items,
        key=lambda item: changes[item[0]],
        reverse=True
        )
    
    top_coin, _ = sorted_portfolio[0]
    top_change = changes[top_coin]
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    report = ""
    report += f"Updated: {now}\n\n"
    report += f"{'COIN':<4}|{'PRICE':^10}|{'CHG':^6}|TR\n"
    report += "-" * 30 + "\n"

    for coin, price in sorted_portfolio:
        change = changes[coin]

        if change is not None:
            trend = get_trend(change)
            sign = '+' if change > 0 else ''
            change_str = f"{sign}{change:.1f}%"

            report += f"{coin:<4}|{f'${price:,.2f}':>10}|{change_str:>6}|{trend}\n"

    report += f"\nTOP GAINER: {top_coin} ({top_change:.1f}%)"

    return report


def get_data():
    response = requests.get(
        url = "https://api.coingecko.com/api/v3/simple/price",
        params ={
            'ids': 'bitcoin,ethereum,solana,ripple',
            'vs_currencies': 'usd',
            'include_24hr_change': 'true'
        },
        timeout=10
    )
    
    data = response.json()
    
    if 'bitcoin' not in data:
        print("API ERROR:", data)
        return {}, {}
    portfolio = {
        'BTC': data['bitcoin']['usd'],
        'ETH': data['ethereum']['usd'],
        'SOL': data['solana']['usd'],
        'XRP': data['ripple']['usd']
    }
    
    changes = {
        'BTC': data['bitcoin'].get('usd_24h_change'),
        'ETH': data['ethereum'].get('usd_24h_change'),
        'SOL': data['solana'].get('usd_24h_change'),
        'XRP': data['ripple'].get('usd_24h_change')
        }
    
    return portfolio, changes

def send_to_telegram_report(report):
    payload = {
        "chat_id": chat_id,
        "text": f'<pre>{report}</pre>',
        "parse_mode": 'HTML'
    }
    response = requests.post(telegram_url, data=payload, timeout=10)
    
    print(response.status_code)
    print(response.text)   
    if response.status_code != 200:
        raise Exception(f"Telegram send failed: {response.status_code}")


def run_report():
    try:
        print("Running report...")
        portfolio, changes = get_data()
        report = build_report(portfolio, changes)
        send_to_telegram_report(report)
        print("Report sent")
    except Exception as e:
        print(f"ERROR: {e}")

import sys

if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else "once"

    if command == "once":
        run_report()

    elif command == "run":
        print("Scheduler started...")
        schedule.every().day.at("10:00").do(run_report)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Unknown command. Use: once or run")  