from strategies.response_strategy import ResponseStrategy

class StrategyContext:
    def __init__(self, strategy=None):
        if strategy and not isinstance(strategy, ResponseStrategy):
            raise TypeError("A estratégia deve ser uma subclasse de ResponseStrategy")
        self._strategy = strategy
        self._strategies = {} 

    def register_strategy(self, name, strategy):
        if not isinstance(strategy, ResponseStrategy):
            raise TypeError("A estratégia deve ser uma subclasse de ResponseStrategy")
        self._strategies[name] = strategy

    def set_strategy(self, strategy):
        if not isinstance(strategy, ResponseStrategy):
            raise TypeError("A estratégia deve ser uma subclasse de ResponseStrategy")
        self._strategy = strategy

    def execute_strategy(self, name, *args, **kwargs):
        if name not in self._strategies:
            raise ValueError(f"Estratégia '{name}' não registrada")
        strategy = self._strategies[name]
        return strategy.execute(*args, **kwargs)