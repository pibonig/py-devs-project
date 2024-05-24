class InvalidCommandParamsException(Exception):
    def __init__(self, cls):
        super().__init__(f"Invalid command parameters. Example: {cls.name} {cls.signature}")
