import sys
sys.path.append('../')
# customs libs 
from ..dataBaseHandler import django_db_Handler, request_Handler
from news.models import Headlines



class IndianXpress_scraper:
    """ Scrape data from indianxpress.com """
    def __init__(self):
        pass
        return None
    
    def start_scraping(self):
        Url = "https://indianexpress.com"
        request_obj = request_Handler()
        Response = request_obj.request_xml(Url)
    
        if len(Response) is not None:
            title = request_obj.dataCleaner( 
                Response.xpath('//div[@class="ie-first-story"]/h1/a/text()')
                )
            news_headline = Headlines()
            if Headlines.objects.filter(title = title).exists():
                return None
            else:
                link = request_obj.dataCleaner( 
                    Response.xpath('//div[@class="ie-first-story"]/h1/a/@href')
                    )
                image = Response.xpath('//*[@class="lead-img"]/a/img/@src') 
                # Get news posting date
                Response = request_obj.request_xml(link)
                date = request_obj.dataCleaner(
                    Response.xpath('//*[@id="storycenterbyline"]/span/text()')
                    ) 

                # saving to db
                db_object = django_db_Handler(
                    table_name = Headlines,
                    Datetime_format="%B %d %Y %I:%M:%S %p",
                    website_name = "indianXpress",
                    webIcon="https://images.indianexpress.com/2018/10/fav-icon.png?w=32",
                )
                db_object.Save_to_db(
                            
                            news_title = str(title),
                            page_link = str(link),
                            img_src = "https:" + str(image[0]),
                            Datetime = str(date),
                            
                        )
          

            
        


