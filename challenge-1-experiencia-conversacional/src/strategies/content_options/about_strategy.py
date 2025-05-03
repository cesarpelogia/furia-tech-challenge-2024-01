from telebot.types import ReplyKeyboardMarkup, KeyboardButton

class AboutStrategy:
    def execute(self, message, bot, user_data):
        """
        Envia informações sobre a FURIA com um botão para voltar ao menu inicial.
        """
        content = (
            "🐆 *Sobre a FURIA*\n\n"
            "Conheça mais sobre a história, valores e conquistas da FURIA no link abaixo:\n\n"
            "🔗 [Quem Somos - FURIA](https://www.furia.gg/quem-somos)"
        )

        markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add(KeyboardButton("Voltar 🔙"))

        bot.send_message(
            message.chat.id,
            content,
            parse_mode="Markdown",
            reply_markup=markup
        )