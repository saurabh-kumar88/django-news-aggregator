from django.urls import path
from news.views import scrape, news_list, about, homepage 

urlpatterns = [
    path('scrape/', scrape, name="scrape"),
    path('', news_list, name="home"),
    path('about/',about,name="about"),
    path('homepage/',homepage, name="homepage"),
    

    #path('latestfeeds/', LatestEntriesFeed()),
]