from flask import Flask, request
import requests

BOT_TOKEN = '7582978452:AAE1Zdz62epr589ezQSnZS9TdraznuW2Rgw'
CHAT_ID = '6837915435'  # 填你自己/群组/管理员的 chat_id

app = Flask(__name__)

@app.route('/order', methods=['POST'])
def order():
    data = request.json or request.form
    tg_info = (
        f"🆔TG ID: {data.get('telegram_id', '')}\n"
        f"👤Username: @{data.get('telegram_name', '')}\n"
        f"姓名: {data.get('name', '')}\n"
        f"电话: {data.get('phone', '')}\n"
        f"商品: {data.get('item', '')} 规格: {data.get('spec', '')} 数量: {data.get('qty', '')}\n"
        f"备注: {data.get('note', '')}"
    )
    # 可附上用户头像URL data.get('photo_url')
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": tg_info})
    return {'ok': True}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
