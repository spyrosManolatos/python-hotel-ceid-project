import csv
import math

def cityOrResortHotelPercentage():
    totalRecordsCounter = 0
    cityHotelCounter = 0
    resortHotelCounter = 0
    with open('hotel_booking.csv', mode='r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            for key, value in row.items():
                if key == 'hotel':
                    totalRecordsCounter = totalRecordsCounter + 1
                    if value == 'Resort Hotel':
                        resortHotelCounter = resortHotelCounter + 1
                    else:
                        cityHotelCounter = cityHotelCounter + 1
    print("Total Record Counter: " + str(totalRecordsCounter))
    print("Percentage of city hotels: " + str(math.floor((cityHotelCounter/totalRecordsCounter) * 100)))
    print("Percentage of resort hotels: " + str(math.floor((resortHotelCounter/totalRecordsCounter) * 100)))



def findCancellations():
    cancelResort = 0
    cancelCity = 0
    cancelArray = []
    cancelArray.append(cancelResort)  ##counter for cancelResort
    cancelArray.append(cancelCity)   ##counter for cancelCity
    with open('hotel_booking.csv', mode='r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            for key, value in row.items():
                for key2, value2 in row.items():
                    if key == 'is_canceled' and key2 == 'hotel':
                        if value == '1' and value2 == 'Resort Hotel':
                            cancelArray[0] = cancelArray[0] + 1
                        elif value == '1' and value2 == 'City Hotel':
                            cancelArray[1] = cancelArray[1] + 1
    # print("Total cancellations: " + str(cancelArray.reduce(lambda x,y: x+y)))
    print("Total City Hotel cancellations: " + str(cancelArray[0]))
    print("Total Resort Hotel cancellations: " + str(cancelArray[1]))


findCancellations()
cityOrResortHotelPercentage()
