import telegram_send
import time
import random
import bestbuy
import amazon

class Product:
    def __init__(self,name,bestbuyLink,amazonLink):
        self.name = name
        self.bestbuyLink = bestbuyLink
        self.amazonLink = amazonLink
    instock = False
    def checkStock(self):
        if (self.bestbuyLink):
            bestbuy.check(self.bestbuyLink)
##########
PS5Full = Product('PS5 Disc','https://www.bestbuy.ca/en-ca/product/playstation-5-console-online-only/14962185','https://www.amazon.ca/PlayStation-5-Console/dp/B08GSC5D9G/')
PS5Digital = Product('PS5 Digital','https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-console-online-only/14962184','https://www.amazon.ca/Playstation-3005721-PlayStation-Digital-Edition/dp/B08GS1N24H')
##########
bbProducts = [PS5Full,PS5Digital]
amznProducts = [PS5Full,PS5Digital]
##########
def checkAll():
    for p in bbProducts:
        if (p.bestbuyLink != ''):
            p.instock = bestbuy.check(p.bestbuyLink)
        if (p.instock == True):
            telegram_send.send(messages=[p.name,'seems be be in stock'])
            print(time.ctime(), 'Alert!!', p.name, 'in stock BestBuy!')
    for q in amznProducts:
        if (q.amazonLink != ''):
            q.instock = amazon.check(q.amazonLink)
        if (q.instock == True):
            telegram_send.send(messages=[q.name,'seems be be in stock'])
            print(time.ctime(), 'Alert!!', q.name, 'in stock Amazon!')

while True:
    checkAll()
    print(time.ctime(), 'Out of Stock')
    time.sleep( 12.5 - random.random()*5)