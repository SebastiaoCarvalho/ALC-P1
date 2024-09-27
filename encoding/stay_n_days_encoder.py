from pysat.examples.rc2 import RC2
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder
from pysat.card import CardEnc, EncType
from datetime import timedelta

class StayNDaysEncoder(Encoder) :

    def encode(self, solver : RC2, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int :
        for city in city_dict.keys():
            if city_dict[city].is_base_city():
                continue
            arrivals = [flight for flight in flight_list if flight.get_arrival_city() == city]
            departs = [flight for flight in flight_list if flight.get_departure_city() == city]
            for arrival in arrivals:
                depart_date = arrival.get_day() + timedelta(days=city_dict[city].get_nights())
                disjunction = []
                for depart in departs:
                    if depart_date != depart.get_day():
                        solver.add_clause([-arrival.get_id(), -depart.get_id()]) # cant only fly to other city after exactly n nights
                    else :
                        disjunction.append(depart.get_id())
                if len(disjunction) > 0:
                    enc = CardEnc.equals(disjunction, bound=1, top_id=var_count, encoding=EncType.seqcounter) # needs to fly with exactly one flight
                    for clause in enc.clauses:
                        solver.add_clause(clause)
                    var_count += len(disjunction) - 1
                    
        return var_count