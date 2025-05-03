from telebot.types import ReplyKeyboardMarkup, KeyboardButton

class WhereToWatchStrategy:
    def execute(self, message, bot, user_data, disable_web_page_preview=False):
        content = (
            "🎮 *Onde assistir os jogos da FURIA?*\n\n"
            "Acompanhe a FURIA AO VIVO nas principais plataformas:\n\n"
            "🟣 *Twitch*\n"
            "Transmissões ao vivo, bastidores e interação com a comunidade:\n"
            "👉 [twitch.tv/furiatv](https://www.twitch.tv/furiatv)\n\n"
            "📺 *YouTube*\n"
            "Conteúdos gravados, melhores momentos e transmissões:\n"
            "👉 [youtube.com/@FURIAggCS](https://www.youtube.com/@FURIAggCS)\n\n"
        )

        markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add(KeyboardButton("Voltar 🔙"))
        
        bot.send_message(
            message.chat.id,
            content,
            parse_mode="Markdown",
            reply_markup=markup,
            disable_web_page_preview=disable_web_page_preview
        )