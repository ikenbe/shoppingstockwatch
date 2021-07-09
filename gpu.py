import telegram_send
import time
import random
import bestbuy
import amazon


class Product:
    def __init__(self, name, bestbuyLink, amazonLink):
        self.name = name
        self.bestbuyLink = bestbuyLink
        self.amazonLink = amazonLink

    instock = False

    def checkStock(self):
        if self.bestbuyLink:
            bestbuy.check(self.bestbuyLink)


##########
nv3060Ti = Product(
    "Nvidia 3060 Ti",
    "https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3060-ti-8gb-gddr6-video-card/15166285",
    "",
)
nv3070 = Product(
    "Nvidia 3070",
    "https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3070-8gb-gddr6-video-card-only-at-best-buy/15078017",
    "",
)
evga3060Ti = Product(
    "evga3060ti",
    "https://www.bestbuy.ca/en-ca/product/evga-nvidia-geforce-rtx-3060-ti-ftw3-ultra-8gb-gddr6-video-card/15229237",
    "",
)
evga3070 = Product(
    "evga3070",
    "https://www.bestbuy.ca/en-ca/product/evga-geforce-rtx-3070-xc3-ultra-8gb-gddr6-video-card/15147122",
    "",
)
evga3080 = Product(
    "evga3080",
    "https://www.bestbuy.ca/en-ca/product/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6x-video-card/15084753",
    "",
)
msi3060ti = Product(
    "MSI 3060 Ti",
    "https://www.bestbuy.ca/en-ca/product/msi-nvidia-geforce-rtx-3060-ti-ventus-2x-oc-8gb-gddr6-video-card/15178453",
    "",
)
msi3070 = Product(
    "MSI 3070",
    "https://www.bestbuy.ca/en-ca/product/msi-nvidia-geforce-rtx-3070-ventus-3x-oc-8gb-gddr6-video-card/15038016",
    "",
)
msi3080 = Product(
    "MSI 3080",
    "https://www.bestbuy.ca/en-ca/product/msi-nvidia-geforce-rtx-3080-ventus-3x-10gb-gddr6x-video-card/14950588",
    "",
)
asustuf3080 = Product(
    "ASUS TUF 3080",
    "https://www.bestbuy.ca/en-ca/product/msi-nvidia-geforce-rtx-3080-ventus-3x-10gb-gddr6x-video-card/14950588",
    "",
)
asusrog3080 = Product(
    "ASUS ROG 3080",
    "https://www.bestbuy.ca/en-ca/product/msi-nvidia-geforce-rtx-3080-ventus-3x-10gb-gddr6x-video-card/14950588",
    "",
)
testobj = Product(
    "Corsair TM30 Performance Thermal Paste",
    "https://www.bestbuy.ca/en-ca/product/corsair-tm30-performance-thermal-paste/14193869",
    "",
)
##########
bbProducts = [
    nv3060Ti,
    nv3070,
    evga3060Ti,
    evga3070,
    evga3080,
    msi3060ti,
    msi3070,
    msi3080,
    asusrog3080,
    asustuf3080,
]
amznProducts = []
##########
def checkAll():
    for p in bbProducts:
        if p.bestbuyLink != "" and bestbuy.check(p.bestbuyLink) == True:
            telegram_send.send(messages=[p.name, "seems be be in stock BestBuy"])
            print(time.ctime(), "Alert!!", p.name, "in stock BestBuy!")
    for q in amznProducts:
        if q.amazonLink != "" and amazon.check(q.amazonLink) == True:
            telegram_send.send(messages=[q.name, "seems be be in stock Amazon"])
            print(time.ctime(), "\033[1;41;40m Alert!!", q.name, "in stock Amazon!\033[0m")


print(time.ctime(), "\033[34m Script Start\033[0m")
while True:
    checkAll()
    print(time.ctime(), "\033[1;30m No Stock Found. Staring New Cycle\033[0m")
    time.sleep(12.5 - random.random() * 5)
