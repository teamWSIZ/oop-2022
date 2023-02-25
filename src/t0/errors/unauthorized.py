class SecurityUnauthorized(Exception):
    def __init__(self, message="pls use sudo"):
        self.message = message
        super().__init__(self.message)
