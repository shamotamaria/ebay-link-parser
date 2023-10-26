## Python script that parses ebay link

- Pagination: On each page script looks for "Next page" link and recursively call itself for that url.
- To filter items in a specific condition: Script accepts a parameter "new", "used", "notspecified" that maps to get-parameter `LH_ItemCondition`. Without a parameter or in case of value not listed above - parses all the items. For example,
```sh
python crawler.py used #parses only items that have condition "used"
```
- Future improvements: Add tests

## Task
Build a crawler in Go or Python that visits the following page:

https://www.ebay.com/sch/garlandcomputer/m.html

From there it should:
Extract the title, price, product URL and condition (new/pre-owned) information of each listed item.
Store the results in a folder called “data”.
Results should be individual files containing a JSON with the data defined above.
Each product URL follows this format:
https://www.ebay.com/itm/234908325972?hash=item36b1a09854:g:czcAAOSwHoRlFfxf

In which the ITEM ID is: 234908325972
Use the item ID as the filename for the result file.
For example: the file 234908325972.json should contain a json formatted in this way:


Bonus points:
Make the crawler write the result files asynchronously
Add support for pagination
Add a parameter to only crawl items in a specific condition (New, Pre-Owned, etc).

