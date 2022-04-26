
from bs4 import BeautifulSoup
import requests
import os

html_txt = requests.get("https://www.flipkart.com/search?q=washing+machines&sid=j9e%2Cabm%2C8qx&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=washing+machines%7CWashing+Machines&requestId=5f16d7e7-80fb-46fb-ac3e-3e612728bb5d=")
soup = BeautifulSoup(html_txt.text, "lxml")
#print(soup)

res = soup.findAll("div", class_= "_3pLy-c row")

html ="<h1>"+" WashingMachine "+"</h1>"
html += '<table>'
html += "<tr>"
html += "<th>" + "product Name" +"</th>"
html += "<th>" + "Price" + "</th>"
html += "<th>" + "Discount" + "</th>"
html += "</tr>"
html += "<tr>"
for r in res:
    prod = r.find("div", class_="_4rR01T").text
    price = r.find("div", class_="_30jeq3 _1_WHN1").text
    discount = r.find("div",class_="_3Ay6Sb").find("span").text
    html += "<td>" + prod + "</td>"
    html += "<td>" + price + "</td>"
    html += "<td>" + discount + "</td>"
    html += "</tr>"
html += "</table>"

os.startfile('mypage.html')

