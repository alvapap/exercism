import random
import string

class Robot:
    unique_names = set()
    
    # create a name cosisting of 2 uppercase letters and 3 digits
    def create_name(self):
        name = ""
        for letters in range(2):
            name += random.choice(string.ascii_uppercase)
        for numbers in range(3):
            name += str(random.randint(0,9))
        return name
    
    def __init__(self):
        self.name = self._get_name()

    def reset(self):
        old_name = self.name
        self.name = self._get_name()
        self.unique_names.remove(old_name)

    # get a unique name for each robot
    def _get_name(self):
        name = self.create_name()
        while name in self.unique_names:
            name = self.create_name()
        self.unique_names.add(name)
        return name


    