#!/usr/bin/env python3

from curses import ERR
from distutils.log import ERROR, error
import os
import requests

filepath = '/data/feedback'
dict_reviews = {}
hostname_ip = '35.24.302.12'

def read_file():
    for file_name in os.listdir(filepath):
        try:
            with open(filepath + '/' + file_name, 'r') as file:
                dict_reviews['title'] = file.readline().rstrip()
                dict_reviews['name'] = file.readline().rsplit()
                dict_reviews['data'] = file.readline().rsplit()
                dict_reviews['feedback'] = file.readline().rsplit()
        except ERROR:
            pass
    post_dict(dict_reviews)

def post_dict(dict_data):
    response = requests.post('https://{hostname_ip}/feedback/', json=dict_data)
    if response.status_code == 201:
        print('Post to site successful for : ', dict_data['title'])
    else:
        print('Error while posintg : ' + dict_data['title'] + ', error code : ' + str(response.status_code))

if __name__ == "__main__":
    read_file()