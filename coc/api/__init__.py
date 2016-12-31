from urllib import quote

import requests

api_endpoint = 'https://api.clashofclans.com/v1'


class COCApi(object):
    def __init__(self, token):
        self.token = token
        self.headers = {
            'Accept': "application/json",
            'authorization': "Bearer " + self.token
        }

    def _get(self, uri, params=None):
        url = api_endpoint + uri
        response = requests.get(url, params=params, headers=self.headers)
        return response.status_code, response.json()

    def get_war_log(self, clan_tag, params=None):
        url = '/clans/{0}/warlog'.format(quote(clan_tag))
        return self._get(url, params)

    def get_clan_info(self, clan_tag):
        url = '/clans/{0}'.format(quote(clan_tag))
        return self._get(url)
