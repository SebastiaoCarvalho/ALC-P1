from pysat.examples.rc2 import RC2
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder

class SoftEncoder(Encoder):

    def encode(self, solver : RC2, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int :
        max_cost = (max(flight.get_cost() for flight in flight_list))
        for flight in flight_list:
            print([flight.get_id()], max_cost - flight.get_cost() + 1)
            solver.add_clause([flight.get_id()], weight= (max_cost - flight.get_cost() +1))