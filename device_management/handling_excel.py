import pandas as pd

default_status_excel = "../Plant_Status_fixed.xlsx"
'''
df = pd.DataFrame({'c0':[0,1,2],'c1':[1,2,3],'c2':[4,5,6],'c3':[7,8,9]})
df.to_csv("test.csv", index=False)
df1 = pd.read_csv("test.csv", usecols=['c0','c1'])
print(df1)
'''
class Default_Status_Handler():
    default_status = pd.read_excel(default_status_excel, sheet_name="Plant data", usecols="A:C,E:L",index_col=None, dtype={"Light (hr)":str})
    #default_status = pd.read_csv(default_status_excel, usecols=['Plant Name','PH', 'EC'])
    print(default_status.head(5))
    

    def get_Status():
       
       return 
