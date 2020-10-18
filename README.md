# SearchMart
SearchEngine for scraped pages from walmart.com

Contains the webscraper used to scrape data from walmart.com and the scraped dataset. Each '_products.txt' file contains unique products in that category and the '_links.txt' file holds the links between different products. The 'all_products.txt' and 'all_links.txt' files contain all the unique products and all their unique links. In total we had 21,532 unique products.

To run the web scraper, you need to provide three command-line arguments: the url where it should start scraping, the max number of products it should crawl to, and the name of the department you are scraping.

All required modules must be in their standard versions except you must install scikit-learn version 0.22.2.post1 (pip install -Iv scikit-learn==0.22.2.post1)

To use the server for the backend, run an Apache server with index.html in ServerPython/, and also run the apy.py REST API in RestAPI/.

Link to our machine learning models are [here.](https://drive.google.com/drive/folders/1Hu-wNzY6c8lyhliRmRrNSQZultWkoaM4?usp=sharing) To load them into our server, make sure they are in a folder titled 'MachineLearningModels' that is one directory above the directory the server is in.
