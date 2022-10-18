from os import read
import requests, json
from urllib.parse import urlencode
#from token_my import TOKEN


APP_ID = 51442805
TOKEN = 'vk1.a.Bv85NseNvhbO1LmqMjyWHBNB-OL4tCYDOdjHhvvtTAQ-5rVEMThWpndE-wF2xTEhI6VE_-wNOJRtGwkIT8jbVb6uisDut3Iiilj-x2BqnbfitGoauAv-jtMvB2gyXbu-Bw3iQGCt7Gvq95aGSKeSMnCC-jNcdF3ZPqc_h-RPsxUw3DvMy5Qodp_6_Pu72XKEklSVuuHXhoLggaeqxnh_Gw'

class VKClient:
    BASE_URL: str = "https://api.vk.com/method/"
    URL_AUTH = "https://oauth.vk.com/authorize?client_id=51442805&redirect_uri=http://example.com/callback&scope=12&display=mobile"
    URL_REDIRECT = "https://oauth.vk.com/blank.html"
    METHOD_GET = "photos.getAll"
    PROTOCOL_VERSION: str = "5.131"
    

    def __init__(self, TOKEN: str = None, user_id: str = "1"):
        self.token = TOKEN
        self.user_id = user_id

    
    def _get_url(self, method_name: str) -> str:
        return f"{self.BASE_URL}{method_name}"

    def get_photos(self):
        url = self._get_url(self.METHOD_GET)
        params = {
            "access_token": self.token,
            "v": self.PROTOCOL_VERSION,
            "album_id": "wall",
            
        }

        response = requests.get(url, params=params)

        # with open(r'final_file.jpg', 'wb') as file_write:
        #     file_write.write(response)
                   
        return response.json()


client = VKClient(TOKEN, "9214619")
result = client.get_photos()
print(result)

