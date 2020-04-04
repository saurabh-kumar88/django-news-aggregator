import sys
import time
sys.path.append('../')

from django.shortcuts import render, redirect
from news.models import Headlines, World, Tech_news, Economy, Sports
from datetime import datetime

from .Scrapers.dateTime_logic import Get_DateTime

#_______________________ Top headlines __________________________________
from .Scrapers.headlines.timesOfindia import TimesOfindia_scraper
from .Scrapers.headlines.hindustanTimes import Hindustantimes_scraper
from .Scrapers.headlines.indianXpress import IndianXpress_scraper
from .Scrapers.headlines.economicsTimes import EconomicsTimes_scraper
from .Scrapers.headlines.deccanherald import DeccanHarald_scraper

#_______________________ World ___________________________________
from .Scrapers.world.france24_world import France24_scraper
from .Scrapers.world.TOI_world import TOI_world_scraper
from .Scrapers.world.indianXpress_world import IndianXpress_world_scraper

#______________________ Tech world ___________________________________
from .Scrapers.tech_news.hindustantimes_tech import Hindustantimes_tech_scraper

#______________________ Economy ____________________________________
from .Scrapers.economy.thePrint import thePrint_scraper

#______________________ Sports ______________________________________
from .Scrapers.sports.theHindu import The_Hindu_scraper


def run_scrapers():
    """
    Combine all scrapers category-wise into one method
    """

#_______________TOP STORIES________________________________    
    deccanherald = DeccanHarald_scraper()
    deccanherald.start_scraping()
    
    economicstimes = EconomicsTimes_scraper()
    economicstimes.start_scraping()

    hidustantimes = Hindustantimes_scraper()
    hidustantimes.start_scraping()

    indianxpress = IndianXpress_scraper()
    indianxpress.start_scraping()

    #times_of_india = TimesOfindia_scraper()
    #times_of_india.start_scraping()
#____________________TECH_________________________________
    
    hindustantimes_tech = Hindustantimes_tech_scraper()
    hindustantimes_tech.start_scraping(news_count=4)

#______________________WORLD________________________________
    France24 = France24_scraper()
    France24.start_scraping()

    indianxpress_world = IndianXpress_world_scraper()
    indianxpress_world.start_scraping(news_count = 4 )

    times_of_india_world = TOI_world_scraper()
    times_of_india_world.start_scraping() 
    

#___________________ECONOMY______________________________

    the_print = thePrint_scraper()
    the_print.start_scraping(news_count=4)


#__________________SPORTS________________________________

    the_hindu = The_Hindu_scraper()
    the_hindu.start_scraping(news_count = 4)


    return None

def scrape(request):
    """
    run all scrapers sequentially here, and reloads to home page
    """
    run_scrapers()
    
    return redirect("../")


class TempNews:
    """ 
    Temporary class to hold news objects for django context processor.
    ...

    Methods
    -------
    __init__()
        Holds nothing, news objects
    """
    def __init__(self,id, title, url, image, time_Stamp,timeDiff, websiteIcon, website_name):
        self.id = id
        self.title = title
        self.url = url
        self.image = image
        self.time_Stamp = time_Stamp    
        self.timeDiff = timeDiff
        self.website_name = website_name
        self.websiteIcon = websiteIcon
    

class News_sorting_and_listing:
    
    def __init__(self):
        """ 
        This class sorts news on the basis of how older a news is
        News posts which have lower time diff will be diplayed at top.
        ...

        Methods
        -------
        __init__()
            Holds nothing, reserved for future use
        Return
        ------
        None

        Sorting()
            First retrive news posts saved in database and then sorts them 
            according to time difference between publication and current time. 
        """
        pass
        return None   

    def Sorting(self, TableName):
        """ 
        First retrive news posts saved in database and then sorts them 
        according to time difference between publication and current time.

        Parameters
        ----------
        TableName : django models class name
            table's class name
        
        Return value
        ------------
        SortedNews : list
		A list of news objects sorted according there time delta
        newer post at the top
        
        Rule
        ----
        This method also take cares of news which are more then 2 days 
        older, and if found any, it deletes them from database
        which prevent database overfilling and maintains speed of db search

        """
        self.TableName = TableName
        headlines = TableName.objects.all()[::-1]
        
        SortedNews = []
        List =[]
        date_obj = Get_DateTime()
        for news in headlines:
            time_Stamp = datetime.strptime(news.timeStamp, "%Y-%m-%d %H:%M:%S")
            
            #------------testcode---------
            diff = date_obj.Get_Time_Diff(time_Stamp)
            # remove news which are more then 2 days older
            if ("days" in diff) and (int(diff[0]) > 2):
                instance = TableName.objects.filter(id=news.id)
                instance.delete()
            else:
                obj = TempNews( 
                    id=news.id,title=news.title, 
                    url=news.url,image=news.image, 
                    time_Stamp=time_Stamp,timeDiff=diff,
                    website_name=news.website_name, 
                    websiteIcon=news.websiteIcon
                    )
            
                List.append(obj)
        # Re-arranging news list according time stamp(latest news first)
        # list of class objects have been sorted by its attribute(time_Stamp)
        SortedNews = sorted(List, key=lambda x: x.time_Stamp, reverse=True)
    
        return SortedNews

def news_list(request):

    """ Fetch news from database and render them to template

    Parameters
    ----------
    None
    
    Return value
    ------------
    renders home.html

    """

    # Fetching all news from table into a list
    headlines = Headlines.objects.all()[::-1]
    world_news = World.objects.all()[::-1]
    tech_news = Tech_news.objects.all()[::-1]
    economic_news = Economy.objects.all()[::-1]
    sports_news = Sports.objects.all()[::-1]
    
    obj = News_sorting_and_listing()
    # getting list of sorted posts
    headlines_dic = obj.Sorting(Headlines)
    world_dic = obj.Sorting(World)
    tech_dic = obj.Sorting(Tech_news)
    economic_dic = obj.Sorting(Economy)
    sports_dic = obj.Sorting(Sports)

    # django context,  { "key" : list of sorted posts }
    context = {
        'headlines_dic' : headlines_dic,
        'world_dic' : world_dic,
        'tech_dic'  : tech_dic,
        'economic_dic' : economic_dic,
        'sports_dic'   : sports_dic,
        }
    
    
    return render(request, "news/home.html", context=context)


def about(request):
    books = [
        {
            "title"  : "The time machine",
            "Author" : "H.G wells",
            "Pulication" : "1895",
        }
    ]
    context = {
        'books' : books,
    }
    return render(request,'news/about.html', context=context)

def homepage(request):
    return render(request,'news/homepage.html')
