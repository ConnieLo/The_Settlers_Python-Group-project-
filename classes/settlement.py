class Settlement():

    def __init__(self, owner, potential_resources):
        self.owner = owner  #player instance
        self.potential_resources = potential_resources #dictionary of resource and activation number

    def grant_resources(self, resource):
        for res in self.potential_resources:
            if res == resource:
                self.owner.add_resources