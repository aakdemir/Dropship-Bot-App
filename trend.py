import requests
from send_email import sendMail

URLS = []
#product_id = int(input ("Product Id :"))

URL = "https://public.trendyol.com/discovery-web-productgw-service/api/productDetail/" + str(203007364)
URLS.append(URL)
for url_name in URLS:
    r = requests.get(url = url_name)
    data = r.json()
    result = data['result']
    name = result['name']
    print(name , " " , URL)
    for i in range(0,len(result['variants'])):
            size = result['variants'][i]['attributeValue']
            stock =  result['variants'][i]['stock']
            print("size:%s\nstock:%s"
                %( size, stock))
    if(stock == 0):
        htmlEmailContent= """\
            <html>
            <head></head>
            <body>
            <h2>Product Name : {0}</h3>
            <h2>Size : {1}</h2>
            <br/>
            Stock : {2}
            <br/>
            <p>{3}</p>
            </body>
            </html>
            """.format(name,size,stock,"")
        sendMail("alpcanakdemir@gmail.com","Stok Bilgisi",htmlEmailContent)


#203007364