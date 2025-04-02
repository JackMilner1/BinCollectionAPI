import Councils.NorthHertfordshireDistrictCouncil as data

def makeRequest():
    fullAddress = ""
    user_postcode = ""
    user_paon = ""
    fullData = data.getData(fullAddress,user_postcode,user_paon)
    
    for pairs in fullData:
        print(f"Your {pairs[0]} is due on the {pairs[1]}")


makeRequest()
