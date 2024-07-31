#!/usr/bin/python3
"Python script that exports data to a JSON format"
import json
import requests
import sys


def tasks_completed():
    '''Python script to export data in the JSON format'''

    url = "https://jsonplaceholder.typicode.com/"
    employees = requests.get(url + "users").json()

    # Create a dictionary containing to-do list information of all employees
    data_to_exp = {}

    for employee in employees:
        employee_id = employee["id"]
        user_url = url + f"todos?userId={employee_id}"
        todo_list = requests.get(user_url).json()

        data_to_exp[employee_id] = []
        for todo in todo_list:
            task_list = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": employee.get("username")
            }
            data_to_exp[employee_id].append(task_list)
    return data_to_exp
if __name__ == "__main__":
    data_to_exp = tasks_completed()
    file_name = "todo_all_employees.json"
    with open(file_name, "w") as f:
        json.dump(data_to_exp, f, indent=4)
