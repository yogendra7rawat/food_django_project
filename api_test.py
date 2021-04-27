from clarifai.rest import ClarifaiApp
from .models import Input_Url

app = ClarifaiApp(api_key = "c4084332b2384a619b08283ae5658ee9")

concepts =""
url = ""
ID = -1000000
obj = Input_Url.objects.all().values()
for D in obj:
    for k,v in D.items():
        if k=='names':
            url  = v

response=app.tag_urls(urls=["{}".format(url)],model_id='bd367be194cf45149e75f01d59f77ba7')
data=response['outputs']
data=data[0] 
data=data['data']
concepts=data
concepts=concepts['concepts']

def ingredient():
    l = []
    for D in concepts:
        for k,v in D.items():
            if k=="name":
                l.append(v)

    return l