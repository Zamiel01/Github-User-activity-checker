import argparse
import urllib.request
import urllib.error
import json

parser = argparse.ArgumentParser(description="Github User Activity CLI.")
parser.add_argument('username', type=str, help="Enter github username")
args = parser.parse_args()

username = args.username
api = f"https://api.github.com/users/{username}/events"
profile_url = f"https://github.com/{username}"

# Check if username exists
try:
    urllib.request.urlopen(profile_url)
except urllib.error.HTTPError as e:
    if e.code == 404:
        print("Username doesn't exist")
        exit()
    else:
        print(f"Error: {e}")
        exit()

# Fetch user events
try:
    response = urllib.request.urlopen(api)
    data = response.read().decode('utf-8')
    new_data = json.loads(data)
    print(json.dumps(new_data, indent=4))
except urllib.error.HTTPError as e:
    print(f"Failed to fetch events: {e}")
