from bot.bot_instance import bot
from handlers import start_handler

if __name__ == "__main__":
    print("Bot rodando...")
    print("Para acessar, acesse: https://t.me/hermesFuriaBot")
    bot.polling()