import bs4
import requests

def migros_checker(product_name):
    url = "https://www.migros.com.tr/arama?q="
    real_product = product_name.replace(" ","+")
    real_url = url + real_product
    migros_response = requests.get(real_url)
    migros_soup = bs4.BeautifulSoup(migros_response.text , "lxml")
    dict = []
    for j in migros_soup.find_all(class_ = "center product-card-center"):
        try:
           fiyat = float(j.find(class_="price-tag").text.split("\n")[1].split("T")[0].lstrip().rstrip().replace(",","."))
        except ValueError:
            fiyat = j.find(class_="price-tag").text.split("\n")[1].split("T")[0].lstrip().rstrip().replace(",",".")

        dict.append({
            "link" : "https://www.sanalmarket.com.tr"+j.find("a")["href"],
            "urun" : j.find(class_="title product-card-title").text,
            "resim" : j.find("img")["data-src"],
            "fiyat" : fiyat
            #eğer istenirse float dönüşümüne uygun
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
        try:
           fiyat = float(i.find(class_="item-price").text.split("T")[0].replace(",", "."))
        except ValueError:
            fiyat = i.find(class_="item-price").text.split("T")[0].replace(",", ".")


        dict.append({
            "link" : "https://www.carrefoursa.com/tr"+i.find("a")["href"],
            "urun" : i.find(class_ = "item-name").text,
            "resim" : i.find("img")['src'],
            "fiyat" : fiyat
            # eğer istenirse float dönüşümüne uygun
        })
    return dict

def bizim_checker(product_name):
    url = "https://www.bizimtoptan.com.tr/arama/"
    real_product = product_name.replace(" ","%20")
    real_url = url + real_product
    bizim_response = requests.get(real_url)
    bizim_soup = bs4.BeautifulSoup(bizim_response.text,"lxml")
    dict = []
    for i in bizim_soup.find_all(class_ = "col-lg-3 col-sm-4 col-xs-4 col-xxs-6"):
        dict.append({
            "link" : "https://www.bizimtoptan.com.tr" + i.find("a")["href"],
            "urun" : i.find("h3").text
        })
    return dict
