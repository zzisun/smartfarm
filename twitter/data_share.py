# device data share


# 나중에 Model data 받아와서 object.filter(id=..)로 정보 받아온 후
# 아래의 함수로 데이터 처리후 send
def parameter_send():
    #send text data for tweet
    device_name = "Indoor Grow 1" # FOREIGHN_KEY 로 나오지만, IF문으로 처리하여 string으로 바꿈
    gp = {} #growth param
    gp["germination_time"] = 3
    gp["seeding_ec"] = 10
    gp["ec"] = 1.4
    gp["progress_date"] = 38 #38 days
    gp["temparature"] = 75
    gp["humidity"] = 70
    gp["date"] = "2021/05/28" #str(year)+ "/" + ...
    gp["plant_info"] = "cabbage"# FOREIGHN_KEY 로 나오지만, IF문으로 처리하여 string으로 바꿈
    gp["light_hr"] = 10
    text = "device name : " + device_name + "/"
    for _, param in gp.items():
        if type(param) != str:
            text += str(param)
        else:
            text += param
        text += "/"
    return text



# share 된 parameter을 get해서 모델에 넣어주는 함수.
def parameter_get(text):
    gp = {}
    text = text.split('/')
    print(len(text), text)
    del text[0] #device name
    del text[-1] #hashtag
    gp["germination_time"] = text[0]
    gp["seeding_ec"] = text[1]
    gp["ec"] = text[2]
    gp["progress_date"] = text[3]
    gp["temparature"] = text[4]
    gp["humidity"] = text[5]
    gp["year"] = text[6]
    gp["month"] = text[7]
    gp["date"] = text[8]
    gp["plant_info"] = text[9]
    gp["light_hr"] = text[10]
    print(gp)
    return gp