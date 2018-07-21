class River(object):

    def __init__(self, name):
        self.name = name
        self.fish = []

    def get_name(self):
        return self.name

    def count_fish(self):
        return len(self.fish)

    def add_fish(self, fish):
        self.fish.append(fish)

    def remove_fish(self, fish):
        self.fish.remove(fish)

