import json, requests
from collections import OrderedDict
from random import *
from datetime import datetime, timedelta

datas = []
dates = []
num = 10


url = input("url : ")
device_serial = int(input("device_serial : "))
plant_info_id = int(input("plant_info_id : "))
#url = "http://158.247.227.73:8000/device_management/create_plant_params"
#url = "http://127.0.0.1:8000/device_management/create_plant_params"
date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
stand_date = datetime(year, month, day)

for i in range(num):
    dates.append(((stand_date + timedelta(i)).strftime("%Y-%m-%d")))

for i in range(num):
    file_data = OrderedDict()
    file_data['device_info'] = device_serial
    file_data['germination_time'] = 10 + randint(-10, 10)
    file_data['seeding_ec'] = round(uniform(0.1, 1.5), 1)
    file_data['ec'] = round(uniform(0.1, 1.5), 1)
    file_data['ph'] = round(6.5 + uniform(-1.9, 1.9), 1)
    file_data['temparature'] = 60 + randint(-15, 15)
    file_data['humidity'] = 70 + round(uniform(-10, 10), 1)
    file_data['date'] = dates[i]
    file_data['plant_info'] = plant_info_id
    file_data['light_hr'] = 15 + randint(-15, 5)
    file_data['light_lux'] = 200 + randint(-50, 50)
    file_data['nutrientA'] = round(50 + uniform(-50, 50), 1)
    file_data['nutrientB'] = round(50 + uniform(-50, 50), 1)
    file_data['nutrientC'] = round(50 + uniform(-50, 50), 1)
    file_data['nutrientD'] = round(50 + uniform(-50, 50), 1)
    file_data['progress_date'] = 15 + randint(-15, 15)
    file_data['do'] = 6 + randint(-2, 2)
    file_data['co2'] = 400 + randint(-20, 20)

    #print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
    datas.append(file_data)

print(json.dumps(datas, ensure_ascii=False, indent="\t"))

for i in range(num):
    res = requests.post(\
        url,\
        headers = {'accept' : 'application/json','content-type' : 'application/json;charset=UTF-8'}, \
        data=json.dumps(datas[i]))
    print(res.json())
