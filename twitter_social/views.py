from django.shortcuts import render, redirect
from .tweepy import tweet_scrap
from .data_share import parameter_send, parameter_get
from .macro import background_posting
from users.models import Users

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
    search_words = ["#krishian_1_0_0"]
    tweet_info = tweet_scrap(search_words)
    for tweet in tweet_info:
        if tweet["id"] == pk:
            gp = parameter_get(tweet["text"])
            break
    if gp:
        print(gp)
    return redirect('twitter-post')


def TwitterBackground(request):
    background_posting()
    return redirect('twitter-share')
