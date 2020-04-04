import sys
sys.path.append('../')
# customs libs 
from ..dataBaseHandler import django_db_Handler, request_Handler
from news.models import Economy



class thePrint_scraper:
    """ Scrape data from bbc.com """
    def __init__(self):
        pass
        return None
    
    def start_scraping(self, news_count):
        Url = "https://theprint.in/category/economy/"
        request_obj = request_Handler()
        for i in range(news_count):
            Response = request_obj.request_xml(Url)
            # check timeout
            if len(Response) is not None:
                title = Response.xpath('//h3[@class="entry-title td-module-title"]/a/@title')[i]
                
                if Economy.objects.filter(title = title).exists():
                    return None
                else:
                    link = Response.xpath('//h3[@class="entry-title td-module-title"]/a/@href')[i]
                    # Get Image and pub_date  
                    Response = request_obj.request_xml(link)
                    image = Response.xpath('//div[@class="td-post-featured-image"]/figure/img/@src')[0]
                    date = Response.xpath('//span[@class="update_date"]/text()')[0]
                    # Cleaning punlication date
                    s1 = ( ( date.strip() ).replace(",", "") ).split(" ") 
                    s1[0], s1[1] = s1[1], s1[0]
                    pub_date = ""
                    for i in s1:
                        pub_date += i + " "
                    
                    # saving to db
                    
                    db_object = django_db_Handler( 
                        table_name = Economy,
                        Datetime_format="%B %d %Y %I:%M %p %Z",
                        website_name = "thePrint",
                        webIcon="https://d2c7ipcroan06u.cloudfront.net/wp-content/uploads/2018/03/152x152.png",
                         )
                    
                    db_object.Save_to_db(
                            
                            news_title = str(title),
                            page_link = str(link),
                            img_src = str(image),
                            Datetime = str( pub_date.strip() ),
                        )
                                                                             
            
        

        
    