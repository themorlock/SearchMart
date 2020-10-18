'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import queue

class Product:
	def __init__(self, url, title, rating, price, categories):
		self.url = url
		self.title = title
		self.rating = rating
		self.price = price
		self.categories = categories

class Crawler:
	products = []
	visited_urls = set()
	def __init__(self, driver, starting_urls, max_products):
		self.driver = driver
		self.urls_to_visit = queue.Queue()
		[self.urls_to_visit.put(starting_url) for starting_url in starting_urls]
		[self.visited_urls.add(starting_url) for starting_url in starting_urls]
		self.max_products = max_products
	def crawl(self):
		while(len(self.products) < self.max_products and not self.urls_to_visit.empty()):
			try:
				url = self.urls_to_visit.get()
				driver.get(url)
				title = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="product-overview"]/div/div[3]/div/h1'))).text
				rating = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div[5]/div/div[3]/div/div[1]/div[4]/div[1]/div/div/button/span/span[1]').text
				price = driver.find_element_by_class_name('price-characteristic').text
				categories = driver.find_element_by_class_name('breadcrumb-list').text.split('/')
				#print(price, rating, title, categories)
				p = Product(url, title, rating, price, categories)
				self.products.append(p)
				links = driver.find_elements_by_tag_name('a')
				for a in links:
					link = a.get_attribute('href')
					if link is not None and (link not in self.visited_urls) and link.startswith('https://www.walmart.com/ip'):
						print(link)
						self.visited_urls.add(link)
						self.urls_to_visit.put(link)
			except:
				continue

if __name__ == '__main__':
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	prefs = {"profile.managed_default_content_settings.images": 2}
	chrome_options.add_experimental_option("prefs", prefs)
	driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe', options=chrome_options)
	starting_urls = ['https://www.walmart.com/ip/JVC-55-Class-4K-UHD-2160p-HDR-Roku-Smart-LED-TV-LT-55MAW595/832008708?athcpid=832008708&athpgid=athenaItemPage&athcgid=null&athznid=PWBAB&athieid=v0&athstid=CS004&athguid=c19a78b4-007-175383592e96b3&athancid=null&athena=true', 'https://www.walmart.com/ip/JVC-55-Class-4K-UHD-2160p-HDR-Roku-Smart-LED-TV-LT-55MAW595/832008708?athcpid=832008708&athpgid=athenaItemPage&athcgid=null&athznid=PWBAB&athieid=v0&athstid=CS004&athguid=c19a78b4-007-175383592e96b3&athancid=null&athena=true', 'https://www.walmart.com/ip/JVC-55-Class-4K-UHD-2160p-HDR-Roku-Smart-LED-TV-LT-55MAW595/832008708?athcpid=832008708&athpgid=athenaItemPage&athcgid=null&athznid=PWBAB&athieid=v0&athstid=CS004&athguid=c19a78b4-007-175383592e96b3&athancid=null&athena=true', 'https://www.walmart.com/ip/JVC-55-Class-4K-UHD-2160p-HDR-Roku-Smart-LED-TV-LT-55MAW595/832008708?athcpid=832008708&athpgid=athenaItemPage&athcgid=null&athznid=PWBAB&athieid=v0&athstid=CS004&athguid=c19a78b4-007-175383592e96b3&athancid=null&athena=true', 'https://www.walmart.com/ip/JVC-55-Class-4K-UHD-2160p-HDR-Roku-Smart-LED-TV-LT-55MAW595/832008708?athcpid=832008708&athpgid=athenaItemPage&athcgid=null&athznid=PWBAB&athieid=v0&athstid=CS004&athguid=c19a78b4-007-175383592e96b3&athancid=null&athena=true']
	max_products = 5
	crawler = Crawler(driver, starting_urls, max_products)
	crawler.crawl()
	print(len(crawler.visited_urls))
	for product in crawler.visited_urls:
		print(product)
	driver.quit()
'''