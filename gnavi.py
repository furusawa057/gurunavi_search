import requests


def main():
    # APIkeyは公開厳禁！！！！
    API_KEY = ''
    search_param = {'keyid': f'{API_KEY}',
                    'freeword': 'ワイン',
                    'hit_per_page': '5'}
    url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'

    response = requests.get(url, params=search_param)
    shop_list = response.json()['rest']

    for shop in shop_list:
        shop_name = shop['name']
        shop_url = shop['url']
        shop_line = shop['access']['line']
        shop_station = shop['access']['station']

        print(f'{shop_name},{shop_url}, {shop_line}{shop_station}')


if __name__ == '__main__':
    main()
