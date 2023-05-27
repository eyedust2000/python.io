def get_season(country, month):
    seasons = {
        'Australia-Meteorological': {
            'Summer': ['December', 'January', 'February'],
            'Autumn': ['March', 'April', 'May'],
            'Winter': ['June', 'July', 'August'],
            'Spring': ['September', 'October', 'November']
        },
        'Australia-Noongar': {
            'Birak': ['December', 'January'],
            'Bunuru': ['February', 'March'],
            'Djeran': ['April', 'May'],
            'Makuru': ['June', 'July'],
            'Dijiba': ['August', 'September'],
            'Kambarang': ['October', 'November']
        },
        'Spain-Japan-Meteorological': {
            'Winter': ['December', 'January', 'February'],
            'Spring': ['March', 'April', 'May'],
            'Summer': ['June', 'July', 'August'],
            'Autumn': ['September', 'October', 'November']
        },
        'Mauritius-Meteorological': {
            'Summer': ['November', 'December', 'January', 'February', 'March', 'April'],
            'Autumn': ['May'],
            'Winter': ['June', 'July', 'August', 'September'],
            'Spring': ['October']
        },
        'Malaysia-SriLanka-Meteorological': {
            'Northeast Monsoon': ['December', 'January', 'February'],
            'Inter-monsoon': ['March', 'April'],
            'Southeast Monsoon': ['May', 'September'],
            'Inter Monsoon': ['October', 'November']
        }
    }

    for key, value in seasons.items():
        if country in key:
            for season, months in value.items():
                if month in months:
                    return season

    return 'Season not found for the given country and month.'

def write_to_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

def read_from_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        return content

# Get user input
country = input("Enter the country: ")
month = input("Enter the month: ")

# Find the season
season = get_season(country, month)

# Write the result to a file
file_name = "seasons.txt"
write_to_file(file_name, f"Country: {country}\nMonth: {month}\nSeason: {season}")

# Read the result from the file
result = read_from_file(file_name)
print("\nSeason information:\n" + result)
