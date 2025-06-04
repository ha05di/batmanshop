from flask import Flask, request
import requests

# 你的 Telegram Bot Token
BOT_TOKEN = '7582978452:AAE1Zdz62epr589ezQSnZS9TdraznuW2Rgw'
# 你要推送的 chat_id（可以是你/管理员/群组）
CHAT_ID = '6837915435'

app = Flask(__name__)

@app.route('/order', methods=['POST'])
def order():
    data = request.json or request.form
    # 生成订单文本
    order_info = f"新订单：\n姓名: {data.get('name')}\n电话: {data.get('phone')}\n商品: {data.get('item')}\n规格: {data.get('spec')}\n数量: {data.get('qty')}\n备注: {data.get('note')}"
    # 推送到 Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": order_info})
    return {'ok': True}

if __name__ == '__main__':
    app.run()
