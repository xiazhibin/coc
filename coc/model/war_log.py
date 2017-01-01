# coding=utf-8

from coc.util import convert_utc_time, datetime_to_timestamp


class WarLog(object):
    wins = 0

    def __init__(self, data):
        self.data = data
        self.clan = data['clan']
        self.opponent = data['opponent']
        self.result = u'胜利' if data['result'] == u'win' else u'失败'
        self.timestamp = datetime_to_timestamp(convert_utc_time(data['endTime']))

    def __str__(self):
        return u'{0} vs {1} \n结果:{2} \nat {3} \n'.format(self.clan['name'], self.opponent['name'], self.result,
                                                         self.timestamp).encode('utf-8')
