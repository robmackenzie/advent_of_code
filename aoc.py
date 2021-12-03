#!/usr/bin/env python3
import secrets
site_url='https://adventofcode.com/2021/day/[day]'
input_url='https://adventofcode.com/2021/day/[day]/input'


import os,webbrowser,requests,glob,sys
from datetime import datetime, time, timedelta,timezone
from time import sleep
from shutil import copyfile


def before_script(day_num):
    day_folder_name="Day_" + f'{day_num:02d}'
    if not(glob.glob(day_folder_name+"*")):
        os.mkdir(day_folder_name)
        copyfile("Template/template.ipynb",day_folder_name + "/Day_" + f'{day_num:02d}' + ".ipynb")
        print("Creating directory for " + day_folder_name)
    else:
        print(day_folder_name + " Directory already exists.")
def post_script(day_num):
    day_site_url=site_url.replace('[day]',str(day_num))
    day_input_url=input_url.replace('[day]',str(day_num))
    folder_name=glob.glob("Day_" + f'{day_num:02d}'+"*")[0]
    input_request = requests.get(day_input_url, cookies=secrets.cookie)
    input_request.raise_for_status()
    with open(folder_name+"/input", "w") as file:
        file.write(input_request.text)
    #webbrowser.open_new(day_site_url)


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2
        day = int(sys.argv[1])
    except:
        exit("You must provide a day to download")
    # Run the stuff that's safe to do before the release
    before_script(day)
    aoc_release_time=datetime(2021,12,day,0,0,1,tzinfo=timezone(timedelta(hours=-5)))
    now=datetime.now(timezone(timedelta(hours=-8)))
    delta = aoc_release_time - now
    if delta > timedelta(0):
        print("Time until release: " + str(delta))
        print("Sleeping until that time")
        sleep(delta.total_seconds())
    else:
        print("Release has passed. It's been: " + str(delta))
    # Run the stuff for after release!
    post_script(day)