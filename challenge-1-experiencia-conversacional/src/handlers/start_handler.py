from datetime import datetime

from telebot.types import ReplyKeyboardRemove

from bot.bot_instance import bot
from bot.user_context import user_data

from strategies.context import StrategyContext
from strategies.handle_contact_strategy import HandleContactStrategy
from strategies.skip_phone_strategy import SkipPhoneStrategy
from strategies.ask_name_strategy import AskNameStrategy
from strategies.offer_next_steps_strategy import OfferNextStepsStrategy
from strategies.exit_strategy import ExitStrategy

from strategies.content_options.official_site_strategy import OfficialSiteStrategy
from strategies.content_options.social_media_strategy import SocialMediaStrategy
from strategies.content_options.where_to_watch_strategy import WhereToWatchStrategy
from strategies.content_options.news_strategy import NewsStrategy
from strategies.content_options.about_strategy import AboutStrategy

strategy_context = StrategyContext()
strategy_context.register_strategy("ask_name", AskNameStrategy())
strategy_context.register_strategy("contact", HandleContactStrategy())
strategy_context.register_strategy("skip", SkipPhoneStrategy())
strategy_context.register_strategy("offer_next_steps", OfferNextStepsStrategy())


@bot.message_handler(commands=['start'])
def send_welcome(message):
    now = datetime.now()
    hour = now.hour

    if 5 <= hour < 12:
        greeting = "Bom dia! ☀️"
    elif 12 <= hour < 18:
        greeting = "Boa tarde! 🌤️"
    else:
        greeting = "Boa noite! 🌙"

    bot.send_message(
        message.chat.id,
        f"{greeting} Seja bem-vindo ao canal da FURIA! 🐺🔥\n\nQual é o seu nome?", reply_markup=ReplyKeyboardRemove()
    )
    bot.register_next_step_handler(message, lambda msg: strategy_context.execute_strategy("ask_name", msg, bot, user_data))

@bot.message_handler(content_types=['offer_next_steps'])
def offer_next_steps(message):
    strategy_context.execute_strategy("offer_next_steps", message, bot, user_data)
    
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    strategy_context.execute_strategy("contact", message, bot, user_data)
    
@bot.message_handler(func=lambda message: message.text == "Pular")
def skip_phone(message):
    strategy_context.execute_strategy("skip", message, bot, user_data)

@bot.message_handler(func=lambda message: message.text == "Site Oficial 🌍")
def handle_official_site(message):
    OfficialSiteStrategy().execute(message, bot, user_data)

@bot.message_handler(func=lambda message: message.text == "Redes Sociais 🌐")
def handle_social_media(message):
    SocialMediaStrategy().execute(message, bot, user_data, disable_web_page_preview=True)

@bot.message_handler(func=lambda message: message.text == "Onde assistir 📺")
def handle_where_to_watch(message):
    WhereToWatchStrategy().execute(message, bot, user_data, disable_web_page_preview=True)

@bot.message_handler(func=lambda message: message.text == "Notícias e proximos jogos 📰")
def handle_news(message):
    NewsStrategy().execute(message, bot, user_data)

@bot.message_handler(func=lambda message: message.text == "Sobre a FURIA 🐆")
def handle_about(message):
    AboutStrategy().execute(message, bot, user_data)

@bot.message_handler(func=lambda message: message.text == "Voltar 🔙")
def handle_back(message):
    OfferNextStepsStrategy().execute(message, bot, user_data)

@bot.message_handler(func=lambda message: message.text == "Sair")
def handle_exit(message):
    ExitStrategy().execute(message, bot, user_data)