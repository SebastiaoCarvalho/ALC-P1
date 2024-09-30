from pysat.examples.rc2 import RC2
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder
from pysat.card import CardEnc, EncType

class StartInBaseCity(Encoder):

    def encode(self, solver : RC2, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int:
        #print("StartInBaseCity")
        for city in city_dict.keys():
            if not city_dict[city].is_base_city():
                continue
            total_lits = [flight.get_id() for flight in flight_list if flight.get_departure_city() != city]
            depart_lits = [flight.get_id() for flight in flight_list if flight.get_departure_city() == city]
            for depart_lit in depart_lits:
                for lit in total_lits:
                    if flight_list[lit - 1].get_day() <= flight_list[depart_lit - 1].get_day():
                        #print([-lit, -depart_lit])
                        #print(f"add clause ¬{flight_list[lit - 1]} ∨ ¬{flight_list[depart_lit - 1]}")
                        solver.add_clause([-lit, -depart_lit])
        return var_count