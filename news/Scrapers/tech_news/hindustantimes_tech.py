import sys
sys.path.append('../')
# customs libs 
from ..dataBaseHandler import django_db_Handler, request_Handler
from news.models import Tech_news

import copy

class Hindustantimes_tech_scraper:
    """ Scrape data from hindustantimes.com """
    def __init__(self):
        pass
        return None
    
    def start_scraping(self):
        
        Url = "https://www.hindustantimes.com/tech/"
        request_obj = request_Handler()
        Response = request_obj.request_xml(Url)
        links = Response.xpath('//article[@class="post-list-small__entry"]/a/@href')
        
        Data = []
        temp_dic = {}

        if len(links):
            for link in links:
                
                Response = request_obj.request_xml("https://tech.hindustantimes.com" + str(link))
                
                title = Response.xpath('//title/text()')[0]
                dateTime = Response.xpath('//meta[@name="Last-Modified"]/@content')[0]
                image = Response.xpath('//meta[@property="og:image"]/@content')[0]
                
                temp_dic['title'] = str(title).strip()
                temp_dic['link'] = str("https://tech.hindustantimes.com" + link)
                temp_dic['dateTime'] = (str(str(dateTime).strip()).replace("T", " ")).replace("+05:30", "")
                temp_dic['image'] = str(image).strip()

                x = copy.copy(temp_dic)
                Data.append(x)
        
            # saving to db
            for news in Data:
                db_object = django_db_Handler(
                    table_name = Tech_news,
                    Datetime_format="%Y-%m-%d %H:%M:%S",
                    website_name = "hindustantimes",
                    webIcon="https://www.hindustantimes.com/favicon.ico",
                )
                db_object.Save_to_db(
                            
                            news_title = news['title'],
                            page_link = news['link'],
                            img_src = news['image'],
                            Datetime = news['dateTime'],
                            
                        )
        
        
                
