import bs4
import requests
import lxml

def migros_checker(product_name):
    url = "https://www.sanalmarket.com.tr/arama?q="
    real_product = product_name.replace(" ","+")
    real_url = url + real_product
    migros_response = requests.get(real_url)
    migros_soup = bs4.BeautifulSoup(migros_response.text , "lxml")
    dict = []
    for j in migros_soup.find_all(class_ = "product-card product-action "):
        dict.append({
            "link" : "https://www.sanalmarket.com.tr"+j.find("a")["href"],
            "urun" : j.find(class_="title product-card-title").text,
            "resim" : j.find("img")["src"],
            "fiyat" : (j.find(class_="price-tag").text.split("\n")[1].split("T")[0].lstrip().rstrip().replace(",","."))+" TL"

        })
    return dict

def carrefoursa_checher(product_name):
    url = "https://www.carrefoursa.com/tr/search/?text="
    real_product = product_name.replace(" ","+")
    real_url = url + real_product
    carrefoursa_response = requests.get(real_url)
    carrefoursa_soup = bs4.BeautifulSoup(carrefoursa_response.text , "lxml" )
    dict = []
    for i in carrefoursa_soup.find_all(class_ = "col-xs-6 col-sm-3 col-md-2 col-lg2"):
        dict.append({
            "link" : "https://www.carrefoursa.com/tr"+i.find("a")["href"],
            "urun" : i.find(class_ = "item-name").text,
            "resim" : i.find("img")['src'],
            "fiyat" : (i.find(class_ = "item-price").text.split("T")[0].replace(",","."))+" TL"
        })
    return dict
