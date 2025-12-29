orderbot/
├── bot.py
├── admin_panel.py
├── storage.py
├── config.py
├── data/products.json
└── qris/qris.jpg


## ⚙️ Instalasi
```bash
apt update -y
apt install python3 python3-pip -y
pip3 install python-telegram-bot==20.7

🔑 config.py
TOKEN = "TOKEN_BOT"
BOT_NAME = "NAMA_BOT"
ADMIN_ID = 123456789

📦 Produk
mkdir -p data qris
echo '{"panel_cloud":[]}' > data/products.json


Upload QRIS ke:

qris/qris.jpg

🚀 Jalankan Bot
python3 bot.py

👑 Admin
/admin
/addproduct Nama|Harga
/addstock ID|item1,item2

🛠️ Catatan

Restart bot setiap edit file

Jangan pakai reply_text di callback
