#!/usr/bin/python3

"""
Module: API script for retrieving
"""

import requests
import sys
import csv

if __name__ == '__main__':

    base_url = 'https://jsonplaceholder.typicode.com/'
    user_ext = '/users/{}'.format(sys.argv[1])
    todo_ext = '/todos'
    file_name = "{}.csv".format(sys.argv[1])

    employee_response = requests.get(base_url+user_ext)
    employee = employee_response.json()
    todo_response = requests.get(base_url+user_ext+todo_ext)
    todos = todo_response.json()

    file = open(file_name, 'w')
    csv_file = csv.writer(file, quoting=csv.QUOTE_ALL)
    count = 0
    for todo in todos:
        csv_file.writerow([
            employee['id'],
            employee['username'],
            todo['completed'],
            todo['title']
        ])
        
    file.close()
