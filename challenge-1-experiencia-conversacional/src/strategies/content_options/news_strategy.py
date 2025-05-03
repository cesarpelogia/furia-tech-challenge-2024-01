from telebot.types import ReplyKeyboardMarkup, KeyboardButton

class NewsStrategy:
    def execute(self, message, bot, user_data):
        content = (
            "🔥 *Notícias e próximos jogos da FURIA!*\n\n"
            "Acompanhe todas as atualizações sobre a equipe, incluindo resultados, "
            "próximos jogos e muito mais no link abaixo:\n\n"
            "🔗 [Veja mais na Draft5](https://draft5.gg/equipe/330-FURIA)"
        )

        markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add(KeyboardButton("Voltar 🔙"))

        bot.send_message(
            message.chat.id,
            content,
            parse_mode="Markdown",
            reply_markup=markup
        )