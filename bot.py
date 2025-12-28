from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import json
from config import TOKEN, BOT_NAME

def load_products():
    with open("data/products.json") as f:
        return json.load(f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text=f"""👋 Halo, {user.first_name}!

Selamat datang di 🌐 {BOT_NAME} 🚀

🧑 Nama : {user.first_name}
🔗 Username : @{user.username}
🆔 User ID : {user.id}
"""
    keyboard=[
        [InlineKeyboardButton("📦 Produk",callback_data="cat_panel")],
        [InlineKeyboardButton("📂 Kategori",callback_data="kategori")],
        [InlineKeyboardButton("🏠 Home",callback_data="home")]
    ]
    if update.message:
        await update.message.reply_text(text,reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await update.callback_query.edit_message_text(text,reply_markup=InlineKeyboardMarkup(keyboard))

async def kategori(update:Update,context:ContextTypes.DEFAULT_TYPE):
    q=update.callback_query; await q.answer()
    kb=[
        [InlineKeyboardButton("☁️ DIGITAL OCEAN CLOUD",callback_data="cat_panel")],
        [InlineKeyboardButton("📱 APK PREMIUM",callback_data="cat_apk")],
        [InlineKeyboardButton("🔐 Proxy IP",callback_data="cat_proxy")],
        [InlineKeyboardButton("🏠 Home",callback_data="home")]
    ]
    await q.edit_message_text("📂 Pilih Kategori",reply_markup=InlineKeyboardMarkup(kb))

async def produk_panel(update:Update,context:ContextTypes.DEFAULT_TYPE):
    q=update.callback_query; await q.answer()
    data=load_products()["panel_cloud"]
    text="📦 Produk panel_cloud
━━━━━━━━━━━━"
    kb=[]
    for p in data:
        text+=f"\n👉 {p['name']}\n📦 {p['stock']} | 💰 {p['price']:,}"
        kb.append([InlineKeyboardButton(f"🛒 Beli {p['id']}",callback_data="buy")])
    kb.append([InlineKeyboardButton("⬅️ Kembali",callback_data="kategori")])
    await q.edit_message_text(text,reply_markup=InlineKeyboardMarkup(kb))

async def router(update:Update,context:ContextTypes.DEFAULT_TYPE):
    d=update.callback_query.data
    if d=="home": await start(update,context)
    elif d=="kategori": await kategori(update,context)
    elif d=="cat_panel": await produk_panel(update,context)

app=ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(CallbackQueryHandler(router))
app.run_polling()
