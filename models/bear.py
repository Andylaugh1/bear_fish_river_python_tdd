
class Bear(object):
    def __init__(self, name):
        self.name = name
        self.stomach = []

    def get_name(self):
        return self.name

    def count_stomach_contents(self):
        return len(self.stomach)

    def eat_fish(self, fish):
        self.stomach.append(fish)

    def get_stomach_contents(self):
        return self.stomach

    def be_sick(self):
        self.stomach.clear()

    def eat_fish_from_river(self, fish, river):
        self.eat_fish(fish)
        river.remove_fish(fish)
