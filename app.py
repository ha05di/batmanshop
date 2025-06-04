from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

# 推荐用环境变量方式保密敏感信息，也可以直接写死
BOT_TOKEN = os.getenv("BOT_TOKEN") or '你的bot token'
CHAT_ID = os.getenv("ADMIN_CHAT_ID") or '你的chat id'

app = Flask(__name__)
CORS(app)  # 允许跨域

@app.route('/')
def index():
    return 'Batman1788下单API已上线'

@app.route('/order', methods=['POST'])
def order():
    data = request.json or request.form
    tg_id = data.get('tg_id') or '未知'
    tg_name = data.get('tg_name') or '未知'
    order_info = (
        f"🛒 新订单：\n"
        f"👤 Telegram: {tg_name} (ID: {tg_id})\n"
        f"姓名: {data.get('name')}\n"
        f"电话: {data.get('phone')}\n"
        f"商品: {data.get('item')}\n"
        f"规格: {data.get('spec')}\n"
        f"数量: {data.get('qty')}\n"
        f"备注: {data.get('note') or '无'}"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": order_info})
    return jsonify({'ok': True})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
