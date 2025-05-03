from abc import ABC, abstractmethod

class ResponseStrategy(ABC):
    @abstractmethod
    def execute(self, message, bot, user_data):
        pass