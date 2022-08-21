from django.shortcuts import redirect
from urlbox import UrlboxClient
from django.views.decorators.csrf import csrf_exempt
import time
import json

# Create your views here.
def urlbox(req):
    urlbox_client = UrlboxClient(api_key="YOUR API KEY", api_secret="YOUR API SECRET")
    urlbox_client.post({ "url": "https://www.geeksforgeeks.org/why-reading-code-is-more-important-than-writing/", "webhook_url":"https://ceb0-41-80-96-149.in.ngrok.io/urlbox/result/", "block_ads":True, "hide_cookie_banners":True })
    time.sleep(15)
    return redirect(result)

@csrf_exempt 
def result(request):
    if request.method == 'POST':
        mystr = request.body.decode('utf8').replace("'", '"') # from byte to string
        mydata = json.loads(mystr) # from string to dict
        global redUrl
        redUrl = mydata['result']['renderUrl']
    return redirect(redUrl)

