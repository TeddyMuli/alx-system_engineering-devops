#!/usr/bin/python3
"""Export data to json"""
import json, requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/").json()
    todos = requests.get(url + "todos/")

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": t.get("username")
            } for t in requests.get(url + "todos", params={"userId": u.get("id")}).json()]
        for u in users}, jsonfile)
