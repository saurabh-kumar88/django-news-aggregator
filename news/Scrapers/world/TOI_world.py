import sys
sys.path.append('../')
# customs libs 
from ..dataBaseHandler import django_db_Handler, request_Handler
from news.models import World



class TOI_world_scraper:
    """ Scrape data from bbc.com """
    def __init__(self):
        pass
        return None
    
    def start_scraping(self):
        Url = "https://timesofindia.indiatimes.com/world"
        request_obj = request_Handler()
        Response = request_obj.request_soup(Url)
        
        # check timeout
        if len(Response) is not None:
            article = Response.find_all('a', {'class' : 'w_img'} )[0]
            title = article['title']
            if World.objects.filter(title = title).exists():
                return None
            else:
                link = "https://timesofindia.indiatimes.com" + article['href']
                for img in article:
                    image = img['data-src']
                
                # get publication datetime
                Response = request_obj.request_soup(link)
                pub_date = Response.find_all('div', {'class' : '_3Mkg- byline' })[0].text
                
                # saving to db
                db_object = django_db_Handler(
                    table_name = World,
                    Datetime_format="%b %d %Y %H:%M %Z",
                    website_name = "timesOfindia/world",
                    webIcon="https://timesofindia.indiatimes.com/icons/toifavicon.ico",
                )
                db_object.Save_to_db(
                        
                        news_title = str(title),
                        page_link = str(link),
                        img_src = str(image),
                        Datetime = str(pub_date),
                        
                    )
        

            
        
        
        
        
            
        
