import logging
import os
from datetime import datetime

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Load env
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
SHEET_NAME = os.getenv("SHEET_NAME")

# Logging
logging.basicConfig(level=logging.INFO)

# Setup Google Sheet
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open(SHEET_NAME).sheet1

# Handler pengeluaran
async def handle_expense(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    parts = text.rsplit(' ', 1)
    
    if len(parts) != 2 or not parts[1].isdigit():
        await update.message.reply_text("Format salah. Contoh: Beli kopi 15000")
        return

    description, amount = parts
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    sheet.append_row([today, description, int(amount)])

    await update.message.reply_text("Tercatat! 💾")

# Handler rekap
async def rekap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    records = sheet.get_all_records()
    today = datetime.now().strftime("%Y-%m-%d")
    total = 0
    details = []

    for row in records:
        if row['Tanggal'].startswith(today):
            jumlah = int(row['Jumlah'])
            total += jumlah
            details.append(f"{row['Deskripsi']} - {jumlah:,}")

    if details:
        message = "📊 Pengeluaran Hari Ini:\n" + "\n".join(details)
        message += f"\n\n💰 Total: {total:,}"
    else:
        message = "Belum ada pengeluaran hari ini. 🧘"

    await update.message.reply_text(message)

# Main
if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_expense))
    app.add_handler(CommandHandler("rekap", rekap))

    print("Bot berjalan...")
    app.run_polling()
