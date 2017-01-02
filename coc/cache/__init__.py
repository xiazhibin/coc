WAR_LOG = u'war_log_{0}'
CLAN_INFO = u'clan_info'
WAR_LOG_SIZE = u'war_log_size'
WAR_LOG_SCORE_SET = u'war_log_score_set_{0}'
import json


def get_war_log_size(redis_store, clan_tag):
    return redis_store.hget(WAR_LOG_SIZE, clan_tag)


def get_war_log(redis_store, clan_tag, offset=0, limit=-1):
    name = WAR_LOG.format(clan_tag)
    score_set = WAR_LOG_SCORE_SET.format(clan_tag)
    keys = redis_store.zrevrange(score_set, offset, offset + limit - 1)
    rv = []
    for key in keys:
        rv.append(json.loads(redis_store.hget(name, key)))
    return rv


def incr_war_log_size(redis_store, clan_tag, value=1):
    redis_store.hincrby(WAR_LOG_SIZE, clan_tag, value)


def cache_war_log(redis_store, clan_tag, timestamp, war_log):
    name = WAR_LOG.format(clan_tag)
    score_set = WAR_LOG_SCORE_SET.format(clan_tag)
    key = timestamp
    if not redis_store.hget(name, key):
        redis_store.hset(name, key, war_log)
        redis_store.zadd(score_set, timestamp, timestamp)
        return True
    else:
        return False


def cache_clan_info(redis_store, clan_tag, clan_info):
    name = CLAN_INFO.format(clan_tag)
    redis_store.hset(name, clan_tag, clan_info)
