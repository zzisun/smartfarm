import pandas as pd
import re
from collections import defaultdict
import json
import requests

default_status_excel = "../Plant_Status_fixed.xlsx"
url = "http://127.0.0.1:8000/device_management/store_default_status"

'''
df = pd.DataFrame({'c0':[0,1,2],'c1':[1,2,3],'c2':[4,5,6],'c3':[7,8,9]})
df.to_csv("test.csv", index=False)
df1 = pd.read_csv("test.csv", usecols=['c0','c1'])
print(df1)
'''


class Default_Status_Handler():
    default_status = pd.read_excel(default_status_excel, sheet_name="Plant data", usecols="A:C,E:L",index_col=None, dtype={"Light (hr)":str})
    #default_status = pd.read_csv(default_status_excel, usecols=['Plant Name','PH', 'EC'])

    ''' because of REGEX down there, it occurs bug when changing NAN values to MINUS(-) values....'''
    default_status = default_status.fillna(0)
    status_columns = default_status.columns
    #print(status_columns)

    
    def parse_Status(self):

        '''except column "Plant name"'''
        for column_name in self.status_columns[1:]:
            arr_min = []
            arr_max = []
            for values in self.default_status[column_name]:
                
                
                #minmaxvalue = re.sub(" ", "", str(values))

                ''' because of this REGEX, it occurs bug when changing NAN values to MINUS(-) values....'''
                minmaxvalue = re.split('to|,| to | - |-|–| – |\s',str(values))
                
                '''seperate min, max values'''
                if (column_name == "Seedling_EC" or column_name == "PH" or column_name == "EC"):
                    minmaxvalue[0] = float(minmaxvalue[0])
                    if len(minmaxvalue) > 1:
                        '''because Seedling_EC has only one value, type is float'''
                        if (column_name == "Seedling_EC"):
                            minmaxvalue[1] = float(minmaxvalue[0])
                        else:
                            minmaxvalue[1] = float(minmaxvalue[1])
                
                elif (column_name == "Harvesting_time"):
                    minmaxvalue[0] = int(minmaxvalue[0]) * 7
                    if len(minmaxvalue) > 1:
                        minmaxvalue[1] = int(minmaxvalue[0]) * 7
                
                else:
                    minmaxvalue[0] = int(minmaxvalue[0])
                    if len(minmaxvalue) > 1:
                        minmaxvalue[1] = int(minmaxvalue[1])                    
                
                '''store min value, max value to buffer list'''
                arr_min.append(minmaxvalue[0])
                if len(minmaxvalue) > 1:
                    arr_max.append(minmaxvalue[1])
                else:
                    arr_max.append(minmaxvalue[0])
                
                #print(column_name)
                #print(minmaxvalue)
            
            if (column_name == "Harvesting_time" or column_name == "Seedling_EC"):
                self.default_status.insert(loc=0, column = column_name.lower(), value=arr_min)
                self.default_status = self.default_status.drop(columns = column_name)

            else:
                self.default_status.insert(loc=0, column = column_name.lower() + '_max', value=arr_max)
                self.default_status.insert(loc=0, column = column_name.lower() + '_min', value=arr_min)
                self.default_status = self.default_status.drop(columns = column_name)
        
        self.default_status.insert(loc = 0, column = "crop_name", value=self.default_status["Plant_name"])
        self.default_status = self.default_status.drop(columns = "Plant_name")

        #print("Parsed default_status values")
        #print(self.default_status)
        return self.default_status

    def make_model_similar_dicts(self, default_status):
        default_status_dict_list = []
        for idx,row in default_status.iterrows():
            status_dict = defaultdict()
            status_dict["crop_name"] = row["crop_name"]
            status_dict["co2_min"] = row["co2_min"]
            status_dict["co2_max"] = row["co2_max"]
            status_dict["do_min"] = row["do_min"]
            status_dict["do_max"] = row["do_max"]
            status_dict["humidity_min"] = row["humidity_min"]
            status_dict["humidity_max"] = row["humidity_max"]
            status_dict["harvesting_time"] = row["harvesting_time"]
            status_dict["ec_min"] = row["ec_min"]
            status_dict["ec_max"] = row["ec_max"]
            status_dict["ph_min"] = row["ph_min"]
            status_dict["ph_max"] = row["ph_max"]
            status_dict["temp_min"] = row["temp_min"]
            status_dict["temp_max"] = row["temp_max"]
            status_dict["light_hr_min"] = row["light_hr_min"]
            status_dict["light_hr_max"] = row["light_hr_max"]
            status_dict["seedling_ec"] = row["seedling_ec"]
            status_dict["germination_time_min"] = row["germination_time_min"]
            status_dict["germination_time_max"] = row["germination_time_max"]
            
            #print("Dict -------------------------------------------------------------------")
            #print((status_dict))
            default_status_dict_list.append(status_dict)   
        #print("Result Dict List-------------------------------------------------------------------")     
        #print(default_status_dict_list)
        return default_status_dict_list


# text1 = re.split('-|,|to| to | - ', "5 to 10")
handler = Default_Status_Handler()
send_default_stat = handler.make_model_similar_dicts(handler.parse_Status())

for default_stat in send_default_stat:
    res = requests.patch(url, headers = {'accept' : 'application/json','content-type' : 'application/json;charset=UTF-8'}, data=json.dumps(default_stat))
    print(res.json())