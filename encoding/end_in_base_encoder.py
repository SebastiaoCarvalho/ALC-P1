from pysat.examples.rc2 import RC2
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder

class EndInBaseEncoder(Encoder):

    def encode(self, solver : RC2, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int:
        #print("EndInBaseEncoder")
        for city in city_dict.keys():
            if not city_dict[city].is_base_city():
                continue
            arrive_lits = [flight.get_id() for flight in flight_list if flight.get_arrival_city() == city]
            total_lits  = [flight.get_id() for flight in flight_list if flight.get_arrival_city() != city]
            for arrive_lit in arrive_lits:
                for lit in total_lits:
                    if flight_list[arrive_lit - 1].get_day() <= flight_list[lit - 1].get_day():
                        #print([-arrive_lit, -lit])
                        #print(f"add clause ¬{flight_list[arrive_lit - 1]} ∨ ¬{flight_list[lit - 1]}")
                        solver.add_clause([-arrive_lit, -lit])
        return var_count