#!/usr/bin/python3
"""Export data to CSV format"""
import csv, requests, sys

if __name__ == "__main__":
    userId = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(api_url + "users/{}".format(userId)).json()
    todos = requests.get(api_url + "todos", params={"userId": userId}).json()

    with open("{}.csv".format(userId), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [userId, users.get("username"), todo.get("completed"), todo.get("title")]
        ) for todo in todos]
