#!/usr/bin/python3
"Python script that exports data in CSV format"
from csv import writer, QUOTE_ALL
import requests
import sys


def get_employee_todo_progress(employee_id):
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
    employee_name = user_data["username"]

    # Fetch TODO list data
    todos_url = f"{base_url}//todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    total_tasks = len(todos_data)

    file_name = "{}.csv".format(employee_id)

    with open(file_name, 'w', newline='', encoding='utf8') as f:
        task_writer = writer(f, delimiter=',', quotechar='"',
                             quoting=QUOTE_ALL)
        for todo in todos_data:
            completed = todo.get("completed")
            title = todo.get("title")
            task_writer.writerow([employee_id, employee_name,
                                  completed, title])


if __name__ == "__main__":
    get_employee_todo_progress(sys.argv[1])
