import sys
sys.path.append('../')
# customs libs 
from ..dataBaseHandler import django_db_Handler,request_Handler
from news.models import World

class France24_scraper:
    """ Scrape data from bbc.com """
    def __init__(self):
        pass
        return None
    
    def start_scraping(self):
        Url = "https://www.france24.com/en/"

        request_obj = request_Handler()
        Response = request_obj.request_soup(Url)

        # check timeout
        if len(Response) is not None:
            title = Response.find_all('p', {'class' : 'article__title'})[0].text
            if World.objects.filter(title = title).exists():
                return None
            else:
                image_src = Response.find_all('div', {'class' : 'm-figure__img-wrapper'} )[0]
                image = image_src.find_all('img')[1]
                
                data = Response.find_all('div', {'class' : 'o-banana-split'})[0]
                link = data.find_all('a')[0]
                link = "https://www.france24.com" + str(link['href'])

                # get publication datetime
                Response = request_obj.request_soup( str(link) )
                dateTime = Response.find_all('time')[0]
                pub_date = str( dateTime['datetime'] )
                pub_date = pub_date.replace("T", " ")[0 : 19] + " Etc/GMT+2"
                
                # saving to db
                db_object = django_db_Handler(
                    table_name = World,
                    Datetime_format="%Y-%m-%d %H:%M:%S Etc/GMT+2",
                    website_name = "france24",
                    webIcon="https://www.france24.com/android-chrome-192x192.png",
                )
                db_object.Save_to_db(

                    news_title = str(title),
                    page_link = link,
                    img_src = str(image['src']),
                    Datetime = str(pub_date),
                        
                    )
        

        


