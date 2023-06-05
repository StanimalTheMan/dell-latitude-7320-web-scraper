from bs4 import BeautifulSoup
import requests

targetURL = 'https://www.dell.com/en-us/shop/dell-laptops/latitude-7320-laptop/spd/latitude-13-7320-2-in-1-laptop/cto01l732013us?redirectTo=SOC'

is_latitude_7320_in_stock = False # dummy initialization as I last checked and it was temporarily out of stock

request = requests.get(targetURL)

soup = BeautifulSoup(request.content, 'html.parser')

button = soup.find('button', attrs={'data-testid': 'addToCartButton'})

button_text = button.text
if "Temporarily Out of Stock" not in button_text:
    is_latitude_7320_in_stock = True

in_stock_string_status = "in stock" if is_latitude_7320_in_stock else "out of stock"
print(f"Dell Latitude 7320 2 in 1 is {in_stock_string_status}")