from unittest import TestCase
from models.river import River
from models.fish import Fish
from models.bear import Bear

class TestBear(TestCase):
    def setUp(self):
        self.nemo = Fish("Nemo")
        self.dory = Fish("Dory")
        self.marlin = Fish("Marlin")

        self.nile = River("Nile")

        self.baloo = Bear("Baloo")

        self.nile.add_fish(self.nemo)
        self.nile.add_fish(self.dory)

    def test_can_get_name(self):
        self.assertEqual(self.baloo.get_name(), "Baloo")

    def test_can_count_stomach_contents(self):
        self.assertEqual(self.baloo.count_stomach_contents(), 0)

    def test_can_add_fish_to_stomach(self):
        self.baloo.eat_fish(self.marlin)
        self.assertEqual(self.baloo.count_stomach_contents(), 1)

    def test_can_see_stomach_contents(self):
        self.baloo.eat_fish(self.marlin)
        self.assertEqual(self.baloo.get_stomach_contents(), [self.marlin])

    def test_can_be_sick(self):
        self.baloo.eat_fish(self.marlin)
        self.baloo.be_sick()
        self.assertEqual(self.baloo.count_stomach_contents(), 0)

    def test_bear_can_eat_fish_from_river(self):
        self.baloo.eat_fish(self.marlin)
        self.baloo.eat_fish_from_river(self.nemo, self.nile)
        self.assertEqual(self.baloo.get_stomach_contents(), [self.marlin, self.nemo])
        self.assertEqual(self.nile.count_fish(), 1)
