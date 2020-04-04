import sys
sys.path.append('../')
# customs libs 
from ..dataBaseHandler import django_db_Handler, request_Handler
from news.models import Sports


class The_Hindu_scraper:
    """ Scrape data from thehindu.com """
    def __init__(self):
        pass
        return None
    
    def start_scraping(self, news_count):
        self.news_count = news_count
        
        for i in range(news_count):
            Url = "https://www.thehindu.com/sport/"
            request_obj = request_Handler()
            Response = request_obj.request_xml(Url)
            if len(Response) is not None:
                title = request_obj.dataCleaner( 
                    Response.xpath('//a[@class="story-thumb66-text"]/text()')[i]
                    )
                news_headline = Sports()
                if Sports.objects.filter(title = title).exists():
                    pass
                else:
                    link = request_obj.dataCleaner(
                        Response.xpath('//a[@class="story-thumb66-text"]/@href')[i]
                        )               
                    
                    # Get Image and publication date
                    Response = request_obj.request_xml(link)
                    image = Response.xpath('//*[@class="img-container picture"]/picture/source/@srcset')[0]
                    date = request_obj.dataCleaner( 
                        Response.xpath('//meta[@name="publish-date"]/@content')[0]
                        )
                    # Cleaning and re-arranging publication date
                    date2 = date.replace( "T", " " )
                    date3 = date2.replace( date2[19 : len(date2)], " IST")
                    
                    # saving to db
                    db_object = django_db_Handler(
                        table_name = Sports,
                        Datetime_format="%Y-%m-%d %H:%M:%S %Z",
                        website_name = "theHindu",
                        webIcon="https://www.thehindu.com/thfavicon.ico",
                    )
                    db_object.Save_to_db(
                                
                                news_title = str(title),
                                page_link = str(link),
                                img_src = str(image),
                                Datetime = str(date3),
                                
                            )
         

            
        
