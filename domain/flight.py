class Flight :

    def __init__(self, day, departure_city, arrival_city, departure_time, arrival_time, cost) -> None:
        self.id = 0 # FIXME : change this to use variable id
        self.day = day
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.cost = cost

    def __repr__(self) -> str:
        return f"{self.day} {self.departure_city} {self.arrival_city} {self.departure_time} {self.arrival_time} {self.cost}"