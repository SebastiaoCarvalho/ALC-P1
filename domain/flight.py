from datetime import date

class Flight :

    def __init__(self, id, day_str, departure_city, arrival_city, departure_time, arrival_time, cost) -> None:
        self.id = id 
        day, month = day_str.split('/')
        self.day = date(2024, int(month), int(day))
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.cost = cost
    
    def get_id(self) -> int:
        return self.id
    
    def get_day(self) -> date:
        return self.day
    
    def get_departure_city(self) -> str:
        return self.departure_city
    
    def get_arrival_city(self) -> str:
        return self.arrival_city    

    def __repr__(self) -> str:
        return f"{self.id} {self.day} {self.departure_city} {self.arrival_city} {self.departure_time} {self.arrival_time} {self.cost}"