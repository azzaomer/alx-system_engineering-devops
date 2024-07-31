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
    task_list = {}

    for employee in employees:
        employee_id = employee["id"]
        user_url = url + f"todos?userId={employee_id}"
        todo_list = requests.get(user_url).json()
        for todo in todo_list:
            task_list[employee_id] = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_name
            }
            task_list[employee_id].append(task_list)
    return task_list

if __name__ == "__main__":
    task_list = tasks_completed()
    file_name = "todo_all_employees.json"
    with open(file_name, "w") as f:
        json.dump(task_list, f, indent= 4)
