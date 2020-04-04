import sys
sys.path.append('../')
# customs libs 
from ..dataBaseHandler import django_db_Handler, request_Handler
from news.models import World


class IndianXpress_world_scraper:
    """ Scrape world news from indianxpress/world.com """
    def __init__(self):
        pass
        return None
    
    def start_scraping(self, news_count):
        self.news_count = news_count
        
        for i in range( news_count ):
            Url = "https://indianexpress.com/section/world/"
            request_obj = request_Handler()
            Response = request_obj.request_xml(Url)    
            if len(Response) is not None:
                title = Response.xpath('//div[@class="articles"]/h2/a/text()')[i]
                if World.objects.filter(title = title).exists():
                    pass
                else:
                    link = Response.xpath('//div[@class="articles"]/h2/a/@href')[i]
                    pub_date = Response.xpath('//div[@class="articles"]/div[@class="date"]/text()')[i]
                    # get image
                    Response = request_obj.request_xml(link)
                    image = Response.xpath('//meta[@property="og:image"]/@content')[0] 
                    
                    # saving to db         
                    db_object = django_db_Handler(
                        table_name = World,
                        Datetime_format="%B %d %Y %I:%M:%S %p",
                        website_name = "indianXpress-world",
                        webIcon="https://images.indianexpress.com/2018/10/fav-icon.png?w=32",
                    )
                    db_object.Save_to_db(
                                    
                                    news_title = str(title),
                                    page_link = str(link),
                                    img_src = str(image),
                                    Datetime = str(pub_date),
                                    
                                )
                                
                
                
                    

            
        




    
