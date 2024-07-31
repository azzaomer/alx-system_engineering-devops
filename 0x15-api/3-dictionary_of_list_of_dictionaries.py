#!/usr/bin/python3
"Python script that exports data to a JSON format"
import json
import requests
import sys


def tasks_completed():
    '''Python script to export data in the JSON format'''

    id = 1
    tasks_todo = {}
    while True:
        url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        response = requests.get(url)
        response_json = response.json()
        if len(response_json) == 0:
            break
        employee_name = response_json.get("username")

        url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
        todos = requests.get(url)
        todos_json = todos.json()
        task_list = []

        for task in todos_json:
            task_dict = {}
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            task_dict["username"] = employee_name
            task_list.append(task_dict)

        tasks_todo[id] = task_list
        id += 1

    file_name = "todo_all_employees.json"
    with open(file_name, "a") as f:
        json.dump(tasks_todo, f)


if __name__ == "__main__":
    tasks_completed()
