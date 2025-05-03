from strategies.response_strategy import ResponseStrategy
from strategies.offer_next_steps_strategy import OfferNextStepsStrategy

class SkipPhoneStrategy(ResponseStrategy):
    def execute(self, message, bot, user_data):
        user_name = user_data[message.chat.id]['name']
        bot.send_message(
            message.chat.id,
            f"Sem problemas, {user_name}! Vamos começar!"
        )
        OfferNextStepsStrategy().execute(message, bot, user_data)