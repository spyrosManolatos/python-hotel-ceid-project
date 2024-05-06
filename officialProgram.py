import pandas as pd


def findHotelsCancellations():
    mydict = pd.read_csv('hotel_booking.csv')
    averageCancellations = mydict.groupby('hotel')['is_canceled'].size() / len(mydict) * 100
    print("Percentages of each cancellation: ")
    print(averageCancellations)


def findStaysNightsBy():
    mydict = pd.read_csv('hotel_booking.csv')
    mydict['total_nights_spent_by'] = mydict['stays_in_week_nights'] + mydict['stays_in_weekend_nights']
    findsStayNights = mydict.groupby('hotel')['total_nights_spent_by'].size() / len(mydict)
    print("Average nights spent by: ")
    print(findsStayNights)


def findStaysPerSeasonAndPerMonth():
    monthsMappedToSeasons = {'January': 'Winter', 'February': 'Winter', 'March': 'Spring', 'April': 'Spring',
                             'May': 'Spring',
                             'June': 'Summer', 'July': 'Summer', 'August': 'Summer', 'September': 'Fall',
                             'October': 'Fall',
                             'November': 'Fall', 'December': 'Winter'}
    mydict = pd.read_csv('hotel_booking.csv')
    mydictResortHotels = mydict[mydict['hotel'] == 'Resort Hotel'].copy()
    findMonthBookingsResortHotels = mydictResortHotels.groupby('arrival_date_month').size()
    mydictCityHotels = mydict[mydict['hotel'] == 'City Hotel'].copy()
    findMonthBookingsCityHotels = mydictCityHotels.groupby('arrival_date_month').size()
    print('Resort Hotel Data:(bookings per month): ')
    print(findMonthBookingsResortHotels)
    print('City Hotel Data:(bookings per month): ')
    print(findMonthBookingsCityHotels)
    mydictResortHotels.loc[:, 'season'] = mydictResortHotels['arrival_date_month'].map(
        lambda x: monthsMappedToSeasons.get(x))
    mydictCityHotels.loc[:, 'season'] = mydictCityHotels['arrival_date_month'].map(
        lambda x: monthsMappedToSeasons.get(x))
    findSeasonBookingsCityHotels = mydictCityHotels.groupby('season').size()
    findSeasonBookingsResortHotels = mydictResortHotels.groupby('season').size()
    print('City Hotel Data:(bookings per season): ')
    print(findSeasonBookingsCityHotels)
    print('Resort Hotel Data:(bookings per season): ')
    print(findSeasonBookingsResortHotels)


def bookingsPerRoomType():
    mydict = pd.read_csv('hotel_booking.csv')
    dataTypePerRoomTypeResortHotels = mydict[mydict['hotel'] == 'Resort Hotel'].copy().groupby(
        'assigned_room_type').size()
    dataTypePerRoomTypeCityHotels = mydict[mydict['hotel'] == 'City Hotel'].copy().groupby('assigned_room_type').size()
    print('City Hotel Room Type:(assigned_room_type)')
    print(dataTypePerRoomTypeCityHotels)
    print('Resort Hotel Room Type(assigned_room_type)')
    print(dataTypePerRoomTypeResortHotels)


def travellerKinds():
    mydict = pd.read_csv('hotel_booking.csv')
    mydict['families'] = ((mydict['adults'] == 2) & ((mydict['children'] >= 1) | (mydict['babies'] >= 1))).astype(int)
    mydict['couples'] = ((mydict['adults'] == 2) & (mydict['children'] == 0) | (mydict['babies'] == 0)).astype(int)
    mydict['individualTravellers'] = ((mydict['adults'] >= 1) & (mydict['adults'] != 2) & (mydict['children'] == 0) & (
                mydict['babies'] == 0)).astype(int)
    dataTypeTravellerKinds = mydict.groupby('hotel')[['families', 'couples', 'individualTravellers']].sum()
    print(dataTypeTravellerKinds)

findHotelsCancellations()
findStaysNightsBy()
findStaysPerSeasonAndPerMonth()
bookingsPerRoomType()
travellerKinds()
