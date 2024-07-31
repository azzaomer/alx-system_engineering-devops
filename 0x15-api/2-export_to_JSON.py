#!/usr/bin/python3
"Python script that exports data to a JSON file"
import json
import requests
import sys


def tasks_complete(id):
    '''Script that exports an employee TODO tasks to a json'''
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    response = requests.get(url)
    response_json = response.json()
    employee_name = response_json.get("name")

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(url)
    todos_json = todos.json()
    task_list = {id: []}

    for task in todos_json:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_name
        }
        task_list[id].append(task_dict)

    # todos = {"{}".format(id): task_list}

    file_name = "{}.json".format(id)
    with open(file_name, "a") as f:
        json.dump(task_list, f)


if __name__ == "__main__":
    tasks_complete(sys.argv[1])
