import sys
import os

# Add the root directory of your project to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)


# Now import CustomScraper
from scraper import CustomScraper

# Specify the target directory
target_directory = 'coto/coto_data_panales'
scroll_amount = 500
store = 'Coto'
page_count = 1
url = 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-perfumería-pañales-y-productos-para-incontinencia-pañales-para-bebé/_/N-fmf3uu'
content_area_css = ''
description_css = 'div.descrip_full'
price_css = 'div.atg_store_productPrice'

# Create an instance of CustomScraper
scraper = CustomScraper(target_directory,
                        scroll_amount,
                        store,
                        page_count,
                        url,
                        None,
                        description_css,
                        price_css)

# Call the scrape_data method to scrape data
scraper.scrape_data()
