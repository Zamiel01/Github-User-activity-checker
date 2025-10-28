import subprocess

print('welcome to github user activity checker')

#collecting user name
user = str(input("enter the github username: "))

#using curl command to fetch user github activity
cmd = ["curl", f"https://api.github.com/users/{user}/events"]

result = subprocess.run(cmd, capture_output=True, text=True)

print(result)

 jjj