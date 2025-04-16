import requests


def check_input(number):
    try:
        val = int(str(number))
        return val
    except ValueError:
        print("That's not an int!")


print("Input the username you wish to see the activity of")
username = input()
print("Requested data of: "+username)

print("How much  recent activity do you wish to see?")
number = input()
number = check_input(number)


def request_response(username):
    response = requests.get(f"https://api.github.com/users/{username}/events",timeout=5)
    return response

def check_status(response):
    if response.status_code == 200:
        return "Check OK"
    else:
        return f"NOT GOOD AAAA!!!! Error: {response.status_code}"

def fetch_data(username,number,response):
    data = response.json()
    if not data:
        print("No recent activity found.")
        return
    print("\nRecent Public Events:\n")
    for event in data[:number]:  # Just show the 5 most recent
        print(f"- Type: {event['type']}")
        print(f"  Repo: {event['repo']['name']}")
        print(f"  Created at: {event['created_at']}\n")


x = request_response(username)
if check_status(x) == "Check OK":
    fetch_data(username,number,x)
else:
    raise Exception("Something went wrong")

