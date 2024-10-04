from datetime import timedelta
from pysat.examples.rc2 import RC2
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder

class InvalidFlightsEncoder(Encoder):

    def encode(self, solver : RC2, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int:
        # Group flights by arrival city for easy lookup
        flights_by_arrival_city = {}
        for flight in flight_list:
            arrival_city = flight.get_arrival_city()
            if arrival_city not in flights_by_arrival_city:
                flights_by_arrival_city[arrival_city] = []
            flights_by_arrival_city[arrival_city].append(flight)

        # Sort flights in each arrival city group by day
        for flights in flights_by_arrival_city.values():
            flights.sort(key=lambda f: f.get_day())
        
        # Iterate over each flight to check validity based on stay duration
        for flight in flight_list:
            departure_city = flight.get_departure_city()
            
            if city_dict[departure_city].is_base_city():
                continue

            # Get the required stay duration (N days) for the departure city
            required_stay = city_dict[departure_city].get_nights()
            required_arrival_day = flight.get_day() - timedelta(days=required_stay)

            # Check if there's a flight arriving N days before the current departure
            valid = False
            if departure_city in flights_by_arrival_city:
                for arrival_flight in flights_by_arrival_city[departure_city]:
                    if arrival_flight.get_day() == required_arrival_day:
                        valid = True
                        break

            # If no valid arrival flight exists, discard the current departure flight
            if not valid:
                solver.add_clause([-flight.get_id()])  # Exclude this flight from possible solutions