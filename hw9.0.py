import requests, json, os
# from urllib.parse import urlencode


APP_ID = 51442805
TOKEN_VK = 'vk1.a.Bv85NseNvhbO1LmqMjyWHBNB-OL4tCYDOdjHhvvtTAQ-5rVEMThWpndE-wF2xTEhI6VE_-wNOJRtGwkIT8jbVb6uisDut3Iiilj-x2BqnbfitGoauAv-jtMvB2gyXbu-Bw3iQGCt7Gvq95aGSKeSMnCC-jNcdF3ZPqc_h-RPsxUw3DvMy5Qodp_6_Pu72XKEklSVuuHXhoLggaeqxnh_Gw'
TOKEN_Ya = 'y0_AgAAAAAMU5B4AADLWwAAAADQXDXFdBHPAWnrSai5pHFFKdIWfWAhyNQ'
BASE_DIR = os.getcwd()

class VKClient:
    BASE_URL: str = "https://api.vk.com/method/"
    URL_AUTH = "https://oauth.vk.com/authorize?client_id=51442805&redirect_uri=http://example.com/callback&scope=12&display=mobile"
    URL_REDIRECT = "https://oauth.vk.com/blank.html"
    METHOD_GET = "photos.get"
    PROTOCOL_VERSION: str = "5.131"
    

    def __init__(self, TOKEN: str = None, user_id: str = "1"):
        self.token = TOKEN_VK
        self.user_id = user_id

    
    def _get_url(self, method_name: str) -> str:
        return f"{self.BASE_URL}{method_name}"

    def get_photos(self):
        url = self._get_url(self.METHOD_GET)
        params = {
            "access_token": self.token,
            "v": self.PROTOCOL_VERSION,
            "album_id": "wall",
            "offset": "1",
            "count": "1"
            
        }

        response = requests.get(url, params=params)
        with open(r'foto_list.json', 'w') as file_write:
            json.dump(response.json(), file_write)

        name_file = 'foto_list.json'           
        return name_file

class YandexDisk:
    URL_UPLOAD_LINK: str = "https://cloud-api.yandex.net/v1/disk/resources/upload"


    def __init__(self, token: str):
        self.token = token

    @property
    def header(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }

    def _get_upload_link(self, ya_disk_path: str):
        params = {"path": ya_disk_path, "overwrite": "true"}
        response = requests.get(self.URL_UPLOAD_LINK, headers=self.header, params=params)
        
        if response.status_code != 200:
            raise requests.exceptions.RequestException
        
        upload_url = response.json().get("href")
        return upload_url

    def uploader(self, ya_disk_path: str, file_path: str):
        upload_link = self._get_upload_link(ya_disk_path)
        with open(file_path, 'rb') as file_obj:
            response = requests.put(upload_link, data=file_obj)
            if response.status_code == 201:
                print('Успешно загрузили')
            elif response.status_code == 412:
                print('При дозагрузке файла был передан неверный диапазон в заголовке Content-Range')
            elif response.status_code == 413:
                print('Размер файла больше допустимого.\n' \
                   'Если у вас есть подписка на Яндекс 360, можно загружать файлы размером до 50 ГБ,\n' \
                   'если подписки нет — до 1 ГБ.')
            elif response.status_code == 507:
                print('Для загрузки файла не хватает места на Диске пользователя.')
        return response.status_code


if __name__ == '__main__':
    client = VKClient(TOKEN_VK, "9214619")
    result = client.get_photos()
    
    FILES_NAME = result
    file_path = os.path.join(BASE_DIR, FILES_NAME)
    
    uploader = YandexDisk(TOKEN_Ya)
    uploader.uploader(FILES_NAME, file_path)

