WAR_LOG = u'war_log_{0}'
CLAN_INFO = u'clan_info'
WAR_LOG_SIZE = u'war_log_size_{0}'


def get_war_log_size(redis_store, clan_tag):
    name = WAR_LOG_SIZE.format(clan_tag)
    return redis_store.get(name)


def incr_war_log_size(redis_store, clan_tag, value=1):
    name = WAR_LOG_SIZE.format(clan_tag)
    redis_store.incr(name, value)


def cache_war_log(redis_store, clan_tag, timestamp, war_log):
    name = WAR_LOG.format(clan_tag)
    key = timestamp
    if not redis_store.hget(name, key):
        redis_store.hset(name, key, war_log)
        return True
    else:
        return False


def cache_clan_info(redis_store, clan_tag, clan_info):
    name = CLAN_INFO.format(clan_tag)
    redis_store.hset(name, clan_tag, clan_info)
