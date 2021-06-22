import pandas as pd
import re

default_status_excel = "../Plant_Status_fixed.xlsx"
'''
df = pd.DataFrame({'c0':[0,1,2],'c1':[1,2,3],'c2':[4,5,6],'c3':[7,8,9]})
df.to_csv("test.csv", index=False)
df1 = pd.read_csv("test.csv", usecols=['c0','c1'])
print(df1)
'''
class Default_Status_Handler():
    default_status = pd.read_excel(default_status_excel, sheet_name="Plant data", usecols="A:C,E:L",index_col=None, dtype={"Light (hr)":str}).head(5)
    #default_status = pd.read_csv(default_status_excel, usecols=['Plant Name','PH', 'EC'])
    status_columns = default_status.columns
    
    def parse_Status(self):
        for column_name in self.status_columns:
            for values in self.default_status[column_name]:
                print(values)
                
                #minmaxvalue = re.split('-|,|to| to | - ', str(values))
                minmaxvalue = re.sub(" ", "", str(values))
                minmaxvalue = re.split('["to"\\,\\-]+',minmaxvalue)
                print(minmaxvalue)
        return 
# text1 = re.split('-|,|to| to | - ', "5 to 10")
handler = Default_Status_Handler()
handler.parse_Status()