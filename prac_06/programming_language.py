class ProgrammingLanguage:
    def __init__(self, language, typing, reflection, year):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """returns true if type is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.language}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"
