import secrets
site_url='https://adventofcode.com/2021/day/[day]'
input_url='https://adventofcode.com/2021/day/[day]/input'

from datetime import datetime, time
from time import sleep
import os,webbrowser,requests

def before(day_num):
    folder_name="Day_" + f'{day_num:02d}'
    if not(os.path.isdir(folder_name)):
        os.system("cp -R Template \"" + folder_name + "\"")
def and_go(day_num):
    day_site_url=site_url.replace('[day]',str(day_num))
    day_input_url=input_url.replace('[day]',str(day_num))
    folder_name="Day_" + f'{day_num:02d}'
    webbrowser.open_new(day_site_url)
    input_request = requests.get(day_input_url, cookies=cookie)
    input_request.raise_for_status()
    with open(folder_name+"/input", "w") as file:
        file.write(input_request.text)

before(1)
and_go(1)