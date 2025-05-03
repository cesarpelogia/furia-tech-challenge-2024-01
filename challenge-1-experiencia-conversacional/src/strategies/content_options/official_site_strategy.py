from telebot.types import ReplyKeyboardMarkup, KeyboardButton

class OfficialSiteStrategy:
    def execute(self, message, bot, user_data):
        """
        Envia informações sobre o site oficial da FURIA com um botão para voltar ao menu inicial.
        """
        # Conteúdo da mensagem
        content = (
            "**🔥 VIVA A FURIA! 🔥**\n\n"
            "Descubra o universo da **FURIA**:\n\n"
            "- 🎮 **Esports de elite**: CS2, Valorant, LoL, Rocket League e mais\n"
            "- 👕 **Moda urbana autêntica**: colaborações com Adidas, ZOR, My Hero Academia e outros\n"
            "- 🎥 **Conteúdo que pulsa**: streams, bastidores e novidades direto da fonte\n\n"
            "Seja parte do movimento que vai **além do jogo**.\n\n"
            "🔗 [Acesse o site oficial da FURIA](https://www.furia.gg)"
        )

        # Criação do teclado com o botão "Voltar"
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add(KeyboardButton("Voltar 🔙"))

        # Envia a mensagem com o botão
        bot.send_message(
            message.chat.id,
            content,
            parse_mode="Markdown",
            reply_markup=markup
        )