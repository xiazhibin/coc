import json
import time

from coc.model.clan_info import ClanInfo
from coc.model.war_log import WarLog
from coc.util import get_logger

huo_wu_qing_chun = '#9R9VLJOP'
logger = get_logger('spider_coc')


def run():
    clans()
    clan_info()


def clans():
    from coc.cache import cache_war_log, get_war_log_size, incr_war_log_size
    from coc import coc_api, redis_store
    size = get_war_log_size(redis_store, huo_wu_qing_chun)
    if not size:
        limit = 50
    else:
        limit = 2
    status_code, rv = coc_api.get_war_log(huo_wu_qing_chun, {'limit': limit})
    if status_code == 200:
        for obj in rv['items']:
            m = WarLog(obj)
            if cache_war_log(redis_store, huo_wu_qing_chun, m.timestamp, json.dumps(m.data)):
                incr_war_log_size(redis_store, huo_wu_qing_chun)
                logger.info(str(m))


def clan_info():
    from coc import coc_api, redis_store
    status_code, rv = coc_api.get_clan_info(huo_wu_qing_chun)
    if status_code == 200:
        m = ClanInfo(rv)
        if m.can_cache():
            from coc.cache import cache_clan_info
            m.data.update({'last_update': time.time()})
            cache_clan_info(redis_store, huo_wu_qing_chun, json.dumps(m.data))
            logger.info(str(m))
