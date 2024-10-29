class Basket:
    def __init__(self, name):
        self.name = name
        self.contents = []

    def add_orange(self, orange):
        self.contents.append(orange)

    def list_contents(self):
        return [f"{orange.variety}, {orange.weight}kg, expires on {orange.expiry_date}" for orange in self.contents]
