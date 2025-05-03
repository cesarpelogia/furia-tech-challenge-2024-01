from strategies.response_strategy import ResponseStrategy
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

class AskNameStrategy(ResponseStrategy):
    def execute(self, message, bot, user_data):

        user_data[message.chat.id] = {'name': message.text.strip()}
        user_name = user_data[message.chat.id]['name']
        print(f"Usuário {message.chat.id} informou o nome: {user_name}")
        
        phone_button = KeyboardButton('Enviar meu telefone', request_contact=True)
        skip_button = KeyboardButton("Pular")
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add(phone_button, skip_button)

        bot.send_message(
            message.chat.id,
            f"Muito prazer, {user_name}! Eu sou o Hermes! 🐺🔥\n\n"
            "Para personalizarmos seu atendimento, você pode me enviar seu número de telefone?\n\n"
            "Caso não deseje, é só clicar em 'Pular'.",
            reply_markup=markup
        )