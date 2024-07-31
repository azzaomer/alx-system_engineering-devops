#!/usr/bin/python3
"Python script that exports data in CSV format"
import requests
import sys


def get_employee_todo_progress(id):
    '''Script that exports an employee TODO tasks to a csv file
        Parameters:
        id: Is an interger representing an employee id.
    '''

    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data["name"]

    # Fetch TODO list data
    todos_url = f"{base_url}/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    total_tasks = len(todos_data)

    task_compleated = 0
    task_list = ""

    file_name = "{}.csv".format(id)

    with open(file_name, "a") as f:
        for todo in todos_data:
            completed = todo.get("completed")
            title = todo.get("title")
            csv_data = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format
            (id, employee_name, completed, title)
            f.write(csv_data)


if __name__ == "__main__":
    get_employee_todo_progress(sys.argv[1])
