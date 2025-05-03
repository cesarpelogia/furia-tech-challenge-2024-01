from telebot.types import ReplyKeyboardMarkup, KeyboardButton

class SocialMediaStrategy:
    def execute(self, message, bot, user_data, disable_web_page_preview=False):
        content = (
            "🔥 *Conecte-se com a FURIA nas redes sociais!*\n\n"
            "📸 *Instagram*\n"
            "Siga os bastidores, treinos e lifestyle da equipe:\n"
            "👉 [@furiagg](https://www.instagram.com/furiagg)\n\n"
            "🎵 *TikTok*\n"
            "Veja conteúdos rápidos, desafios e momentos únicos da FURIA:\n"
            "👉 [@furiagg](https://www.tiktok.com/@furiagg)\n\n"
            "🐦 *Twitter (X)*\n"
            "Fique por dentro das provocações, reações e atualizações em tempo real:\n"
            "👉 [@furiagg](https://twitter.com/furiagg)\n\n"
            "📘 *Facebook*\n"
            "Acompanhe postagens oficiais, eventos e mais da FURIA:\n"
            "👉 [FURIA no Facebook](https://www.facebook.com/furiagg)\n"
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