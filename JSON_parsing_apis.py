import requests
import json
# # Iteration 1
# post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
# print(post_codes_req.status_code)
#
# # Dont need to manually declare == 200, built in packages do it already
# if post_codes_req.status_code == 200:
#     print("It worked!")
# elif post_codes_req.status_code:
#     print("Page not available")
#

# Iteration 2, doing same output with oop
class Status_code:

    # Getting user input of url
    def __init__(self, url):
        self.url = url

    def check_status_code(self):
        # Getting status of website, using requests function
        self.post_codes_req = requests.get(self.url)
        print(self.post_codes_req.status_code)

class Live_web_status(Status_code):

    # Inheriting url attribute from Status_code class
    def __init__(self, url):
        super().__init__(url)

    def live_web_status(self):
        # Calling function from parent class to get status code of the website
        self.check_status_code()
        # Dont need to manually declare == 200, built in packages do it already
        if self.post_codes_req.status_code == 200:
            print("It worked!")
        elif self.post_codes_req.status_code:
            print("Page not available")

# Creating and testing class object
obj1 = Live_web_status("https://api.postcodes.io/postcodes/se120nb")
obj1.live_web_status()

