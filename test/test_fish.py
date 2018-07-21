from unittest import TestCase
from models.fish import Fish



class TestFish(TestCase):
    def setUp(self):
        self.nemo = Fish("Nemo")
        # self.nemo.name = "nemo"


    def test_can_get_name(self):
        self.assertEqual("Nemo", self.nemo.get_name())

    def test_can_set_name(self):
        self.assertEqual("John", self.nemo.set_name("John"))

