from telebot import types
from dotenv import load_dotenv
import os
import telebot
from datetime import datetime

# Carregar as variáveis de ambiente
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

# Dicionário para armazenar o nome dos usuários temporariamente
user_data = {}

# Boas-vindas /start
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
        f"{greeting} Seja bem-vindo ao canal da FURIA! 🐺🔥\n\nQual é o seu nome?"
    )
    # Aguardar o nome do usuário
    bot.register_next_step_handler(message, ask_name)

# Armazenar nome e oferecer opções
def ask_name(message):
    user_name = message.text.strip()
    user_data[message.chat.id] = user_name  # Salva o nome pelo chat_id

    bot.send_message(
        message.chat.id,
        f"Prazer, {user_name}! 😎 Vamos lá!",
    )
    offer_options(message)

# Oferecer opções via botões
def offer_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Notícias 📰')
    btn2 = types.KeyboardButton('Instagram 📸')
    btn3 = types.KeyboardButton('YouTube ▶️')
    btn4 = types.KeyboardButton('Próximas Partidas 📅')
    btn5 = types.KeyboardButton('Twitch 🎥')
    btn6 = types.KeyboardButton('Outros ❓')

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5, btn6)

    bot.send_message(message.chat.id, "Escolha uma opção:", reply_markup=markup)

# Tratar escolha do usuário
@bot.message_handler(func=lambda message: True)
def handle_user_choice(message):
    user_name = user_data.get(message.chat.id, "FURIOSO")  # Se não tiver nome salvo, usa 'FURIOSO'

    user_choice = message.text

    if user_choice == 'Notícias 📰':
        bot.reply_to(message, f"{user_name}, confira as notícias da FURIA aqui: https://draft5.gg/equipe/330-FURIA")
    elif user_choice == 'Instagram 📸':
        bot.reply_to(message, f"{user_name}, nos siga no Instagram! 📸 https://www.instagram.com/furiagg")
    elif user_choice == 'YouTube ▶️':
        bot.reply_to(message, f"{user_name}, confira nosso canal no YouTube: https://www.youtube.com/@FURIAggCS")
    elif user_choice == 'Próximas Partidas 📅':
        bot.reply_to(message, f"{user_name}, veja as próximas partidas aqui: https://draft5.gg/proximas-partidas")
    elif user_choice == 'Twitch 🎥':
        bot.reply_to(message, f"{user_name}, acompanhe nossas lives na Twitch: https://www.twitch.tv/furiatv?lang=pt-br")
    elif user_choice == 'Outros ❓':
        bot.reply_to(message, f"{user_name}, me diga do que você precisa que eu vou tentar te ajudar! 💬")
    else:
        bot.reply_to(message, f"Desculpe, {user_name}, não entendi. Escolha uma das opções acima! 👆")

# Rodar o bot
if __name__ == '__main__':
    bot.polling()
