# device data share
import sys
import requests
URL = 'http://127.0.0.1:8000/device_management/status/1'
# 나중에 Model data 받아와서 object.filter(id=..)로 정보 받아온 후
# 아래의 함수로 데이터 처리후 send
def parameter_send():
    #send text data for tweet
    device_name = "Indoor Grow 1" # FOREIGHN_KEY 로 나오지만, IF문으로 처리하여 string으로 바꿈
    gp = {} #growth param
    gp["germination_time"] = 3
    gp["seeding_ec"] = 0.5
    gp["ec"] = 0.80
    gp["progress_date"] = 5 #38 days
    gp["temparature"] = 65
    gp["humidity"] = 50
    gp["date"] = "2021/05/28" #str(year)+ "/" + ...
    gp["light_hr"] = 18
    gp["ph"] = 5.8
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
    #gp["year"] = text[6]
    #gp["month"] = text[7]
    #gp["date"] = text[8]
    gp["light_hr"] = text[9]
    gp["ph"] = text[10]
    print(gp)

    # POST WITH CSRF
    #
    # client = requests.session()
    # client.get(URL)
    # print(client.cookies)
    # if 'csrftoken' in client.cookies:
    #     csrftoken = client.cookies['csrftoken']
    # else:
    #     csrftoken = client.cookies['csrf']
    # gp["csrfmiddlewaretoken"] = csrftoken
    # gp["next"] = '/'
    # r = client.post(URL, data=gp, headers=dict(Referer=URL))
    #
    return gp
