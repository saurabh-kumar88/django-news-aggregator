import sys
sys.path.append('../')

from news.models import Headlines
# customs libs 
from ..dataBaseHandler import django_db_Handler, request_Handler

class DeccanHarald_scraper:
    """ Scrape data from economicstimes.indiatimes.com """
    def __init__(self):
        pass
        return None
    
    def start_scraping(self):
        Url = "https://www.deccanherald.com"
        request_obj = request_Handler()
        Response = request_obj.request_xml(Url)
        
        # Check for timeout
        if len(Response) is not None:
            title = request_obj.dataCleaner( 
                Response.xpath('//*[@class="image-overlay-text relative-main full-height"]/div/h1/text()')
                )
            
            news_headline = Headlines()
        
            if Headlines.objects.filter(title = title).exists():
                return None
            else:
                link = request_obj.dataCleaner( 
                    Response.xpath('//*[@class=" fc_topstory blue"]/div/div/a/@href')
                    )
                link = Url + str(link)
                image = Url + str(Response.xpath('//*[@id="home-top-stories"]/div/div/div[1]/div[1]/a/div/img[1]/@src')[0] )
                
                # Get news posting date
                Response = request_obj.request_xml(link)
                date = Response.xpath('//meta[@property="og:updated_time"]/@content')[0]
                # processing & formating publication date
                date2 = date.replace( "T", " " )
                date3 = date2.replace( date2[19 : len(date2)], " IST")
            
                # saving to db
                db_object = django_db_Handler(
                    table_name = Headlines,
                    Datetime_format="%Y-%m-%d %H:%M:%S %Z",
                    website_name = "deccanherald",
                    webIcon="https://www.deccanherald.com/sites/dh/files/png-32X32.png",
                )

                db_object.Save_to_db(        
                            news_title = title,
                            page_link = link,
                            img_src = image,
                            Datetime = date3.strip(),
                            
                        )
         

        
                
                
            
        
