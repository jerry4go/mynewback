import requests
import os
import datetime

TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")

def get_eth_full_ticker():
    try:
        url = "https://api.coingecko.com/api/v3/coins/ethereum"
        params = {
            "localization": "false",
            "tickers": "false",
            "community_data": "false",
            "developer_data": "false"
        }
        res = requests.get(url, params=params, timeout=15)
        res.raise_for_status()
        data = res.json()

        market = data["market_data"]
        price = market["current_price"]["usd"]
        change_pct = market["price_change_percentage_24h"]
        high24h = market["high_24h"]["usd"]
        low24h = market["low_24h"]["usd"]
        volume_eth = market["total_volume"]["eth"]
        volume_usd = market["total_volume"]["usd"]

        sign = "+" if change_pct >= 0 else ""

        text = f"""💰 ETH/USDT 完整行情
——————————————
现价：${price:,.2f}
24h涨跌：{sign}{change_pct:.2f}%
24h最高：${high24h:,.2f}
24h最低：${low24h:,.2f}
24h成交量：{volume_eth:,.2f} ETH
24h成交额：${volume_usd/1e9:.2f} B
——————————————"""
        return text
    except Exception as e:
        return f"❌ 获取行情失败：{str(e)}"

def send_tg(msg):
    url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TG_CHAT_ID, "text": msg}
    requests.post(url, json=payload)

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
ticker_text = get_eth_full_ticker()
full_msg = f"📅 {now}\n{ticker_text}"
send_tg(full_msg)