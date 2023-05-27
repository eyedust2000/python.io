def compare_temperature(city, temperature):
    cities = {
        'perth': {
            'morning': 18.2,
            'afternoon': 23
        },
        'adelaide': {
            'morning': 16.5,
            'afternoon': 21
        }
    }

    if city.lower() in cities:
        city_temps = cities[city.lower()]
        morning_temp = city_temps['morning']
        afternoon_temp = city_temps['afternoon']
        average_temp = (morning_temp + afternoon_temp) / 2

        diff = temperature - average_temp

        if diff > 5:
            message = "The temperature is significantly above the average."
        elif diff < -5:
            message = "The temperature is significantly below the average."
        else:
            message = ""

        if temperature > average_temp:
            return f"The temperature in {city} is above the average ({average_temp}°C). {message}"
        elif temperature < average_temp:
            return f"The temperature in {city} is below the average ({average_temp}°C). {message}"
        else:
            return f"The temperature in {city} is equal to the average ({average_temp}°C)."
    else:
        return "City not found."

# Example usage
city = input("Enter the city (Perth or Adelaide): ")
temperature = float(input("Enter the temperature reading: "))

result = compare_temperature(city, temperature)
print(result)
