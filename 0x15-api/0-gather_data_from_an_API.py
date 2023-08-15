#!/usr/bin/python3
"""using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from requests import get
from sys import argv


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_r = requests.get(user_url)
        todos_r = requests.get(todos_url)

        if user_r.status_code != 200 or todos_r.status_code != 200:
            print("Error: Unable to fetch data from the API.")
            return

        user_data = user_r.json()
        todos_data = todos_r.json()

        emp_name = user_data['name']
        total = len(todos_data)
        done = sum(1 for task in todos_data if task['completed'])

        print(f"Employee {emp_name} is done with tasks({done}/{total}):")

        for task in todos_data:
            if task['completed']:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
