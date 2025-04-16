import requests


print("Input the username you wish to see the activity of")
username = input()
print("Requested data of: "+username)


def request_response(username):
    response = requests.get(f"https://api.github.com/users/{username}/events",timeout=5)
    return response

def check_status(response):
    if response.status_code == 200:
        return "Check OK"
    else:
        return f"NOT GOOD AAAA!!!! Error: {response.status_code}"

def fetch_data(username):



    pass


x = request_response(username)
print(check_status(x))

print(x.json())