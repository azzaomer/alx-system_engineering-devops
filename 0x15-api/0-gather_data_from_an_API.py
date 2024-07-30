#!/usr/bin/python3
"""

"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return
    
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch TODO list data
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"TODO list for user with ID {employee_id} not found.")
        return
    
    todos_data = todos_response.json()

    # Calculate the number of done tasks and total tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Display the results
    print("Employee {} is done with tasks({}/{}):".format(employee_name, task_compleated, number_tasks))
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")