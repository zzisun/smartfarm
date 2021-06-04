import json
from collections import OrderedDict
from random import *

datas = []
dates = []
num = 10


device_serial = int(input())
plant_info_id = 9

for i in range(num):
    dates.append("2021-01-1" + str(i))

for i in range(num):
    file_data = OrderedDict()
    #file_data['device_info_id'] = device_serial
    file_data['serial'] = device_serial
    #file_data['plant_info_id'] = plant_info_id
    file_data['ph'] = round(5 + uniform(-3.9, 3.9), 1)
    file_data['temp'] = 50 + randint(-30, 30)
    file_data['ec'] = round(uniform(0.1, 2.0), 1)
    file_data['light_lux'] = 200 + randint(-50, 50)
    file_data['nutrientA'] = round(1.0 + uniform(-0.5, 0.5), 1)
    file_data['date'] = dates[i]
    #print(json.dumps(file_data, ensure_ascii=False, indent="\t"))
    datas.append(file_data)

print(json.dumps(datas, ensure_ascii=False, indent="\t"))