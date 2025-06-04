from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

BOT_TOKEN = '7582978452:AAE1Zdz62epr589ezQSnZS9TdraznuW2Rgw'
CHAT_ID = '6837915435'

app = Flask(__name__)
CORS(app)

@app.route('/order', methods=['POST'])
def order():
    data = request.json or request.form
    order_info = f"新订单：\n姓名: {data.get('name')}\n电话: {data.get('phone')}\n商品: {data.get('item')}\n规格: {data.get('spec')}\n数量: {data.get('qty')}\n备注: {data.get('note')}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": order_info})
    return jsonify({'ok': True})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
