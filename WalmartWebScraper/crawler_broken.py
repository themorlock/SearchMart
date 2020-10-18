
import requests
from bs4 import BeautifulSoup
import queue

class Product:
	def __init__(self, url, title, rating, price, categories):
		self.url = url
		self.title = title
		self.rating = rating
		self.price = price
		self.categories = categories




'''
from scrapy.item import Item, Field

class SitegraphItem(Item):
	 url = Field()
	 #title = Field()
	 #rating = Field()
	 #price = Field()
	 #categories = Field()
	 #brand = Field()
	 children = Field()


from scrapy.selector import Selector	
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.utils.url import urljoin_rfc

class GraphspiderSpider(CrawlSpider):
	name = 'walmartcrawler'
	#allowed_domains = ['www.walmart.com/cp/electronics']
	start_urls = ['walmart.com']

	rules = (
		Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True),
	)

	def parse_item(self, response):
		hxs = HtmlXPathSelector(response)
		i = SitegraphItem()
		i['url'] = response.url
		llinks=[]
		for anchor in hxs.select('//a[@href]'):
			href=anchor.select('@href').extract()[0]
			if not href.lower().startswith("javascript"):
				llinks.append(urljoin_rfc(response.url,href))
		i['children'] = llinks
		return i

'''

'''
class Crawler:
	products = []
	def __init__(self, starting_urls, max_products):
		self.urls_to_visit = queue.Queue()
		[self.urls_to_visit.put(starting_url) for starting_url in starting_urls]
	def crawl(self):
		while(len(self.products) < max_products and not self.urls_to_visit.empty()):
			try:
				url = self.urls_to_visit.get()
				page = requests.get(url)
				soup = BeautifulSoup(page.content, 'html.parser')
				page_url = page.url
				#print(page_url)
				title = soup.title.text
				rating = soup.find('span', itemprop='ratingValue').text
				price = soup.find('span', class_='price-characteristic').text
				categories = soup.find_all('span', itemprop='name')
				for i in range(len(categories)):
					categories[i] = categories[i].text
				self.products.append(Product(page_url, title, rating, price, categories))
			except:
				continue

			for item in soup.findAll('a', href=True):
				child_url = item['href']
				if child_url != page.url and 'walmart.com' in child_url:
					self.urls_to_visit.put(child_url)

if __name__ == '__main__':
	starting_urls = ['https://www.walmart.com/ip/SAMSUNG-Galaxy-Watch-Bluetooth-Smart-Watch-46mm-Silver-SM-R800NZSAXAR/163601874']
	max_products = 10
	walmart_crawler = Crawler(starting_urls, max_products)
	walmart_crawler.crawl()
	print(len(walmart_crawler.products))
	for i in range(len(walmart_crawler.products)):
		print(walmart_crawler.products[i].url)
		print(walmart_crawler.products[i].title)
		print(walmart_crawler.products[i].rating)
		print(walmart_crawler.products[i].price)
		print(walmart_crawler.products[i].categories)
'''
#page = requests.get('https://wrd.walmart.com/track?rd=https%3A%2F%2Fwww.walmart.com%2Fip%2FLG-65-Class-4K-UHD-2160P-Smart-TV-65UN6950ZUA-2020-Model%2F195775096%3FfindingMethod%3Dwpa&rdf=1&wpa_qs=laxa9q2z57wdicoBI2fNj8QLPonJ1-jmZdV7qlMBImX871bC83y0AHxF1eql4__nykf4x1Mowi4LI3qE8UXCTFUS7HTNphevgd1zNM6gK-r9tHKu2A5yS1h1465nz1bX0oa7ym6gf6stKxr1Bj8mWndrirLYvYK5maT2La4qYFzqClnVKnLyMnnEpoFXloKf&cmp=1369580&storeId=4216&adUid=76c6744b-6b23-4190-89f9-13cd50b99d39&pt=ip&mLoc=top&tgtp=0&bt=1&slr=F55CDC31AB754BB68FE0B39041159D63&pgid=316226539&itemId=195775096&relRank=0&pltfm=desktop&relUUID=eb91c839-6592-4f59-b577-befedc10b804&isSlr=false&adpgm=wpa&tn=WMT&requestUUID=eb91c839-6592-4f59-b577-befedc10b804&adgrp=419596&bkt=1674&plmt=__plmt__&tax=3944_1060825_447913&ver=2')
#print(page.url)
