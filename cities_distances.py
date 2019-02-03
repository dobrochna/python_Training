#  Program finds distances between available cities.
import math


cities = {'Warszawa': ((52, 13, 54.925, 'N'), (21, 0, 24.215, 'E')),
          'Krakow': ((50, 3, 43.011, 'N'), (19, 56, 12.683, 'E')),
          'Lizbona': ((38, 42, 27.903, 'N'), (9, 8, 11.731, 'W')),
          'Barcelona': ((41, 22, 58.418, 'N'), (2, 10, 38.756, 'E')),
          'Sydney': ((33, 51, 17.337, 'S'), (151, 12, 59.234, 'E')),
          'Lima': ((12, 3, 43.583, 'S'), (77, 2, 11.492, 'W'))}


def print_cities():
    for name in cities.keys():
        print(name)


def calculate_latitude(coordinates):
    latitude = coordinates[2]/3600 + coordinates[1]/60 + coordinates[0]
    if coordinates[3] == 'S':
        latitude = -latitude
    return latitude


def calculate_longtitude(coordinates):
    longtitude = coordinates[2]/3600 + coordinates[1]/60 + coordinates[0]
    if coordinates[3] == 'E':
        longtitude = -longtitude
    return longtitude


def calculate_distance(city_1, city_2):
    latitude_city_1 = calculate_latitude(cities[city_1][0])
    longtitude_city_1 = calculate_longtitude(cities[city_1][1])
    latitude_city_2 = calculate_latitude(cities[city_2][0])
    longtitude_city_2 = calculate_longtitude(cities[city_2][1])

    cities_distance = math.sqrt((latitude_city_2-latitude_city_1)**2 + (math.cos(latitude_city_1*math.pi/180) *
                                (longtitude_city_2-longtitude_city_1))**2) * (40075.704/360)

    return cities_distance


if __name__ == '__main__':
    while True:
        while True:
            print('Available cities: ')
            print_cities()
            city_one = input('Pass name for first city: ')
            city_two = input('Pass name for second city: ')

            try:
                distance = calculate_distance(city_one, city_two)
                break

            except:
                print('Wrong city name, try again!')

        print('Distance between %s and %s is: %ikm.' % (city_one, city_two, distance))
        decision_1 = input("Do you want to calculate distance in different unit? Pass 'y' or 'n': ")
        if decision_1.lower() == 'y':
            dif_unit = input("Which unit? Pass 'm' for miles and 'y' for yards.")
            if dif_unit.lower() == 'm':
                distance = distance/1.61
                print('Distance in miles is: %i.' % distance)
            elif dif_unit.lower() == 'y':
                distance = distance/0.91
                print('Distance in yards is: %i.' % distance)
            else:
                print('You passed wrong unit symbol!')

        decision_2 = input("Do you want to calculate another distance? Pass 'y' or 'n': ")
        if decision_2.lower() == 'y':
            continue
        elif decision_2.lower() == 'n':
            break
        else:
            print('Wrong decision format, so were going again!')
