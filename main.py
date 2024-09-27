from parsers.input_parser import parse_input
from pysat.examples.rc2 import RC2
from pysat.formula import WCNF
from encoding.depart_encoder import DepartEncoder
from encoding.arrival_encoder import ArrivalEncoder  
from encoding.stay_n_days_encoder import StayNDaysEncoder
from encoding.arrive_after_depart_encoder import ArriveAfterDepartEncoder
from encoding.end_in_base_encoder import EndInBaseEncoder
from encoding.start_in_base_city import StartInBaseCity
from encoding.soft_encoder import SoftEncoder


city_map, flight_list = parse_input()

solver = RC2(WCNF())

encoder = DepartEncoder()
var_counter = encoder.encode(solver, flight_list, city_map, len(flight_list))

encoder = ArrivalEncoder()
var_counter = encoder.encode(solver, flight_list, city_map, var_counter)

#encoder = StayNDaysEncoder()
#var_counter = encoder.encode(solver, flight_list, city_map, var_counter)

encoder = ArriveAfterDepartEncoder()
var_counter = encoder.encode(solver, flight_list, city_map, var_counter)

encoder = EndInBaseEncoder()
var_counter = encoder.encode(solver, flight_list, city_map, var_counter)

encoder = StartInBaseCity()
var_counter = encoder.encode(solver, flight_list, city_map, var_counter)

encoder = SoftEncoder()
var_counter = encoder.encode(solver, flight_list, city_map, var_counter)

solution = solver.compute()
if solution != None:
    for i in range(0, len(flight_list)):
        if solution[i] > 0:
            print(flight_list[i - 1])
else:
    print("No solution found")
