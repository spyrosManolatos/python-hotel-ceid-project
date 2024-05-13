import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
import csv


def createGui():
    root = tk.Tk()
    root.title('Python Project Basic Principles of Coding Languages And Compiling 2024')

    label1 = tk.Label(root, text='Python Project Basic Principles of Coding Languages And Compiling 2024')
    label1.pack(pady=10)
    label2 = tk.Label(root, text='Press whatever tf you want to execute the functions that are demanded:(')
    label2.pack(pady=10)
    frame = tk.Frame(root)
    frame.pack()
    button1 = tk.Button(root, text='Hotels Cancellations per Hotel Type',
                        command=lambda: dispDataSet(frame, findHotelsCancellations()))
    button1.pack(pady=5)
    button2 = tk.Button(root, text='Night Stays per Hotel Type',
                        command=lambda: dispDataSet(frame, findStaysNightsBy()))
    button2.pack(pady=5)
    button3 = tk.Button(root, text='Stays Per Month(Resort Hotels)',
                        command=lambda: dispDataSet(frame, findStaysPerMonth('Resort Hotel')))
    button3.pack(pady=5)
    button4 = tk.Button(root, text='Stays Per Month(City Hotels)',
                        command=lambda: dispDataSet(frame, findStaysPerMonth('City Hotel')))
    button4.pack(pady=5)
    button5 = tk.Button(root, text='Stays Per Season(Resort Hotels)',
                        command=lambda: dispDataSet(frame, findStaysPerSeason('Resort Hotel')))
    button5.pack(pady=5)
    button6 = tk.Button(root, text='Stays Per Season(City Hotels)',
                        command=lambda: dispDataSet(frame, findStaysPerSeason('City Hotel')))
    button6.pack(pady=5)
    button7 = tk.Button(root, text='Booking per room type(Resort Hotels)',
                        command=lambda: dispDataSet(frame, bookingsPerRoomType('Resort Hotel')))
    button7.pack(pady=5)
    button8 = tk.Button(root, text='Booking per room type(City Hotels)',
                        command=lambda: dispDataSet(frame, bookingsPerRoomType('City Hotel')))
    button8.pack(pady=5)
    button9 = tk.Button(root, text='traveller kinds',
                        command=lambda: dispDataSet(frame, travellerKinds()))
    button9.pack(pady=5)
    button10 = tk.Button(root, text='monthly change rate for resort hotel',
                         command=lambda: dispDataSet(frame, bookingChangeRate('Resort Hotel')))
    button10.pack(pady=5)
    button11 = tk.Button(root, text='monhtly change rate for city hotel',
                         command=lambda: dispDataSet(frame, bookingChangeRate('City Hotel')))
    button11.pack(pady=5)
    root.mainloop()


def dispDataSet(frame, dataset):
    for widget in frame.winfo_children():
        widget.destroy()
    for idx, data in enumerate(dataset):
        label = tk.Label(frame, text=data)
        label.grid(row=idx, column=0, sticky='w', padx=10, pady=5)
    # x_values = dataset.keys()
    # y_values = dataset.values()
    # plt.plot(x_values, y_values)
    # plt.xlabel('X-AXIS')
    # plt.ylabel('Y-AXIS')
    # plt.show()


def findHotelsCancellations():
    mydict = pd.read_csv('hotel_booking.csv')
    averageCancellations = mydict.groupby('hotel')['is_canceled'].size() / len(mydict) * 100
    return [f'Average Cancellations for {hotel}: {cancellation:.2f}%' for hotel, cancellation in
            averageCancellations.items()]


def findStaysNightsBy():
    mydict = pd.read_csv('hotel_booking.csv')
    noCancellations = mydict[mydict['is_canceled'] == 0]
    noCancellations['total_nights_spent_by'] = noCancellations['stays_in_week_nights'] + noCancellations[
        'stays_in_weekend_nights']

    findsStayNights = noCancellations.groupby('hotel')['total_nights_spent_by'].size() / len(
        noCancellations)
    return [f'Average Nights Stayed for {hotel}: {nights:.2f}' for hotel, nights in findsStayNights.items()]


