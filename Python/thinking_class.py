class name:
    def thinking(self):
        print("I'm thinking...")
    the_name = "Python 3"

class brain(name):
    def think(self):
        super().thinking()
        print(f"I'm done thinking. {super().the_name}")

brain().think()
