import sys
import os

# Add the root directory of your project to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

# Now import CustomScraper
from scraper import CustomScraper

# Specify the target directory
target_directory = 'carrefour/carrefour_data_pampers'
scroll_amount = 500
store = 'Carrefour'
page_count = 6
url = 'https://www.carrefour.com.ar/Mundo-Bebe/Panales?page='
content_area_css = 'vtex-flex-layout-0-x-flexColChild pb0'
description_css = 'span.vtex-product-summary-2-x-productBrand'
price_css = 'span.valtech-carrefourar-product-price-0-x-sellingPrice'
link_css = 'a.vtex-product-summary-2-x-clearLink'

# Create an instance of CustomScraper
scraper = CustomScraper(target_directory,
                        scroll_amount,
                        store,
                        page_count,
                        False,
                        url,
                        None,
                        description_css,
                        price_css,
                        link_css)

# Call the scrape_data method to scrape data
scraper.scrape_data()
