import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎬 Buy Tutorial — 150 ETB", callback_data="buy")],
        [InlineKeyboardButton("📚 What is included?", callback_data="info")]
    ]

    await update.message.reply_text(
        "🎬 Welcome to Lyrivo Tutorial!\n\n"
        "Learn how to create professional Lyrics Videos "
        "using Alight Motion.\n\n"
        "👇 Choose an option:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "buy":
        await query.edit_message_text(
            "💰 Tutorial Price: 150 ETB\n\n"
            "Payment system will be added next. 🔒\n\n"
            "After payment is confirmed, your tutorial "
            "will be delivered automatically. 🎬"
        )

    elif query.data == "info":
        await query.edit_message_text(
            "📚 Lyrivo Tutorial includes:\n\n"
            "🎬 Full Lyrics Video Tutorial\n"
            "📱 Alight Motion editing\n"
            "✨ Step-by-step explanation\n"
            "🔥 Professional Lyrics Style\n\n"
            "Price: 150 ETB"
        )


def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError("BOT_TOKEN is not set!")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Lyrivo Tutorial Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
