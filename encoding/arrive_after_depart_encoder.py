from pysat.examples.rc2 import RC2
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder
from pysat.card import CardEnc, EncType

class ArriveAfterDepartEncoder(Encoder) :

    def encode(self, solver : RC2, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int :
        for city in city_dict.keys():
            if city_dict[city].is_base_city():
                continue
            depart_lits = [flight.get_id() for flight in flight_list if flight.get_departure_city() == city]
            arrive_lits = [flight.get_id() for flight in flight_list if flight.get_arrival_city() == city]
            for depart_lit in depart_lits:
                for arrive_lit in arrive_lits:
                    solver.add_clause([-depart_lit, -arrive_lit]) # if departed from city, then cannot arrive again at city
        return var_count