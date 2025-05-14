# 💸 Expense Tracker Telegram Bot

A simple Telegram bot to track your daily expenses and log them into Google Sheets. Built with Python, Google Sheets API, and Telegram Bot API.

## 📁 Project Structure
```
expense-tracker-telegram-bot/
├── credentials.json          # Google API credentials
├── .env                      # Environment variables (Telegram Token, Sheet Name)
└── main.py                   # Main bot script
```

## 🚀 Features
- Track expenses by sending messages like `Beli Kopi 15000`
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

### 4. Main Bot Script Setup
1. Create new file and give it name `main.py`
2. Copy [main.py](./main.py) file to your main.py file.

### 5. Run the Bot
```
python main.py
```

## 🧠 How It Works
- User sends a message: `Beli Batagor 12000`
- Bot parses the message → logs timestamp, description, and amount to Google Sheets
- `/rekap` command summarizes today’s expenses from the Sheet

## 📦 Dependencies
- `python-telegram-bot`
- `gspread`
- `oauth2client`
- `python-dotenv`

## 🤝 Contributing
Contributions are welcome! If you have suggestions, bug fixes, or improvements, feel free to open an issue or submit a pull request. Please follow standard Python coding conventions.

## 📄 License
This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.
