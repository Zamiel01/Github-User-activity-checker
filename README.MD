# GitHub User Activity CLI

A simple command-line tool to fetch and display GitHub user activity in a readable JSON format. This script checks if a GitHub username exists before fetching the user’s latest public events.

---

## Features

- Validate if a GitHub username exists.  
- Fetch latest GitHub user events via the GitHub API.  
- Display events in a human-readable JSON format.  
- Lightweight and easy to use with no external dependencies besides Python standard libraries.

---

## Requirements

- Python 3.x  
- Internet connection  

> No external Python packages are required.

---

## Installation

1. **Clone this repository:**
```bash
git clone https://github.com/your-username/github-user-activity-cli.git

Navigate into the project directory:


cd github-user-activity-cli



Verify Python 3 is installed:


python3 --version


Usage
Run the script with a GitHub username:
python3 github_user_activity.py <username>

Example:
python3 github_user_activity.py octocat

Output:
[
    {
        "id": "1234567890",
        "type": "PushEvent",
        "actor": {
            "login": "octocat",
            ...
        },
        ...
    }
]

If the username does not exist:
Username doesn't exist


How It Works


The script checks if the username exists on GitHub.


If it exists, it fetches the user’s public events from the GitHub API:
https://api.github.com/users/<username>/events


The response is formatted as JSON with indentation for readability.


If the username does not exist, the script exits with a friendly message.



Notes


Rate Limits: The GitHub API allows up to 60 unauthenticated requests per hour. Exceeding this will result in an HTTP 403 error.


Public Events Only: Only public events are accessible via the API. Private activity is not included.



Contributing
Contributions are welcome! Feel free to:


Submit issues


Fork the repository


Open pull requests



License
This project is licensed under the MIT License.

---

If you want, I can also **enhance this README with badges, color-coded JSON example, and a CLI screenshot section**, making it more visually appealing for GitHub. This can really make it stand out.  

Do you want me to do that?
