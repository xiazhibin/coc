import time

from flask import jsonify

from coc.model.clan_info import ClanInfo
from coc.model.war_log import WarLog

huo_wu_qing_chun = '#9R9VLJOP'


def clans():
    from coc import coc_api, redis_store
    status_code, rv = coc_api.get_war_log(huo_wu_qing_chun, {})
    if status_code == 200:
        for obj in rv['items']:
            m = WarLog(obj)
            from coc.cache import cache_war_log
            cache_war_log(redis_store, huo_wu_qing_chun, m.timestamp, m.data)
    return jsonify(rv)


def clan_info():
    from coc import coc_api
    status_code, rv = coc_api.get_clan_info(huo_wu_qing_chun)
    if status_code == 200:
        m = ClanInfo(rv)
        from coc.cache import cache_clan_info, redis_store
        m.data.update({'last_update': time.time()})
        cache_clan_info(redis_store, huo_wu_qing_chun, m.data)
    return jsonify(rv)
