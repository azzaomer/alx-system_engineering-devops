#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her ToDo list progress.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    '''Script that displays an employee completed TODO tasks in stout
        Parameters:
        employee_id: Is an interger representing an employee id.
    '''
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch TODO list data
    todos_url = f"{base_url}/users/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate the number of done tasks and total tasks
    total_tasks = len(todos_data)

    task_compleated = 0
    task_list = ""

    # Display the results
    for task in todos_data:
        if task.get("completed") is True:
            task_compleated += 1
            task_list += "\t " + task.get("title") + "\n"

    print("Employee {} is done with tasks({}/{}):" .format(employee_name,
                                                           task_compleated,
                                                           total_tasks))
    print(task_list[:-1])


if __name__ == "__main__":
    get_employee_todo_progress(sys.argv[1])
