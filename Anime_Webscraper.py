import scrapy
from scrapy.crawler import CrawlerProcess



#Defining Variables
class AnimeItem(scrapy.Item):
    Position = scrapy.Field()
    Title = scrapy.Field()
    Score = scrapy.Field()
    Year = scrapy.Field()


# This class create the name of the project, then uses the url provided
class AnimeSpider(scrapy.Spider):
    name = 'anime_spider'
    start_urls = ['https://myanimelist.net/topanime.php']


    """This function uses a for loop that iterates through the data provided
    and creates a list with the position, title, score, and the year provided
    """
    def parse(self, response):
        for ranking, anime in enumerate(response.css('tr.ranking-list')):
            position = ranking + 1
            title = anime.css('div.di-ib h3 a::text').get()
            score = anime.css('span.score::text').get()
            year = anime.css('div.information span::text').re_first(r'\((\d{4})\)')


            item = AnimeItem()
            item['Position'] = position
            item['Title'] = title
            item['Score'] = score
            item['Year'] = year


            yield item


#This is how you call and use the program
process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'anime_data.json'
})
#This calls the program
process.crawl(AnimeSpider)
process.start()
