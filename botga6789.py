from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'GA6789 xin chào {update.effective_user.first_name} \n❤️ Nạp đầu tặng 100% (Đá gà, Casino, Thể Thao, Slot...)\n❤️ Nạp đầu mỗi ngày tặng 10% (Thể thao, Đá gà)\n❤️ Bảo hiểm 8% mỗi ngày (Đá gà)\n💋 Link đăng ký: https://daga1111.com')


app = ApplicationBuilder().token("7961294831:AAGEOAbfx3KYYm9dCZ8yHE-QWf-IhK0jXd8").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()