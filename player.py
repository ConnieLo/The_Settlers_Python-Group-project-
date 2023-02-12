class player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.score = 0
        self.resources = {"wood": 0, "brick": 0, "sheep": 0, "wheat": 0, "ore": 0}

    def increase_score(self, points):
        self.score += points

    def add_resources(self, resource, quantity):
        self.resources[resource] += quantity

    def remove_resources(self, resource, quantity):
        if self.resources[resource] >= quantity:
            self.resources[resource] -= quantity
            return True
        else:
            return False

    def display(self, surface, font, x, y):
        text = font.render(f"{self.name}'s Score: {self.score}", True, self.color)
        text2 = font.render(f"{self.name}'s Resources: {self.resources}", True, self.color)
        surface.blit(text, (x, y))
        surface.blit(text2, (x, y+50))