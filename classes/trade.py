class Trade: # Not finished!
    def __init__(self, giver, receiver, give, receive):
        self.giver = giver
        self.receiver = receiver
        self.give = give
        self.receive = receive
        
    def execute(self):
        if all(self.giver.remove_resources(res, qty) for res, qty in self.give.items()) and \
           all(self.receiver.remove_resources(res, qty) for res, qty in self.receive.items()):
            for res, qty in self.give.items():
                self.receiver.add_resources(res, qty)
            for res, qty in self.receive.items():
                self.giver.add_resources(res, qty)
            return True
        return False