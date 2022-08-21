from scrapingbee import ScrapingBeeClient
from django.http import FileResponse

# Create your views here.
def scrapingbee(req):
    client = ScrapingBeeClient(api_key='YOUR API KEY')

    response = client.get(
        'https://www.geeksforgeeks.org/why-reading-code-is-more-important-than-writing/',
        params={
            'screenshot': True,
        }
    )

    if response.ok:
        with open("scrapingbeeshots/media/screenshot.png", "wb") as f:
            f.write(response.content)

    return FileResponse(open('scrapingbeeshots/media/screenshot.png', 'rb'))
