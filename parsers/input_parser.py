import sys
from domain.city import City
from domain.flight import Flight

from typing import Dict, List, Tuple

def parse_input() -> Tuple[Dict[str, City], List[Flight]]:
    city_map = {}
    flight_list = []
    n : int = int(readline())
    base_city = parse_base_city()
    city_map[base_city.code] = base_city
    for _ in range(n-1):
        city = parse_city()
        city_map[city.code] = city
    m : int = int(readline())
    for i in range(m):
        flight_list.append(parse_flight(i+1))
    return city_map, flight_list


def parse_base_city() -> City:
    city_info = readline()
    city_name, airport_code = city_info.split(' ')
    return City(city_name, airport_code, -1)

def parse_city() -> City:
    city_info = readline()
    city_name, airport_code, num_nights = city_info.split(' ')
    num_nights = int(num_nights)
    return City(city_name, airport_code, num_nights)

def readline() -> str:
    return sys.stdin.readline().strip()

def parse_flight(id) -> Flight:
    flight_info = readline()
    day, departure_city, arrival_city, departure_time, arrival_time, cost = flight_info.split()
    cost = int(cost)
    return Flight(id, day, departure_city, arrival_city, departure_time, arrival_time, cost)
