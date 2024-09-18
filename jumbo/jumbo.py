import sys
import os

# Add the root directory of your project to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

# Now import CustomScraper
from scraper import CustomScraper

# Specify the target directory
target_directory = 'jumbo/jumbo_data_pampers'
scroll_amount = 500
store = 'Jumbo'
page_count = 4
url = 'https://www.jumbo.com.ar/bebes-y-ninos/panales?page='
content_area_css = 'div.vtex-search-result-3-x-gallery'
description_css = 'span.vtex-product-summary-2-x-productBrand'
price_css = 'div.jumboargentinaio-store-theme-1dCOMij_MzTzZOCohX1K7w'
link_css = 'a.vtex-product-summary-2-x-clearLink'

# Create an instance of CustomScraper
scraper = CustomScraper(target_directory,
                        scroll_amount,
                        store,
                        page_count,
                        False,
                        url,
                        content_area_css,
                        description_css,
                        price_css,
                        link_css)

# Call the scrape_data method to scrape data
scraper.scrape_data()
