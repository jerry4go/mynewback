import requests
import os
import datetime

TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")

# ========== 用不受屏蔽的公开接口 ==========
def get_eth_price():
    try:
        # 这个接口 GitHub 绝对能访问！
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "ethereum",
            "vs_currencies": "usdt",
            "include_24hr_change": "true"
        }
        res = requests.get(url, params=params, timeout=10)
        data = res.json()

        price = data["ethereum"]["usdt"]
        change = data["ethereum"]["usdt_24h_change"]
        sign = "+" if change >= 0 else ""

        return f"""💰 ETH/USDT 实时行情
现价：${price:,.2f}
24h 涨跌：{sign}{change:.2f}%"""

    except Exception as e:
        return f"❌ 获取失败：{str(e)}\n错误类型：{type(e).__name__}"

def send_tg(msg):
    url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TG_CHAT_ID, "text": msg}
    requests.post(url, json=payload)

# 执行
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
content = f"📅 {now}\n{get_eth_price()}"
send_tg(content)