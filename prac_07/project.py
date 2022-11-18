import datetime
class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"\n{self.name}\t{self.start_date}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"

    def __format__(self, format_spec):
        if not format_spec:
            return str(self)
        elif format_spec == "d":
            date = self.start_date.strftime("%x")
            return f"{self.name}, Started on {date}, Priority of {str(self.priority)}, Estimate cost of " \
                   f"${self.cost_estimate:.2f}, {str(self.completion_percentage)}%"

    def __lt__(self, other):
        return self.priority < other.priority
