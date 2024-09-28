from pysat.examples.rc2 import RC2
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder
from pysat.card import CardEnc, EncType
from datetime import timedelta

class StayNDaysEncoder(Encoder) :

    def encode(self, solver : RC2, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int :
        print("StayNDaysEncoder")
        for city in city_dict.keys():
            if city_dict[city].is_base_city():
                continue
            arrivals = [flight for flight in flight_list if flight.get_arrival_city() == city]
            departs = [flight for flight in flight_list if flight.get_departure_city() == city]
            for arrival in arrivals:
                depart_date = arrival.get_day() + timedelta(days=city_dict[city].get_nights())
                print(arrival.get_id(), depart_date, arrival.get_day(), city_dict[city].get_nights())

        return var_count