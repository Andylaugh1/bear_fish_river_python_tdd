from unittest import TestCase
from models.river import River
from models.fish import Fish

class TestRiver(TestCase):
    def setUp(self):
        self.nile = River("Nile")
        self.nemo = Fish("Nemo")
        self.dory = Fish("Dory")

    def test_can_get_name(self):
        self.assertEqual(self.nile.get_name(), "Nile")

    def test_can_add_fish(self):
        self.nile.add_fish(self.nemo)
        self.assertEqual(self.nile.count_fish(), 1)

    def test_can_remove_fish(self):
        self.nile.add_fish(self.nemo)
        self.nile.remove_fish(self.nemo)
        self.assertEqual(self.nile.count_fish(), 0)

    def test_can_remove_all_fish(self):
        self.nile.add_fish(self.nemo)
        self.nile.add_fish(self.dory)
        self.nile.remove_all_fish()
        self.assertEqual(self.nile.count_fish(), 0)