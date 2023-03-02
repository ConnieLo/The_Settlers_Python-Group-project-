class Bank:
    def __init__(self, resources=None):
        self.resources = resources or {
            "brick": 19,
            "lumber": 19,
            "wool": 19,
            "grain": 19,
            "ore": 19
        }

    def add_resources(self, resource_type, amount):
        # Adds a certain amount of a resource to the bank
        if resource_type in self.resources:
            self.resources[resource_type] += amount

    def remove_resources(self, resource_type, amount):
        # Removes a certain amount of a resource from the bank
        if resource_type in self.resources:
            self.resources[resource_type] -= amount

    def has_resources(self, resource_dict):
        # Checks if the bank has enough resources to fulfill a resource dictionary
        for resource_type, amount in resource_dict.items():
            if amount > self.deck.count_cards(resource_type):
                return False
        return True

    def get_resources(self):
        # Returns the dictionary of resources held by the bank
        resource_dict = {}
        for card_type in self.deck.get_card_types():
            resource_dict[card_type] = self.deck.count_cards(card_type)
        return resource_dict