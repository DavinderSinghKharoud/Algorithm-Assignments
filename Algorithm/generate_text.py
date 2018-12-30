def generate_text(passenger_name, flight_number, gate_number):
   return '{}, go to gate {} for flight {}.'.format(passenger_name,gate_number,flight_number)

print(generate_text("Sam Roger", "AI221", 12))