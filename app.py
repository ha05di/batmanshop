from flask import Flask, request, jsonify
from flask_cors import CORS
from telegram import Bot
import gspread

app = Flask(__name__)
CORS(app)

# Telegram Bot 配置（可删减）
TOKEN = '7582978452:AAE1Zdz62epr589ezQSnZS9TdraznuW2Rgw'
ADMIN_ID = 6837915435
bot = Bot(token=TOKEN)

# Google Sheet 配置
SHEET_NAME = 'Menu'    # Google Sheet 文件名
MENU_SHEET = 'menu'               # 菜单sheet名，和你sheet的tab名一致

# ====== 菜单接口：动态读取 Sheet ======
@app.route('/api/menu')
def menu():
    # gspread连接
    gc = gspread.service_account(filename='service_account.json')
    sh = gc.open(SHEET_NAME)
    ws = sh.worksheet(MENU_SHEET)
    data = ws.get_all_records()
    # 可选：过滤是否上架
    menu = [row for row in data if not row.get('是否上架') or row.get('是否上架').strip().upper() != 'N']
    return jsonify(menu)

# ...其它接口如前...
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
