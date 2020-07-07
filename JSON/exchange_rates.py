# import json
import json

# create a class exchange_rates
class Exchange_rates:

    # with required attributes(none)
    def __init__(self):
        pass

    def conversion(self):
        with open("exchange_rates.json", "r") as jsonfile:
            self.dataset = json.load(jsonfile)

    # fetch data from exchange_rates.json
    def fetch_data(self):
            # display the data
            print(self.dataset)
            # display the type of data
            print(type(self.dataset))

    # method to return the exchange rates
    def fetch_exchange_rates(self):
            # For loop to get all exchange rates
            for key in self.dataset:
                if key == "rates":
                    print(self.dataset["rates"])

    def fetch_specific_rate(self):
        exchange_rate_data = (self.dataset["rates"])
        # Creating list to print out currencies.
        x = []
        for i in exchange_rate_data:
            x.append(i)
        print(x)
        # Getting currency to get conversion rate for
        currency = input("What currency would you like the exchange rate of, please see list.\n")
        # display exchange rates with specific currencies
        print("1 Euro =", self.dataset["rates"][currency.upper()])

obj1 = Exchange_rates()
obj1.conversion()
# obj1.fetch_data()
# obj1.fetch_exchange_rates()
obj1.fetch_specific_rate()