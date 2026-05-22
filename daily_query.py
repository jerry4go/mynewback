import requests
import datetime

# ========== 配置项，后续填仓库密钥 ==========
TG_BOT_TOKEN = ""
TG_CHAT_ID = ""

def get_query_data():
    """你的自定义查询任务，替换成自己接口/数据库/爬虫逻辑"""
    # 示例：获取当日时间+模拟查询数据
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query_result = f"""
📅 每日查询任务播报
执行时间：{now}
查询状态：正常完成
模拟查询数据：测试任务数据123
    """
    return query_result

def send_telegram(msg):
    """推送消息到Telegram"""
    url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TG_CHAT_ID,
        "text": msg
    }
    res = requests.post(url, data=data)
    print("推送结果：", res.json())

if __name__ == "__main__":
    result = get_query_data()
    send_telegram(result)