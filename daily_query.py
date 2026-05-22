import requests
import os
import datetime

# 从环境变量读取
TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")

print("=== 调试信息 ===")
print(f"Token 是否存在: {TG_BOT_TOKEN is not None}")
print(f"Chat ID 是否存在: {TG_CHAT_ID is not None}")

def get_data():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"✅ 每日查询任务完成\n时间：{now}\n状态：正常"

def send_tg(text):
    if not TG_BOT_TOKEN or not TG_CHAT_ID:
        print("❌ 错误：环境变量缺失！")
        return
    url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TG_CHAT_ID, "text": text}
    print(f"请求URL: {url}")
    print(f"请求参数: {payload}")
    res = requests.post(url, json=payload)
    print(f"响应状态码: {res.status_code}")
    print(f"响应内容: {res.json()}")

send_tg(get_data())