import sys
sys.path.append('../')
# customs libs 
from ..dataBaseHandler import django_db_Handler, request_Handler
from news.models import Tech_news


class Hindustantimes_tech_scraper:
    """ Scrape data from hindustantimes.com """
    def __init__(self):
        pass
        return None
    
    def start_scraping(self, news_count):
        self.news_count = news_count
        for i in range( news_count ):
            Url = "https://www.hindustantimes.com/tech/"
            request_obj = request_Handler()
            Response = request_obj.request_xml(Url)
            if len(Response) is not None:
                title = Response.xpath('//div[@class="media-heading headingfour"]/a/@title')[i]
                
                title = Response.xpath('//div[@class="media-heading headingfour"]/a/@title')[i]
                if Tech_news.objects.filter(title = title).exists():
                    pass
                else:
                    link = Response.xpath('//div[@class="media-heading headingfour"]/a/@href')[i]
                    image = Response.xpath('//div[@class="media-left"]/a/img/@src')[i] 
                    # Get news posting date
                    pub_date = Response.xpath('//span[@class="time-dt"]/text()')[i]
                    # saving to db
                    db_object = django_db_Handler(
                        table_name = Tech_news,
                        Datetime_format="%b %d %Y %H:%M",
                        website_name = "hindustantimes",
                        webIcon="https://www.hindustantimes.com/favicon.ico",
                    )
                    db_object.Save_to_db(
                                
                                news_title = str(title),
                                page_link = str(link),
                                img_src = str(image),
                                Datetime = str(pub_date),
                                
                            )
            
            
            
                    

            
        




    
