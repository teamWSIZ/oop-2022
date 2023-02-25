class SecurityBadRequest(Exception):
    def __init__(self, message="BadRequest"):
        self.message = message
        super().__init__(self.message)
