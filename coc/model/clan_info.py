# coding=utf-8
class ClanInfo(object):
    def __init__(self, data):
        self.data = data
        self.tag = data['tag']
        self.utxt_name = data['name']
        self.warWinStreak = data['warWinStreak']
        self.warWins = data['warWins']
        self.isWarLogPublic = data['isWarLogPublic']
        self.warLosses = data.get('warLosses', -1)
        self.warTies = data.get('warTies', -1)

    def __str__(self):
        return u'部落名:{0}, 连胜:{1}, 胜场:{2}, 战败:{3}, 胜率:{4}%'.format(self.utxt_name, self.warWinStreak, self.warWins,
                                                                  self.warLosses,
                                                                  self.get_win_rate()).encode('utf-8')

    def get_win_rate(self):
        if self.isWarLogPublic:
            return round(self.warWins / float(self.warLosses + self.warWins + self.warTies) * 100, 2)
        else:
            return -1

    def can_cache(self):
        return self.warLosses != -1
