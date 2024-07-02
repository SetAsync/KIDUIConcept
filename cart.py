class cart:
    def __init__(self):
        pass
    
    @property
    def status(self):
        if not self._status:
            self.getStatus()
        return self._status