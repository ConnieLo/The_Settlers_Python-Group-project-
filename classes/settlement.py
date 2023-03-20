import player

class Settlement():

    def __init__(self, owner, potential_resources):
        self.owner = owner  #player instance
        self.is_city = False #boolean
        self.potential_resources = potential_resources #dictionary of resource and activation number

    def grant_resources(self, resource):
        #generates resources for the owner of the settlement
        if self.is_city:
            for res in self.potential_resources:
                self.owner.add_resource(res, 2)
        else:
            for res in self.potential_resources:
                self.owner.add_resource(res, 1)