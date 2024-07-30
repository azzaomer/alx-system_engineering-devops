#!/usr/bin/python3
"Python script that exports data in CSV format"
import requests
import sys


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

    task_compleated = 0
    task_list = ""

    file_name = "{}.csv".format(id)

    with open(file_name, "a") as fd:
        for todo in todos_data:
            completed = todo.get("completed")
            title = todo.get("title")
            csv_data = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(id, employee_name, completed, title)
            fd.write(csv_data)


if __name__ == "__main__":
    get_employee_todo_progress(sys.argv[1])
