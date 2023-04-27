class Trade:
    def __init__(self, giver, receiver, give, receive):
        self.giver = giver
        self.receiver = receiver
        self.give = give
        self.receive = receive

    def execute(self):
        if self.giver.can_afford_cost(self.give) \
                and \
                self.receiver.can_afford_cost(self.receive):
            for res, qty in self.give.items():
                self.giver.resources[res] -= qty
                self.receiver.resources[res] += qty
            for res, qty in self.receive.items():
                self.giver.resources[res] += qty
                self.receiver.resources[res] -= qty
            return True
        return False
