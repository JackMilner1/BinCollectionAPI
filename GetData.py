import Councils.NorthHertfordshireDistrictCouncil as data

def makeRequest():
    fullAddress = ""
    user_postcode = ""
    user_paon = ""
    fullData = data.getData(fullAddress,user_postcode,user_paon)
    
    for pairs in fullData:
        print(f"Your {pairs[0]} is due on the {pairs[1]}")

def findChosenCouncil(address,postcode,poan):
    # this will check what the postcode is and return the council associated with the postcode
    # this council can then be imported and getData can be ran
    pass

def searchPostcode():
    pass

def getDataRecieverImport():
    pass

def canUserRequest():
    pass

makeRequest()
