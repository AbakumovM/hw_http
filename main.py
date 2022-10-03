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
            if i['name'] in [hero1, hero2, hero3]:
                intel_hero[i['name']] = i['powerstats']['intelligence']
        for j in intel_hero:
            if intel_hero[j] == max(intel_hero.values()):
                return f'Самый умный среди Ваших супергероев : {j}'           


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

def get_fike_hw3():
    url = 'https://api.stackexchange.com/2.3/questions?fromdate=1664496000&todate=1664668800&order=desc&sort=activity&tagged=Python&site=stackoverflow'            
    respons = requests.get(url)
    return respons.json()
        
        



if __name__ == '__main__':
    #Задча 1
    super_man = SuperHeroes()
    result = super_man.get_file_list()
    r = super_man.intelligence_heroes(result, 'Hulk', 'Captain America', 'Thanos')
    print(r)
    #Задача 2
    # path_to_file = input('Введите полный путь до файла, который хотите загрузить на диск: ')
    # token = input('Введите Ваш TOKEN: ')
    # uploader = YaUploader(token)
    # result = uploader.upload(path_to_file)
    # pprint(result)
    # # Задача 3
    # r = get_fike_hw3()
    # pprint(r)


    
