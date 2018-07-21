import random
import sys
import os


class Fish(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, newName):
        self.name = newName
        return self.name
