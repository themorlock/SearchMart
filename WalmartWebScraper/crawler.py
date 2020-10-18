from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import queue
import sys

class Crawler:
	def __init__(self, driver, starting_url, max_products):
		self.driver = driver
		self.visited_products = {}
		self.visited_products[''] = ''
		self.visited_products[self.url_to_product(starting_url)] = starting_url
		self.urls_to_visit = queue.Queue()
		self.urls_to_visit.put(starting_url)
		self.max_products = max_products
		self.links = {}
	def url_to_product(self, url):
		s = url.split('/')
		if(len(s) < 5):
			return ""
		try:
			int(s[4])
			return ""
		except:
			return s[4]
	def crawl(self):
		while (len(self.visited_products) < self.max_products and not self.urls_to_visit.empty()):
			try:
				url = self.urls_to_visit.get()
				driver.get(url)
				WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'slider')))
				links = driver.find_elements_by_tag_name('a')
				for a in links:
					link = a.get_attribute('href')
					if link is not None and link.startswith('https://www.walmart.com/ip'):
						product = self.url_to_product(link)
						if product not in self.visited_products:
							my_product_name = self.url_to_product(url)
							if my_product_name not in self.links:
								self.links[my_product_name] = []
							self.links[my_product_name].append(product)
							self.visited_products[product] = link
							self.urls_to_visit.put(link)
			except:
				continue
	def write_crawler_to_file(self, name):
		f_products = open(name + '_products.txt', 'w')
		for key, value in self.visited_products.items():
			f_products.write(key + ' : ')
			f_products.write(value)
			f_products.write('\n')
		f_products.close()
		f_links = open(name + '_links.txt', 'w')
		for key, value in self.links.items():
			f_links.write(key + ' : ')
			f_links.write(str(value))
			f_links.write('\n')
		f_links.close()

if __name__ == '__main__':
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	prefs = {"profile.managed_default_content_settings.images": 2}
	chrome_options.add_experimental_option("prefs", prefs)
	driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe', options=chrome_options)
	starting_url = sys.argv[1]#'https://www.walmart.com/ip/SAMSUNG-Galaxy-Watch-Bluetooth-Smart-Watch-46mm-Silver-SM-R800NZSAXAR/163601874'#'https://www.walmart.com/ip/JVC-55-Class-4K-UHD-2160p-HDR-Roku-Smart-LED-TV-LT-55MAW595/832008708?athcpid=832008708&athpgid=athenaItemPage&athcgid=null&athznid=PWBAB&athieid=v0&athstid=CS004&athguid=c19a78b4-007-175383592e96b3&athancid=null&athena=true'
	max_products = int(sys.argv[2])
	walmart_crawler = Crawler(driver, starting_url, max_products)
	walmart_crawler.crawl()
	walmart_crawler.write_crawler_to_file(sys.argv[3])
	print(len(walmart_crawler.visited_products))
	for product in walmart_crawler.visited_products:
		print(product)
	driver.quit()
