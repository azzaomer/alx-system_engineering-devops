import requests
import sys


def tasks(id):
    '''Script that exports an employee TODO tasks to a json file
        Parameters:
        employee_id: Is an interger representing an employee id.
    '''

    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    response = requests.get(url)
    response_json = response.json()
    employee_name = response_json.get("name")

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

    todos[id] = task_list
    id += 1

    file_name = "todo_all_employees.json"
    with open(file_name, "a") as f:
        json.dump(todos, f)


if __name__ == "__main__":
    tasks(sys.argv[1])
