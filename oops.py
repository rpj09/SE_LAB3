class FlightDatabase:
    def __init__(self):
        self.flights = [
            {"Flight ID": "AI161E90", "From": "BLR", "To": "BOM", "Price": 5600},
            {"Flight ID": "BR161F91", "From": "BOM", "To": "BBI", "Price": 6750},
            {"Flight ID": "AI161F99", "From": "BBI", "To": "BLR", "Price": 8210},
            {"Flight ID": "VS171E20", "From": "JLR", "To": "BBI", "Price": 5500},
            {"Flight ID": "AS171G30", "From": "HYD", "To": "JLR", "Price": 4400},
            {"Flight ID": "AI131F49", "From": "HYD", "To": "BOM", "Price": 3499}
        ]

        self.city_names = {
            "BLR": "Bengaluru",
            "BOM": "Mumbai",
            "BBI": "Bhubaneswar",
            "HYD": "Hyderabad",
            "JLR": "Jabalpur"
        }

    def search_flights_by_city(self, city_code):
        city_flights = []

        for flight in self.flights:
            if flight["From"] == city_code or flight["To"] == city_code:
                city_flights.append(flight)

        return city_flights

    def search_flights_from_city(self, from_city_code):
        flights_from_city = []

        for flight in self.flights:
            if flight["From"] == from_city_code:
                flights_from_city.append(flight)

        return flights_from_city

    def search_flights_between_cities(self, from_city_code, to_city_code):
        flights_between_cities = []

        for flight in self.flights:
            if flight["From"] == from_city_code and flight["To"] == to_city_code:
                flights_between_cities.append(flight)

        return flights_between_cities

    def get_city_name(self, city_code):
        return self.city_names.get(city_code, "Unknown city")


def main():
    database = FlightDatabase()

    print("Flight Search Options:")
    print("1. Flights departing from a city")
    print("2. Flights arriving at a city")
    print("3. Flights between two cities")
    print("4. Exit")

    while True:
        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            from_city_code = input("Enter the departure city code (e.g., BOM): ")
            flights = database.search_flights_from_city(from_city_code)
            print(f"Flights from {database.get_city_name(from_city_code)}:")
            for flight in flights:
                print(f"Flight ID: {flight['Flight ID']}, To: {database.get_city_name(flight['To'])}, Price: {flight['Price']}")
        elif choice == 2:
            to_city_code = input("Enter the arrival city code (e.g., BBI): ")
            flights = database.search_flights_by_city(to_city_code)
            print(f"Flights arriving at {database.get_city_name(to_city_code)}:")
            for flight in flights:
                print(f"Flight ID: {flight['Flight ID']}, From: {database.get_city_name(flight['From'])}, Price: {flight['Price']}")
        elif choice == 3:
            from_city_code = input("Enter the departure city code (e.g., BOM): ")
            to_city_code = input("Enter the arrival city code (e.g., BBI): ")
            flights = database.search_flights_between_cities(from_city_code, to_city_code)
            print(f"Flights from {database.get_city_name(from_city_code)} to {database.get_city_name(to_city_code)}:")
            for flight in flights:
                print(f"Flight ID: {flight['Flight ID']}, Price: {flight['Price']}")

        elif choice == 4:
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
