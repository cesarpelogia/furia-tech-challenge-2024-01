from telebot.types import ReplyKeyboardRemove


class ExitStrategy:
    def execute(self, message, bot, user_data):
        bot.send_message(
            message.chat.id,
            "Obrigado por interagir com o canal da FURIA! Até a próxima! 🐺🔥",
            reply_markup=ReplyKeyboardRemove()
        )
        bot.send_message(
            message.chat.id,
            "Se precisar de algo mais, é só me enviar uma mensagem! 😊"
        )
        from strategies.offer_next_steps_strategy import OfferNextStepsStrategy
        bot.register_next_step_handler(message, lambda msg: OfferNextStepsStrategy.show_main_menu(bot, msg, user_data))