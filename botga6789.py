import telebot

TOKEN = "7961294831:AAGEOAbfx3KYYm9dCZ8yHE-QWf-IhK0jXd8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    first_name = message.from_user.first_name
    reply_text = (
        f"GA6789 xin chào {first_name}!\n"
        "❤️ Nạp đầu tặng 100% (Đá gà, Casino, Thể Thao, Slot...)\n"
        "❤️ Nạp đầu mỗi ngày tặng 10% (Thể thao, Đá gà)\n"
        "❤️ Bảo hiểm 8% mỗi ngày (Đá gà)\n"
        "💋 Link đăng ký: https://daga1111.com"
    )
    bot.reply_to(message, reply_text)

bot.infinity_polling()
