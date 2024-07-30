#!/usr/bin/python3
"Python script that exports data in CSV format"
import requests
import sys
import json


def get_employee_todo_progress(id):
    '''Script that exports an employee TODO tasks to a csv file
        Parameters:
        employee_id: Is an interger representing an employee id.
    '''

    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    response = requests.get(url)
    user_response = response.json()
    employee_name = response_json["name"]

    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos_response = requests.get(url)
    todos_data = todos.json()
    total_tasks = len(todos_json)
    task_list = []

    for task in todos_data:
        todo_dict = {}
        todo_dict["task"] = task.get("title")
        todo_dict["completed"] = task.get("completed")
        todo_dict["username"] = employee_name
        task_list.append(todo_dict)
    
    todo = {"{}".format(id): task_list}

    file_name = "{}.json".format(id)
    with open(file_name, "a") as file:
        json.dump(todo, file)
    
    if __name__ == "__main__":
        get_employee_todo_progress(sys.argv[1])
        