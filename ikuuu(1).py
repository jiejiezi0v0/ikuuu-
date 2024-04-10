import requests
from lxml import etree
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
def findurl():
    url=requests.get("https://ikuuu.club/",headers=headers)
    tree=etree.HTML(url.content.decode())
    URL=tree.xpath('/html/body/center[1]/p/a')[0].text
    return URL
s = requests.session()
data={
    "email":"",#your email
    "passwd":""#your password
}
dest=findurl()
s.post(dest+"/auth/login",headers=headers,data=data)
s.post(dest+"/user/checkin",headers=headers)