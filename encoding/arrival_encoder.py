from pysat.examples.rc2 import RC2
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder
from pysat.card import CardEnc, EncType

class ArrivalEncoder(Encoder) :

    def encode(self, solver : RC2, flight_list : list[Flight], city_dict: tuple[dict[str, City]], var_count: int) -> None :
        for city in city_dict.keys():
            lits = [flight.get_id() for flight in flight_list if flight.get_arrival_city() == city]
            enc = CardEnc.equals(lits, bound=1, top_id=var_count, encoding=EncType.seqcounter)
            for clause in enc.clauses:
                solver.add_clause(clause)
            var_count += len(lits) - 1
        return var_count