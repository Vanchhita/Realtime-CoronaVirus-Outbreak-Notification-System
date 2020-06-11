from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title,message):
    notification.notify(title= title,message=message,
    app_icon ='C:/Users/user/CoronaNotification/eq.ico',timeout=5)
def getData(url):
    r=requests.get(url)
    return r.text
if __name__ == "__main__":
    while(True):
        # notifyMe("Vanya","Let stop the spread of this virus together")
        myHtlmData=getData("https://www.mohfw.gov.in/")
        
        

        soup = BeautifulSoup(myHtlmData, 'html.parser')
        # print(soup.prettify())
        myDataStr=""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr+=tr.get_text()
        myDataStr=myDataStr[1:]
        itemlist=myDataStr.split("\n\n")
        states=['Uttar Pradesh','Bihar','Madhya Pradesh']

        for items in itemlist[0:35]:
            datalist=items.split("\n")
            if datalist[1] in states:
                # print(datalist)
                nTitle='Cases if Covid-19'
                nText=f"State:- {datalist[1]}\n Indian: {datalist[2]}  Foreign: {datalist[3]} \nCures: {datalist[4]}\n Deaths: {datalist[5]} "
                notifyMe(nTitle,nText)
                time.sleep(2)
        time.sleep(3600)




        


        