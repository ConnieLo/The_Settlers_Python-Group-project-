import player

class Settlement():

    def __init__(self, owner, potential_resources):
        self.owner = owner  #player instance
        self.is_city = False #dictionary of resource and activation number
        self.potential_resources = potential_resources

    def grant_resources(self, resource):
        if self.is_city:
            for res in self.potential_resources:
                self.owner.add_resource(res, 2)
        else:
            for res in self.potential_resources:
                self.owner.add_resource(res, 1)