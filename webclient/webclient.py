import requests
import urllib
import cv2
import os

def image(url):
    curDir = os.getcwd()
    print("saving in " + curDir)
    print("OK")
    file = "\\2017030482.jpg"
    urllib.request.urlretrieve(url, curDir+file)

    image = cv2.imread("2017030482.jpg", cv2.IMREAD_UNCHANGED)
    cv2.imshow("2017030482", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
def get(url):
    if len(url) == 0:
        print("Error")
        return

    headers = {'User-Agent': '2017030482/EUNJINHEO/WEBCLIENT/COMPUTERNETWORK'}
    response = requests.get(url=url, timeout = 100000, headers = headers)

    response.encoding = 'utf-8'

    if response.status_code == 404:
        print("NOT FOUND")
    elif response.status_code == 200:
        print(response.text)
    else:
        print(response.status_code)
        
def post(url, data):
    if len(url) == 0:
        print("Error")
        return
    
    headers = {'User-Agent': '2017030482/EUNJINHEO/WEBCLIENT/COMPUTERNETWORK'}
    response = requests.post(url=url, timeout = 100000, headers = headers, data=data)

    response.encoding = 'utf-8'

    if response.status_code == 404:
        print("NOT FOUND")
    elif response.status_code == 200:
        print(response.text)
    else:
        print(response.status_code)
        
if __name__ == '__main__':
    url = "http://52.79.241.196:54097/test/780263.jpg"

    image(url)
    get(url)
    data = input()
    post(url, data)


    
