import requests
import os
import datetime

# ---------- 配置 ----------
TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")
SYMBOL = "ETHUSDT"

# ---------- 获取 24h 完整行情 ----------
def get_eth_usdt_24hr():
    try:
        url = "https://api.binance.com/api/v3/ticker/24hr"
        params = {"symbol": SYMBOL}
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()

        lastPrice = float(data["lastPrice"])
        priceChange = float(data["priceChange"])
        priceChangePercent = float(data["priceChangePercent"])
        highPrice = float(data["highPrice"])
        lowPrice = float(data["lowPrice"])
        volume = float(data["volume"])           # ETH 量
        quoteVolume = float(data["quoteVolume"]) # USDT 量

        # 涨跌符号
        sign = "+" if priceChange >= 0 else ""

        text = f"""💰 {SYMBOL} 行情
现价：${lastPrice:,.2f}
24h：{sign}{priceChange:,.2f}（{sign}{priceChangePercent:.2f}%）
最高：${highPrice:,.2f}
最低：${lowPrice:,.2f}
成交量：{volume:,.2f} ETH / {quoteVolume:,.2f} USDT"""
        return text
    except Exception as e:
        return f"❌ 获取行情失败：{str(e)}"

# ---------- 发送 Telegram ----------
def send_tg(text):
    url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TG_CHAT_ID, "text": text}
    requests.post(url, json=payload)

# ---------- 主程序 ----------
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
report = f"📅 时间：{now}\n" + get_eth_usdt_24hr()
send_tg(report)