from flask import Flask, request
from telegram import Bot

app = Flask(__name__)
TOKEN = '7582978452:AAE1Zdz62epr589ezQSnZS9TdraznuW2Rgw'           # 你的Telegram Bot Token
ADMIN_ID = 6837915435               # 管理员的chat_id
CHANNEL_USERNAME = '@yourchannel'  # 频道用户名，可选

bot = Bot(token=TOKEN)

@app.route('/notify_admin', methods=['POST'])
def notify_admin():
    data = request.json
    if not data: return {'result':'no data'}, 400

    # 订单内容格式化
    items_str = "\n".join([
        f"- {item.get('name')} ({item.get('spec','')}) ×{item.get('qty')}"
        for item in data.get('items', [])
    ])
    text = (
        f"🛒 <b>新订单</b>！\n"
        f"姓名：{data.get('name','')}\n"
        f"电话：{data.get('phone','')}\n"
        f"地址：{data.get('address','')}\n"
        f"商品：\n{items_str}\n"
        f"总价：<b>{data.get('total')}</b>\n"
        f"备注：{data.get('note','')}\n"
        f"下单时间：{data.get('order_id','')[-13:]}"
    )
    try:
        bot.send_message(chat_id=ADMIN_ID, text=text, parse_mode='HTML')
    except Exception as e:
        print('发送失败', e)
        return {'result':'fail'}, 500
    return {'result':'ok'}

# ==== 频道推送下单链接接口 ====
@app.route('/push_link', methods=['POST'])
def push_link():
    url = request.json.get('url')
    bot.send_message(chat_id=CHANNEL_USERNAME, text=f"🛒 <b>点这里进入商城下单</b>：\n{url}", parse_mode='HTML')
    return {'result':'ok'}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
