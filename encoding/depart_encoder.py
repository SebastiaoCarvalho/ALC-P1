from pysat.examples.rc2 import RC2
from domain.flight import Flight
from domain.city import City
from encoding.encoder import Encoder
from pysat.card import CardEnc, EncType

class DepartEncoder(Encoder) :

    def encode(self, solver : RC2, flight_list : list[Flight], city_dict: dict[str, City], var_count: int) -> int :
        #print("DepartEncoder")
        for city in city_dict.keys():
            lits = [flight.get_id() for flight in flight_list if flight.get_departure_city() == city]
            enc = CardEnc.equals(lits, bound=1, top_id=var_count, encoding=EncType.seqcounter)
            for clause in enc.clauses:
                solver.add_clause(clause)
                # string = ""
                # for lit in clause:
                        
                #     if lit < 0:
                #         string += "¬"
                #     if abs(lit) > len(flight_list):
                #         string += "aux" + str(abs(lit) - len(flight_list)) + " ∨ "
                #     else:
                #         string += str(flight_list[abs(lit) - 1]) + " ∨ "
                # if string != "":
                #     print(string[:-3])
            var_count = max(abs(literal) for clause in enc.clauses for literal in clause)
        return var_count