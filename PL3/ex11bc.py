# The following website contains weather information for a given location (website).
# b. Implement a “.py” script that allows a given user to obtain the weather forecast for a
# given day, using the information from the previously stored “. json” file.
# c. As an optional exercise, parse the degrees from °F to ºC and windspeed from mph to
# km/h. Additionally, make the first script (a.) configurable to fetch weather data from
# other locations. Similarly, adjust the second script (b.) so that users can query for
# weather data of all the supported locations

import json
import sys

def load_weather_data(location):
    with open(location + '.json', 'r') as file:
        return json.load(file)
    
def main(location, day):
    data = load_weather_data(location)
    if day in data:
        print(data[day])
    else:
        print("Day not found")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit("usage: " + sys.argv[0] + " <location> <day>")
    location = sys.argv[1]
    day = sys.argv[2]
    main(location, day)
