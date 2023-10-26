import unittest
from helper import compose_url_with_params, parse_element
from bs4 import BeautifulSoup



class TestHelperMethods(unittest.TestCase):

    def test_compose_url_with_params(self):
        url = "http://foo.bar"
        params = {"key":2}
        self.assertEqual(compose_url_with_params(
            url, params), 'http://foo.bar?key=2')
        url = "http://foo.bar?key1=1"
        self.assertEqual(compose_url_with_params(
            url, params), 'http://foo.bar?key1=1&key=2')

    def test_parse_element(self):
        item_file = open("./test_data/item.html", "r")
        element = item_file.read()
        soup = BeautifulSoup(element, "html.parser")
        data = parse_element(soup)

        self.assertEqual(data['product_id'],"296006778391")
        self.assertEqual(data['title'],"Test title")
        self.assertEqual(data['condition'], "Pre-Owned")
        self.assertEqual(data['price'], "MXN $677.89")
        self.assertEqual(data['product_url'],
                         "https://www.ebay.com/itm/296006778391")
        item_file.close()


if __name__ == '__main__':
    unittest.main()
