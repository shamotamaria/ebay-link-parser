import requests
from bs4 import BeautifulSoup
import asyncio
import sys
from helper import compose_url_with_params, parse_element, write_into_file

URL_TO_CRAWL = "https://www.ebay.com/sch/garlandcomputer/m.html"
FOLDER_NAME = "data"
CONDITION_PARAM_NAME = "LH_ItemCondition"
CONDITION_NEW = {CONDITION_PARAM_NAME: 3}
CONDITION_USED = {CONDITION_PARAM_NAME: 4}
CONDITION_NOT_SPECIFIED = {CONDITION_PARAM_NAME: 10}


def crawl_url(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  # select items from the page html
  elements = soup.find_all("li", class_="s-item")
  for element in elements:
    try:
      data = parse_element(element)
      file_name = f"./{FOLDER_NAME}/{data['product_id']}.json"
      # create async task to write into the file
      asyncio.create_task(write_into_file(file_name, data))
    except:
      print(f"Error happened while processing item {data['product_id']}")
  #check if there is a next page to parse
  pagination_next = soup.find("a", class_="pagination__next")
  if pagination_next:
    crawl_url(pagination_next['href'])


async def main():
  params = {}
  # check if there is an argument to filter by condition
  if (len(sys.argv) == 1):
    crawl_url(URL_TO_CRAWL)
  else:
    if (sys.argv[1] == "new"):
      params = CONDITION_NEW
    elif (sys.argv[1] == "used"):
      params = CONDITION_USED
    elif (sys.argv[1] == "notspecified"):
      params = CONDITION_NOT_SPECIFIED

    url = compose_url_with_params(URL_TO_CRAWL, params)
    crawl_url(url)


if __name__ == "__main__":
    asyncio.run(main())