def findStaysPerMonth(hotelType):
    hotels = pd.read_csv('hotel_booking.csv')
    filterHotelsPerHotelType = hotels[hotels['hotel'] == hotelType].copy()
    noCanceledHotels = filterHotelsPerHotelType[filterHotelsPerHotelType['is_canceled'] == 0]
    findMonthBookingsResortHotels = noCanceledHotels.groupby('arrival_date_month').size()
    return [f'Average month bookings for{hotelType}:{months},{values}' for months, values in
            findMonthBookingsResortHotels.items()]


def findStaysPerSeason(hotelType):
    monthsMappedToSeasons = {'January': 'Winter', 'February': 'Winter', 'March': 'Spring', 'April': 'Spring',
                             'May': 'Spring',
                             'June': 'Summer', 'July': 'Summer', 'August': 'Summer', 'September': 'Fall',
                             'October': 'Fall',
                             'November': 'Fall', 'December': 'Winter'}
    hotels = pd.read_csv('hotel_booking.csv')
    hotelsHotelType = hotels[hotels['hotel'] == hotelType]
    hotelsNoCancelations = hotelsHotelType[hotelsHotelType['is_canceled'] == 0]
    hotelsNoCancelations.loc[:, 'season'] = hotelsNoCancelations['arrival_date_month'].map(
        lambda x: monthsMappedToSeasons.get(x))
    findSeasonBookings = hotelsNoCancelations.groupby('season').size()
    return [f'The bookings per season are for {hotelType} are :{key},{value}' for key, value in
            findSeasonBookings.items()]


def bookingsPerRoomType(hotel_kind):
    hotels = pd.read_csv('hotel_booking.csv')
    hotelsHotelType = hotels[hotels['hotel'] == hotel_kind]
    hotelsNoCancelations = hotelsHotelType[hotelsHotelType['is_canceled'] == 0]
    hotelsPerRoomType = hotelsNoCancelations.groupby('assigned_room_type').size()
    return [f'The bookings per room type are for {hotel_kind} are :{key},{value}' for key, value in
            hotelsPerRoomType.items()]


def travellerKinds():
    hotels = pd.read_csv('hotel_booking.csv')
    noCanceledHotels = hotels[hotels['is_canceled'] == 0]
    noCanceledHotels['families'] = ((noCanceledHotels['adults'] == 2) & (
            (noCanceledHotels['children'] >= 1) | (noCanceledHotels['babies'] >= 1))).astype(int)
    noCanceledHotels['couples'] = ((noCanceledHotels['adults'] == 2) & (noCanceledHotels['children'] == 0) | (
            noCanceledHotels['babies'] == 0)).astype(int)
    noCanceledHotels['individualTravellers'] = (
            (noCanceledHotels['adults'] >= 1) & (noCanceledHotels['adults'] != 2) & (
            noCanceledHotels['children'] == 0) & (
                    noCanceledHotels['babies'] == 0)).astype(int)
    dataTypeTravellerKinds = noCanceledHotels.groupby('hotel')[['families', 'couples', 'individualTravellers']].sum()
    return [f'The bookings per travel group are :wh{key},{value}' for key, value in
            dataTypeTravellerKinds.items()]


def bookingChangeRate(hotel_type):
    hotels = pd.read_csv('hotel_booking.csv')
    noCanceledHotels = hotels[hotels['is_canceled'] == 0]
    hotelType = noCanceledHotels[noCanceledHotels['hotel'] == hotel_type]
    findMonthBookingsResortHotels = hotelType.groupby('arrival_date_month').size()
    monthsToChange = {'January-February': 0, 'February-March': 0, 'March-April': 0,
                      'April-May': 0,
                      'May-June': 0, 'June-July': 0, 'July-August': 0, 'August-September': 0,
                      'September-October': 0,
                      'October-November': 0, 'December-January': 0}
    months = list(findMonthBookingsResortHotels.index)
    bookings = list(findMonthBookingsResortHotels.values)
    for i in range(len(months) - 1):
        current_month = months[i]
        next_month = months[i + 1]
        current_bookings = bookings[i]
        next_bookings = bookings[i + 1]
        monthsToChange[f'{current_month}-{next_month}'] = ((next_bookings - current_bookings) / next_bookings) * 100
    return [f'The booking change Rate is {key}:{value:.2f}%' for key, value in monthsToChange.items()]


createGui()
