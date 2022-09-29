import requests

from pprint import pprint


class SuperHeroes:

    def get_file_list(self):
        url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
        respons = requests.get(url)
        return respons.json()

    def intelligence_heroes(self, get_file_list, hero1, hero2, hero3):
        intel_hero = {}
        for i in get_file_list:
            if i['name'] == hero1:
                intel_hero[hero1] = i['powerstats']['intelligence']
            if i['name'] == hero2:
                intel_hero[hero2] = i['powerstats']['intelligence']       
            if i['name'] == hero3:
                intel_hero[hero3] = i['powerstats']['intelligence']
        return f'Самый умный среди Ваших супергероев : {max(intel_hero)}'           


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }


    def _get_upload_link(self, file_path):
        url_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path.split('/')[-1], 'overwrite': 'true'}
        respons = requests.get(url_upload, headers=headers, params=params)
        return respons.json()


    def upload(self, file_path ):
        href = self._get_upload_link(file_path=file_path).get('href', '')
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return 'Файл добавлен!'

        
        



if __name__ == '__main__':
    super_man = SuperHeroes()
    result = super_man.get_file_list()
    r = super_man.intelligence_heroes(result, 'Hulk', 'Captain America', 'Thanos')
    print(r)
    path_to_file = input('Введите полный путь до файла, который хотите загрузить на диск: ')
    token = input('Введите Ваш TOKEN: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    pprint(result)


    
