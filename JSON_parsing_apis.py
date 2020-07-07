import requests
import json
post_codes_req = requests.get("https://api.postcodes.io/postcodes/se10nb")

print(post_codes_req.status_code)

# This is how websites work
# Dont need to manually declare == 200, built in packages do it already
if post_codes_req.status_code == 200:
    print("It worked!")
elif post_codes_req.status_code:
    print("Page not available")

