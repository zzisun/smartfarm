from django.shortcuts import render, redirect
from .tweepy import tweet_scrap
from .data_share import parameter_send, parameter_get
from .macro import background_posting
from users.models import Users
from device_management.models import Device_Info, Farm_Info
from device_management.forms import Growth_Params_Form

def TwitterShare(request):
    # category를 나눌 수 있음
    user = Users.objects.get(email=request.user.email)
    content = {'user' : user}
    return render(request, 'twitter_share.html', content)

def TwitterPost(request):
    search_words = ["#krishian_1_0_0"]
    category = request.GET.get('category', None)
    if category is not None:
        search_words.append('#'+category)
    tweet_info = tweet_scrap(search_words)
    data_text = parameter_send()
    content = {
        "tweet_info": tweet_info,
        "data_text": data_text,
    }
    return render(request, 'twitter_post.html', content)

def TwitterGet(request, pk):
    #Get Farm Info and Choose Farm
    user = request.user
    try:
        device_info = Device_Info.objects.filter(device_user=user)[0]
    except:
        return redirect('device_management:device1')
    print(device_info)
    farm_list = Farm_Info.objects.filter(device_info=device_info)

    search_words = ["#krishian_1_0_0"]
    tweet_info = tweet_scrap(search_words)
    for tweet in tweet_info:
        if tweet["id"] == pk:
            gp = parameter_get(tweet["text"])
            break
    if gp:
        print(gp)
    return render(request, 'twitter_http_post.html', {'gp': gp,
                                                      'farm_list': farm_list})

def TwitterBackground(request):
    background_posting()
    return redirect('twitter-share')
