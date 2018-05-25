import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from codeBud.items import CodeBudItem

class codebuddyScraper(CrawlSpider):
	name = "my_scraper"
	allowed_domains = ['codebuddy.co.in',]
	start_urls = ['https://codebuddy.co.in/ranks/practice',]

	def parse(self,response):
		user_links = response.css("td a::attr(href)").extract()
		for a in user_links:
			#print(a)
			yield scrapy.Request('https://codebuddy.co.in'+a, callback = self.parse_detail_page)

	def parse_detail_page(self,response):
		item = CodeBudItem()
		user_name = response.css("h3::text").extract()[0].strip()
		handle_name = response.css("h4::text").extract()[0].strip()
		item['user_name'] = user_name
		item['handle_name'] = handle_name
		yield item

	#rules = (
     #   Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
      #       callback="parse_item",
       #      follow=False),)

 

			
