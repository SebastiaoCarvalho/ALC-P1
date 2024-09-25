from parsers.input_parser import parse_input
from pysat.examples.rc2 import RC2
from pysat.formula import WCNF
from encoding.depart_encoder import DepartEncoder
from encoding.arrival_encoder import ArrivalEncoder  


city_map, flight_list = parse_input()
print(city_map)
print(flight_list)

solver = RC2(WCNF())

encoder = DepartEncoder()
var_counter = encoder.encode(solver, flight_list, city_map, len(flight_list))

encoder = ArrivalEncoder()
var_counter = encoder.encode(solver, flight_list, city_map, var_counter)