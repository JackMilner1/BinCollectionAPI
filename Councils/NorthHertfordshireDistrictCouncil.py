from bs4 import BeautifulSoup
import requests

def getData():
    thing = "ADDRESS"
    user_postcode = "SG1 6BH"
    user_paon = "9"
    url = "https://uhtn-wrp.whitespacews.com/"
    session = requests.Session()
    hashedLink = session.get(url)
    hashedLink.raise_for_status()

    doc = BeautifulSoup(hashedLink.text,"html.parser")
    alink = doc.find("a", text="Find my bin collection day")
    address_field = doc.find("input",{"id":"address_postcode"})
    nextpageurl = alink["href"].replace("seq=1", "seq=2")
    print(address_field)
    print("\n\n\n" + alink["href"])

    print(nextpageurl)

    data = {
        "address_name_number": user_paon,
        "address_postcode": user_postcode,
    }

    link = session.post(nextpageurl,data)

    link.raise_for_status() 
    doc = BeautifulSoup(link.text,"html.parser")
    alink = doc.find("a", text=thing)
    binDataURL = url + alink["href"]
    binData = session.get(binDataURL)
    doc = BeautifulSoup(binData.text,"html.parser")
    #print(doc.prettify())

    u1s = doc.find("section", id="scheduled-collections").find_all("u1")

    print(u1s)

getData()