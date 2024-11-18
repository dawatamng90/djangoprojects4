from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,'testapp/index.html')

def movies_info(request):
    head_msg = 'Movies Information'
    sub_msg1 = 'Jailer was super hit'
    sub_msg2 = 'Planning for Aashiqui - 3'
    sub_msg3 = "Don't go for movies, practice Django"
    type = 'movies'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def sports_info(request):
    head_msg = 'Sports Information'
    sub_msg1 = 'Barcelona’s Fati sidelined with hamstring injury'
    sub_msg2 = 'SL vs NZ 1st ODI: Mendis, Fernando tons earn Sri Lanka comfortable win in rain-hit match'
    sub_msg3 = "Abdusattorov moves into the sole lead; Praggnanandhaa, Nihal hold Carlsen"
    type = 'sports'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def politics_info(request):
    head_msg = 'Politics Information'
    sub_msg1 = 'Trump’s defence choice stuns the Pentagon and raises questions about the Fox News host’s experience'
    sub_msg2 = 'Sri Lankans vote in parliamentary election'
    sub_msg3 = "Guardian quits Elon Musk-owned X, citing racism and conspiracy theories"
    type = 'politics'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)