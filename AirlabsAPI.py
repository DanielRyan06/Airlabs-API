import requests

API_KEY = str(input("API KEY:"))
FLIGHT = str(input("FLIGHT NUMBER:"))
URL = ("https://airlabs.co/api/v9/flight?flight_iata="+ FLIGHT + "&api_key="+API_KEY)

response = requests.get(URL)
data = response.json()

if "error" in data:
    print(data["error"]["message"])
    exit()

aircraft = data["response"]["aircraft_icao"]
manufacture = data["response"]["manufacturer"]
registration = data["response"]["reg_number"]
flag = data["response"]["flag"]
latitude = data["response"]["lat"]
longitude = data["response"]["lng"]
altitude = data["response"]["alt"]
direction = data["response"]["dir"]
speed = data["response"]["speed"]
squawk = data["response"]["squawk"]
flight_num = data["response"]["flight_number"]
flight_icao = data["response"]["flight_icao"]
flight_iata = data["response"]["flight_iata"]
depart_icao = data["response"]["dep_icao"]
depart_iata = data["response"]["dep_iata"]
arrive_icao = data["response"]["arr_icao"]
arrive_iata = data["response"]["arr_iata"]
airline_iata = data["response"]["airline_iata"]
status = data["response"]["status"]
depart_terminal = data["response"]["dep_terminal"]
depart_gate = data["response"]["dep_gate"]
dep_time_utc = data["response"]["dep_time_utc"]
arrival_terminal = data["response"]["arr_terminal"]
arrival_gate = data["response"]["arr_gate"]
arrival_baggage = data["response"]["arr_baggage"]
arr_time_utc = data["response"]["arr_time_utc"]
duration = data["response"]["duration"]
delayed = data["response"]["delayed"]

print("Status:", status)
print("Aircraft :", aircraft)
print("Manufacturer :", manufacture)
print("Registration :", registration)
print("Flag:", flag)
print("Latitude:", latitude)
print("Longitude:", longitude)
print("Altitude:", altitude)
print("Direction:", direction)
print("Speed:", speed)
print("Squawk:", squawk)
print("Flight Number:", airline_iata + flight_num)
print("Depart ICAO:", depart_icao)
print("Depart IATA:", depart_iata)
print("Depart Terminal:", depart_terminal)
print("Depart Gate:", depart_gate)
print("Depart Time UTC:", dep_time_utc)
print("Arrive ICAO:", arrive_icao)
print("Arrive IATA:", arrive_iata)
print("Arrive Terminal:", arrival_terminal)
print("Arrive Gate:", arrival_gate)
print("Arrive Baggage", arrival_baggage)
print("Arrive Time UTC:", arr_time_utc)
print("Duration:", duration)
print("Delayed:", delayed)
