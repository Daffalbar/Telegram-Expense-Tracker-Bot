# 💸 Expense Tracker Telegram Bot

A simple Telegram bot to track your daily expenses and log them into Google Sheets. Built with Python, Google Sheets API, and Telegram Bot API.

## 📁 Project Structure
```
expense-tracker-telegram-bot/
├── credentials.json          # Google API credentials
├── .env                      # Environment variables (Telegram Token, Sheet Name)
├── main.py                   # Main bot script
├── requirements.txt          # Project dependencies
├── LICENSE                   # MIT License
└── README.md                 # Project documentation
```

## 🚀 Features
- Track expenses by sending messages like `Buy coffee 15000`
- Auto-log expenses to Google Sheets with timestamp
- Use `/rekap` to get a daily expense summary

## ⚙️ Setup Instructions

### 1. Google Sheets Setup
1. Create a new Google Sheet with headers:
   - `Tanggal`, `Deskripsi`, `Jumlah`
2. Go to [Google Cloud Console](https://console.cloud.google.com/):
   - Create a new project
   - Enable **Google Sheets API** and **Google Drive API**
   - Create Service Account credentials and download `credentials.json`
3. Share your Google Sheet with the service account email as **Editor**

### 2. Telegram Bot Setup
1. Open Telegram and chat with [@BotFather](https://t.me/BotFather)
2. Create a new bot with `/newbot`, give it a name and username
3. Copy the **Bot Token**

### 3. Environment Variables
Create a `.env` file:
```
TELEGRAM_TOKEN=your_bot_token
SHEET_NAME=your_sheet_name
```

### 4. Install Dependencies
```
pip install -r requirements.txt
```

### 5. Run the Bot
```
python main.py
```

## 🧠 How It Works
- User sends a message: `Beli makan siang 30000`
- Bot parses the message → logs timestamp, description, and amount to Google Sheets
- `/rekap` command summarizes today’s expenses from the Sheet

### 🔍 main.py
```python
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
```

## 📦 Dependencies
- `python-telegram-bot`
- `gspread`
- `oauth2client`
- `python-dotenv`

## 🤝 Contributing
Contributions are welcome! If you have suggestions, bug fixes, or improvements, feel free to open an issue or submit a pull request. Please follow standard Python coding conventions.

## 🙏 Credits
- Telegram Bot API by [Telegram](https://core.telegram.org/bots/api)
- Google Sheets API by [Google Cloud](https://cloud.google.com/sheets)
- Inspired by the need to simplify personal expense tracking

## 📄 License
This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

---
Made with ❤️ by M. Daffa Aulia Albar
