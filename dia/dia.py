import sys
import os

# Add the root directory of your project to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)


# Now import CustomScraper
from scraper import CustomScraper

# Specify the target directory
target_directory = 'dia/dia_data_pampers'
scroll_amount = 500
store = 'Dia'
page_count = 1
page_flag = True
url = 'https://diaonline.supermercadosdia.com.ar/bebes-y-ninos/panales/panales'
#content_area_css = 'div.vtex-flex-layout-0-x-flexCol'
description_css = 'span.vtex-product-summary-2-x-productBrand'
price_css = 'span.vtex-product-price-1-x-sellingPriceValue'
link_css = 'a.vtex-product-summary-2-x-clearLink'
# Create an instance of CustomScraper
scraper = CustomScraper(target_directory,
                        scroll_amount,
                        store,
                        page_count,
                        page_flag,
                        url,
                        None,
                        description_css,
                        price_css,
                        link_css)

# Call the scrape_data method to scrape data
scraper.scrape_data()
