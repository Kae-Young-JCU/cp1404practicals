class Band:

    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def __str__(self):
        text = []
        for musician in self.musicians:
            text.append(musician.__str__())
        text = ", ".join(text)
        return f"{self.name} ({text})"

    def play(self):
        text = []
        for musician in self.musicians:
            text.append(musician.play())
        text = "\n".join(text)
        return text
