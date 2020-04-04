import sys
sys.path.append('../')
# customs libs 
from ..dataBaseHandler import django_db_Handler, request_Handler
from news.models import Headlines

class TimesOfindia_scraper:
    """ Scrape data from timesofindia.indiatimes.com """
    def __init__(self):
        pass
        return None
    
    def start_scraping(self):
        Url = "https://timesofindia.indiatimes.com"
        request_obj = request_Handler()
        Response = request_obj.request_xml(Url)
        
        if len(Response) is not None:
            title = request_obj.dataCleaner( 
                Response.xpath('//*[@id="featuredstory"]/h2/a/@title') 
                )
            news_headline = Headlines()
            if Headlines.objects.filter(title = title).exists():
                return None
            else:
                link = request_obj.dataCleaner( 
                    Response.xpath('//*[@id="featuredstory"]/h2/a/@href')
                    )
                link = Url + str(link)
                image = Response.xpath('//*[@id="featuredstory"]/a/img/@src')[0]
                 
                # Get news posting date
                Response = request_obj.request_xml(link)
                date = request_obj.dataCleaner(
                    Response.xpath('//div[1][@class="_3Mkg- byline"]/text()')
                    ) 
                
                # saving to db
                db_object = django_db_Handler(
                    table_name = Headlines,
                    Datetime_format="%b %d %Y %H:%M %Z",
                    website_name = "timesofIndia",
                    webIcon="https://timesofindia.indiatimes.com/icons/toifavicon.ico",

                )
                db_object.Save_to_db(

                            news_title = str(title),
                            page_link = str(link),
                            #img_src = str(image[ 2 : len(image) - 2]),
                            img_src = str(image),
                            Datetime = str(date),
                            
                        )
         

            
        


