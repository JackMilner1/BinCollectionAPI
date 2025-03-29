from bs4 import BeautifulSoup
import requests

def getData():
    fullAddress = ""
    user_postcode = ""
    user_paon = ""
    url = "https://uhtn-wrp.whitespacews.com/"
    session = requests.Session()
    hashedLink = session.get(url)
    hashedLink.raise_for_status()


    # Home page 
    doc = BeautifulSoup(hashedLink.text,"html.parser")
    alink = doc.find("a", text="Find my bin collection day")
    nextpageurl = alink["href"].replace("seq=1", "seq=2")

    # Enter user data to parse to next page so correct address data is sent

    data = {
        "address_name_number": user_paon,
        "address_postcode": user_postcode,
    }

    # Gets the page with a list of addresses you can select from

    link = session.post(nextpageurl,data)
    link.raise_for_status() 
    doc = BeautifulSoup(link.text,"html.parser")
    alink = doc.find("a", text=fullAddress) # finds the address matching to the users
    binDataURL = url + alink["href"] # full link for bin data

    # Gets page with bin data

    binData = session.get(binDataURL)
    doc = BeautifulSoup(binData.text,"html.parser")
    u1s = doc.find("section", id="scheduled-collections").find_all("u1") # all data entries


    returnData = []
    print("---------------------------------------------------------------------------")
    print("-------------------------------Your Bin Data-------------------------------")
    print("---------------------------------------------------------------------------")
    for element in u1s:
        DateAndType = element.find_all("li",recursive=False)
        # DateAndType[0] is an image so is unnecessary 
        date = DateAndType[1].text.replace("\n","")
        binType = DateAndType[2].text.replace("\n","")
        print(f"{binType} is due at {date}")
        returnData = returnData + [(binType,date)]
    print("---------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------")
    
    return returnData # returns an array of (binType,date) pairs

getData()