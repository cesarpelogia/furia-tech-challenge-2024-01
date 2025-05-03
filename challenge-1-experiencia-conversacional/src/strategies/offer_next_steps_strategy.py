from strategies.response_strategy import ResponseStrategy
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Ajuste dos imports para refletir a nova estrutura
from strategies.content_options.official_site_strategy import OfficialSiteStrategy
from strategies.content_options.social_media_strategy import SocialMediaStrategy
from strategies.content_options.where_to_watch_strategy import WhereToWatchStrategy
from strategies.content_options.news_strategy import NewsStrategy
from strategies.content_options.about_strategy import AboutStrategy
from strategies.exit_strategy import ExitStrategy

from telebot.types import ReplyKeyboardRemove

class OfferNextStepsStrategy(ResponseStrategy):

    STRATEGY_MAP = {
        "Site Oficial 🌍": OfficialSiteStrategy,
        "Redes Sociais 🌐": SocialMediaStrategy,
        "Onde assistir 📺": WhereToWatchStrategy,
        "Notícias e proximos jogos 📰": NewsStrategy,
        "Sobre a FURIA 🐆": AboutStrategy,
        "Sair": ExitStrategy,
    }

    def execute(self, message, bot, user_data):
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        options = list(self.STRATEGY_MAP.keys())
        markup.add(*[KeyboardButton(option) for option in options])

        bot.send_message(
            message.chat.id,
            "Escolha uma das opções abaixo para continuar:",
            reply_markup=markup
        )

    @staticmethod
    def handle_selection(message, bot, user_data):
        strategy_class = OfferNextStepsStrategy.STRATEGY_MAP.get(message.text)
        if strategy_class:
            strategy = strategy_class()
            strategy.execute(message, bot, user_data)
        else:
            bot.send_message(
                message.chat.id,
                "Desculpe, não entendi sua solicitação. Por favor, escolha uma opção válida."
            )
    
    @staticmethod
    def show_main_menu(bot, message, user_data):
        OfferNextStepsStrategy().execute(message, bot, user_data)