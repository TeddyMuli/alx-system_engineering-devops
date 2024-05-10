#!/usr/bin/python3
"""Export to JSON"""
import json, requests, sys

if __name__ == "__main__":
    userId = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(api_url + "users/{}".format(userId)).json()
    todos = requests.get(api_url + "todos", params={"userid": userId}).json()

    with open("{}.json".format(userId), "w") as jsonfile:
        json.dump({userId: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": users.get("username")
        } for todo in todos]}, jsonfile)
