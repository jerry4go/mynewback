import requests
import os
import datetime

TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")

def get_eth_price():
    try:
        # 注意：只能用 usd，不能用 usdt
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "ethereum",
            "vs_currencies": "usd",
            "include_24hr_change": "true"
        }
        res = requests.get(url, params=params, timeout=10)
        res.raise_for_status()
        data = res.json()

        price = data["ethereum"]["usd"]
        change = data["ethereum"]["usd_24h_change"]
        sign = "+" if change >= 0 else ""

        return f"""💰 ETH/USDT（≈USD）
现价：${price:,.2f}
24h 涨跌：{sign}{change:.2f}%"""

    except Exception as e:
        return f"❌ 获取失败：{str(e)}\n返回内容：{res.text if 'res' in locals() else '无'}"

def send_tg(msg):
    url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TG_CHAT_ID, "text": msg}
    requests.post(url, json=payload)

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
content = f"📅 {now}\n{get_eth_price()}"
send_tg(content)