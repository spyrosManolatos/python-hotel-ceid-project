import csv
import math
from functools import *


def findResortHotels():
    with open('hotel_booking.csv', mode='r') as csvfile:
        csvReader = csv.DictReader(csvfile)
        resortHotels = list(filter(lambda row: row['hotel'] == 'Resort Hotel', csvReader))
    return len(resortHotels)


def findCityHotels():
    with open('hotel_booking.csv', mode='r') as csvfile:
        csvReader = csv.DictReader(csvfile)
        cityHotels = list(filter(lambda row: row['hotel'] == 'City Hotel', csvReader))
    return len(cityHotels)


def findResortHotelsWithNoCancels():
    with open('hotel_booking.csv', mode='r') as csvfile:
        csvReader = csv.DictReader(csvfile)
        resortHotels = list(filter(lambda row: row['hotel'] == 'Resort Hotel' and row['is_canceled'] == '0', csvReader))
    return resortHotels


def findCityHotelsWithNoCancels():
    with open('hotel_booking.csv', mode='r') as csvfile:
        csvReader = csv.DictReader(csvfile)
        cityHotels = list(filter(lambda row: row['hotel'] == 'City Hotel' and row['is_canceled'] == '0', csvReader))
    return cityHotels


def findCancellations():
    with open('hotel_booking.csv', mode='r') as csvfile:
        csvReader = csv.DictReader(csvfile)
        cityHotels = list(filter(lambda row: row['hotel'] == 'City Hotel' and row['is_canceled'] == '1', csvReader))
    with open('hotel_booking.csv', mode='r') as csvfile:
        csvReader = csv.DictReader(csvfile)
        resortHotels = list(filter(lambda row: row['hotel'] == 'Resort Hotel' and row['is_canceled'] == '1', csvReader))
    print("The percentage of the total cancellations of the resort Hotels:" + str(
        math.floor(len(resortHotels) / findResortHotels() * 100)))

    print("The percentage of the total cancellations of the city Hotels:" + str(
        math.floor(len(cityHotels) / findCityHotels() * 100)))


def findStayByNight():
    resortHotels = findCityHotelsWithNoCancels()
    cityHotels = findResortHotelsWithNoCancels()
    accumulate_stays = lambda acc, row: acc + int(row['stays_in_week_nights']) + int(row['stays_in_weekend_nights'])

    # Calculate total stays by night for resort hotels
    staysByNightInResortHotel = reduce(accumulate_stays, resortHotels, 0)

    # Calculate total stays by night for city hotels
    staysByNightInCityHotel = reduce(accumulate_stays, cityHotels, 0)

    print('stays by night in resort hotel:', staysByNightInResortHotel / (findResortHotels() + findCityHotels()))
    print('stays by night in city hotels:', staysByNightInCityHotel / (findCityHotels() + findResortHotels()))


def bookingsPerSeasonAndMonth():
    monthsMappedToSeasons = {'January': 'Winter', 'February': 'Winter', 'March': 'Spring', 'April': 'Spring',
                             'May': 'Spring',
                             'June': 'Summer', 'July': 'Summer', 'August': 'Summer', 'September': 'Fall',
                             'October': 'Fall',
                             'November': 'Fall', 'December': 'Winter'}
    bookingsPerSeasonResortHotel = {season: 0 for season in monthsMappedToSeasons.values()}
    bookingsPerMonthResortHotel = {month: 0 for month in monthsMappedToSeasons.keys()}
    bookingsPerSeasonCityHotel = bookingsPerSeasonResortHotel.copy()
    bookingsPerMonthCityHotel = bookingsPerMonthResortHotel.copy()
    resortHotels = findResortHotelsWithNoCancels()
    cityHotels = findCityHotelsWithNoCancels()
    for key, value in monthsMappedToSeasons.items():
        bookingsPerMonthResortHotel[key] = len(list(filter(lambda row: row['arrival_date_month'] == key, resortHotels)))
        bookingsPerSeasonResortHotel[value] += bookingsPerMonthResortHotel[key]
    for key, value in monthsMappedToSeasons.items():
        bookingsPerMonthCityHotel[key] = len(list(filter(lambda row: row['arrival_date_month'] == key, cityHotels)))
        bookingsPerSeasonCityHotel[value] += bookingsPerMonthCityHotel[key]
    print("seasons booking city hotel: " + str(bookingsPerSeasonCityHotel))
    print("seasons booking resort hotel: " + str(bookingsPerSeasonResortHotel))
    print("month booking city hotel: " + str(bookingsPerMonthCityHotel))
    print("month booking resort hotel: " + str(bookingsPerMonthResortHotel))


def bookingsPerRoomType():
    pass


def travellerKinds():
    pass


findCancellations()
findStayByNight()
bookingsPerSeasonAndMonth()
