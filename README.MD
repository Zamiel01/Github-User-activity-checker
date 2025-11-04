GitHub User Activity CLI

A simple command-line tool to fetch and display GitHub user activity in a readable JSON format. This script checks if a GitHub username exists before fetching the user’s latest public events.

Features

Validate if a GitHub username exists.

Fetch latest GitHub user events via the GitHub API.

Display events in a human-readable JSON format.

Lightweight and easy to use with no external dependencies besides Python standard libraries.

Requirements

Python 3.x

Internet connection

No external Python packages are required.

Installation

Clone this repository:

git clone https://github.com/your-username/github-user-activity-cli.git


Navigate into the project directory:

cd github-user-activity-cli


Make sure Python 3 is installed:

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
https://api.github.com/users/<username>/events.

The response is formatted as JSON with indentation for readability.

If the username does not exist, the script exits with a friendly message.