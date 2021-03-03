import urllib3
from lxml import etree

def check(prdct_link):
    user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'}
    http = urllib3.PoolManager(10,headers=user_agent)
    r = http.request('GET',prdct_link)
    tree = etree.HTML(r.data)
    avail = tree.xpath('//div[@id = "availability"]//text()')
    avail = ' '.join(list(map(Strip, avail)))
    if (avail.find('Currently unavailable.')<0):
        return True
    return False
    '''
    for text in avail:
        text = text.strip()
        if (text.find('Currently unavailable.') + text.find('Sold out') + text.lower().find('unavailable') + text.find('Check other stores') == -4):
            return True
    return False
    '''
def Strip(st):
    st = st.strip()
    return st
'''
test = check('https://www.amazon.ca/PlayStation-5-Console/dp/B08GSC5D9G/')
test = map(Strip, test)
print(' '.join(list(test)))
'''