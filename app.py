from flask import Flask, request
from flask_cors import CORS
import requests

# 你的 Telegram Bot Token 和 chat_id
BOT_TOKEN = '7582978452:AAE1Zdz62epr589ezQSnZS9TdraznuW2Rgw'
CHAT_ID = '6837915435'   # 换成你自己的 chat_id

app = Flask(__name__)
CORS(app)  # 开启 CORS，允许跨域

@app.route('/')
def index():
    return 'API OK'

@app.route('/order', methods=['POST'])
def order():
    # 支持 JSON 或表单数据
    data = request.get_json() or request.form
    print("收到数据:", data)

    # 生成订单文本（可根据实际字段调整）
    order_info = (
        f"🛒 新订单：\n"
        f"姓名: {data.get('name', '')}\n"
        f"电话: {data.get('phone', '')}\n"
        f"商品: {data.get('item', '')}\n"
        f"规格: {data.get('spec', '')}\n"
        f"数量: {data.get('qty', '')}\n"
        f"备注: {data.get('note', '')}\n"
        f"Telegram: {data.get('telegram_name', '')} (ID: {data.get('telegram_id', '')})"
    )

    # 推送到 Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    resp = requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": order_info
    })

    print("推送结果:", resp.status_code, resp.text)
    return {'ok': True}

if __name__ == '__main__':
    # 本地调试用，部署 Render 时可删掉
    app.run(host='0.0.0.0', port=10000, debug=True)
