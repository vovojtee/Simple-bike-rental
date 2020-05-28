import datetime


class BikeRental:

    def __init__(self, stock=0):
        # Constructor class that instantiates bike rental shop
        self.stock = stock

    def displaystock(self):
        # Displays the bikes currently available for rent in the shop
        print('We have currently {} bikes available to rent'.format(self.stock))
        return self.stock

    def rentBikeOnHourlyBasis(self, n):
        if n <= 0:
            print('Number of bikes must be positive.')
            return None

        elif n > self.stock:
            print('Sorry, we have currently {} bikes to rent'.format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            hourlyPrice = 5
            print('You have rented {} bike(s) on hourly basis today at {} hours'.format(n, now.hour))
            print('You will be charged ${} for each hour per bike'.format(hourlyPrice))
            print('We hope that you enjoy our service!')

            self.stock -= n
            return now

    def rentBikeOnDailyBasis(self, n):
        if n <= 0:
            print('Number of bikes must be positive.')
            return None

        elif n > self.stock:
            print('Sorry, we have currently {} bikes to rent'.format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            dailyPrice = 40
            print('You have rented {} bike(s) on daily basis today at {} hours'.format(n, now.hour))
            print('You will be charged ${} for each day per bike'.format(dailyPrice))
            print('We hope that you enjoy our service!')

            self.stock -= n
            return now

    def rentBikeOnWeeklyBasis(self, n):
        if n <= 0:
            print('Number of bikes must be positive.')
            return None

        elif n > self.stock:
            print('Sorry, we have currently {} bikes to rent'.format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            weeklyPrice = 150
            print('You have rented {} bike(s) on weekly basis today at {} hours'.format(n, now.hour))
            print('You will be charged ${} for each week per bike'.format(weeklyPrice))
            print('We hope that you enjoy our service!')

            self.stock -= n
            return now


    def returnBike(self, request):

        '''
        1. Accept a rented bike from a customer
        2. Replenishes the inventory
        3. Return a bill
        '''

        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            # the prices
            hourlyPrice = 5
            dailyPrice = 40
            weeklyPrice = 150

            # hourly bill calc:
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * hourlyPrice * numOfBikes

            # daily bill calc:
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * dailyPrice * numOfBikes

            # weekly bill calc:
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * weeklyPrice * numOfBikes


            # Exclusive family discount
            if (3 <= numOfBikes <= 5):
                print('You are eligible for Family rental promo of 30% discount')
                bill *= 0.7


            print('Thank you for returning your bike. We hope you enjoyed the ride!')
            print('That would be ${}'.format(bill))
            return bill
        else:
            print('You have nothing to return. Are you sure you rented a bike from us?')
            return None


class Customer:

    def __init__(self):

        # method that instantiates some customer objects
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0


    def requestBike(self):

        # takes a request (int input) from the customer for the number of bikes
        bikes = input('How many bikes would you like to rent?')
        try:
            bikes = int(bikes)
        except ValueError:
            print('This is not a number. Try again')
            return -1

        if bikes < 1:
            print('No you can not rent negative number of bikes. Try again')
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    def returnBike(self):

        # allows customers to return their bikes to the rental shop
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0, 0, 0
