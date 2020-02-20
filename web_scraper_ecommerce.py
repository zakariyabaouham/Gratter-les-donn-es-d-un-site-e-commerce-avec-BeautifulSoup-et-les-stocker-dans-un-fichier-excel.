import requests
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
prixx=[] #Liste pour stocker le prix du produit
produits=[] #Liste pour stocker le nom du produit
images=[]#Liste pour stocker l'url de l'image
url = "http://www.tonpc.ma/pc-portable/samsung.html"
reponse_page = requests.get(url)

page_web= BeautifulSoup(reponse_page.content,'lxml')

all_products=page_web.find_all('div', class_='row product-listing')
for a in all_products:
	prix = a.find('div', attrs={'class':'price-box'})
	produit=a.find('h3', attrs={'class':'product-name bottom-line'})
	image=a.find('img', attrs={'class':'product-retina'})
	
	prixx.append(prix.get_text())
	produits.append(produit.get_text())
	images.append(image.get("src"))		
	
	df = pd.DataFrame({'Prix':prixx,'Produits':produits,'image':images}) 
	df.to_csv('produits.csv', index=False, encoding='utf-8')
	
