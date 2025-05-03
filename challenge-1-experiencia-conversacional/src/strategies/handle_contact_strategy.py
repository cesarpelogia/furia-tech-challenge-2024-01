from strategies.response_strategy import ResponseStrategy
from strategies.offer_next_steps_strategy import OfferNextStepsStrategy

class HandleContactStrategy(ResponseStrategy):
    def execute(self, message, bot, user_data):
        phone = message.contact.phone_number
        user_data[message.chat.id]['phone'] = phone
        bot.send_message(
            message.chat.id,
            f"Obrigado! Recebi seu número de telefone: {phone}. Agora, vamos continuar com o atendimento."
        )
        OfferNextStepsStrategy().execute(message, bot, user_data)