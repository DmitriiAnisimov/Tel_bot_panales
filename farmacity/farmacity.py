import sys
import os

# Add the root directory of your project to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

# Now import CustomScraper
from scraper_farmacity import CustomScraperFarmacity

# Specify the target directory
target_directory = 'farmacity/farmacity_data_pampers'
scroll_amount = 500
store = 'Farmacity'
page_count = 1
page_flag = True
url = 'https://www.farmacity.com/bebes/panales'
content_area_css = 'div.vtex-search-result-3-x-gallery'
description_css = 'span.vtex-product-summary-2-x-productBrand'
price_css = 'span.vtex-product-price-1-x-sellingPrice '
price_css_2 = 'span.farmacityar-store-components-1-x-currencyContainer'
link_css = 'a.vtex-product-summary-2-x-clearLink'

# Create an instance of CustomScraper
scraper = CustomScraperFarmacity(target_directory,
                                 scroll_amount,
                                 store,
                                 page_count,
                                 page_flag,
                                 url,
                                 content_area_css,
                                 description_css,
                                 price_css,
                                 link_css,
                                 price_css_2)

# Call the scrape_data method to scrape data
scraper.scrape_data()
