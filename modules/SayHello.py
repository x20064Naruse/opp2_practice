class SayHello:
    def __init__(self, target="World"):
        self.target = target

    def say(self):
        print(f"Hello, {self.target}!!")