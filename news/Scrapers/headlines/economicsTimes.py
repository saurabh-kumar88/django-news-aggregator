import sys
sys.path.append('../')
# customs libs 
from ..dataBaseHandler import django_db_Handler, request_Handler
from news.models import Headlines

class EconomicsTimes_scraper:
    """ Scrape data from economicstimes.indiatimes.com """
    def __init__(self):
        pass
        return None
    
    def start_scraping(self):
        Url = "https://economictimes.indiatimes.com"
        request_obj = request_Handler()
        Response = request_obj.request_xml(Url)
        if len(Response) is not None:
            title = request_obj.dataCleaner( Response.xpath('//*[@id="pageContent"]/div[1]/hgroup/h1/a/text()') )
            news_headline = Headlines()
            if Headlines.objects.filter(title = title).exists():
                return None
            else:
                link = request_obj.dataCleaner( Response.xpath('//*[@id="pageContent"]/div[1]/hgroup/h1/a/@href') )
                link = Url + str(link)
                image = Response.xpath('//*[@id="pageContent"]/div[1]/hgroup/h1/a/img/@src') 
            
                # Get news posting date
                Response = request_obj.request_xml(Url)
                date = request_obj.dataCleaner(Response.xpath('//*[@class="clearfix publish_info"]/div[2]/text()')) 
                
                # saving to db
                db_object = django_db_Handler(
                    table_name = Headlines,
                    Datetime_format="%b %d %Y %I.%M %p %Z",
                    website_name = "economicsTimes",
                    webIcon="https://economictimes.indiatimes.com/icons/etfavicon.ico",

                )
                db_object.Save_to_db(
                            
                            news_title = str(title),
                            page_link = str(link),
                            img_src = str(image[0]),
                            Datetime = str(date),
                            
                        )
        
        
        

            
        
