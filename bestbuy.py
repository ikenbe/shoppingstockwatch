import urllib3
from lxml import etree


def check(prdct_link):
    user_agent = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
    }
    http = urllib3.PoolManager(10, headers=user_agent)
    r = http.request("GET", prdct_link)
    tree = etree.HTML(r.data).xpath('//div[contains(@class,"x-pdp-availability-online")]//text()')
    # avail = tree.xpath('//div[contains(@class,"availability")]//text()')
    # for text in avail:
    #    if (text.find('Coming soon') + text.find('Sold out') + text.lower().find('unavailable') + text.find('Check other stores') == -4):
    #        return True
    for text in tree:
        if text.find("Available to ship") > -1:
            #count += 1
            #if count > 1:
            return True
    return False