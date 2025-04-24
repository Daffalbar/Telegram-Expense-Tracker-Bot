# 💸 Telegram Expense Tracker Bot

Sebuah bot Telegram sederhana berbasis Python yang memungkinkan pengguna mencatat dan merekap pengeluaran harian langsung dari Telegram ke Google Sheets secara otomatis. Cocok untuk kamu yang ingin mengatur keuangan pribadi secara praktis dan efisien.

## ✨ Fitur

- 📥 **Catat Pengeluaran**  
  Cukup kirim pesan seperti `Beli kopi 15000` dan pengeluaran langsung tercatat.

- 📊 **Rekap Harian**  
  Kirim perintah `/rekap` untuk melihat semua pengeluaran hari ini dan totalnya.

- ☁️ **Terhubung ke Google Sheets**  
  Data dicatat otomatis ke spreadsheet Google Sheet kamu, aman dan mudah diakses.

## 📦 Teknologi yang Digunakan

- Python 3
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [Google Sheets API](https://developers.google.com/sheets/api)
- gspread
- oauth2client
- python-dotenv

## 🛠 Instalasi

1. **Clone repositori ini**  
   ```bash
   git clone https://github.com/username/telegram-expense-tracker-bot.git
   cd telegram-expense-tracker-bot
   ```

2. **Pasang dependensi**
   ```bash
   pip install -r requirements.txt
   ```

3. **Buat dan konfigurasi Google Sheet & API**
   - Buat spreadsheet dengan kolom: `Tanggal`, `Deskripsi`, `Jumlah`
   - Aktifkan Google Sheets API dan Google Drive API
   - Buat service account dan unduh `credentials.json`
   - Share sheet ke email service account sebagai editor

4. **Buat Bot Telegram**
   - Chat ke [@BotFather](https://t.me/BotFather), buat bot baru, dan salin token-nya

5. **Konfigurasi `.env`**
   ```env
   TELEGRAM_TOKEN=token_dari_BotFather
   SHEET_NAME=NamaSheetKamu
   ```

6. **Jalankan bot**
   ```bash
   python main.py
   ```

## 📄 Struktur File

```
telegram-expense-tracker-bot/
├── main.py
├── credentials.json
├── .env
├── requirements.txt
└── README.md
```

## 📷 Contoh Penggunaan

- Kirim: `Beli nasi goreng 20000`  
  ✅ Bot membalas: `Tercatat! 💾`

- Kirim: `/rekap`  
  📊 Bot membalas total pengeluaran hari ini

## 🎥 Akan Tersedia
Tutorial lengkap akan segera tersedia di [YouTube Channel Saya](https://youtube.com/@channelmu) 🚀

## 📄 Lisensi

MIT License © 2025 [Daffa Albar](https://github.com/daffaalbar)

---

## 📜 MIT License

Copyright (c) 2025 Daffa Albar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
