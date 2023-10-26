import urllib.parse as urlparse
from urllib.parse import urlencode
import json


async def write_into_file(file_name, data):
  file_object = open(file_name, "w")
  file_object.write(json.dumps(data))
  file_object.close()


def compose_url_with_params(url, params):
  url_parts = list(urlparse.urlparse(url))
  query = dict(urlparse.parse_qsl(url_parts[4]))
  query.update(params)
  url_parts[4] = urlencode(query)
  return urlparse.urlunparse(url_parts)


def parse_element(element):
  link = element.find("a", class_="s-item__link")
  condition = element.find("div", class_="s-item__subtitle")
  price = element.find("span", class_="s-item__price")
  product_id = parse_product_id(link['href'])
  title = link.find("span", {"role": "heading"})

  data = {}
  data['product_id'] = product_id
  data['title'] = title.text if title else ""
  data['condition'] = condition.text if condition else ""
  data['price'] = price.text if price else ""
  data['product_url'] = link['href']
  return data


def parse_product_id(link):
  # parsing product_id from link https://www.ebay.com/itm/234908325972
  product_url = link
  parsed_url = urlparse.urlparse(product_url)
  url_path = parsed_url.path.split("/")
  return url_path[2]
