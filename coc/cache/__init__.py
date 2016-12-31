WAR_LOG = 'war_log_{0}'
CLAN_INFO = 'clan_info'


def cache_war_log(redis_store, clan_tag, timestamp, war_log):
    name = WAR_LOG.format(clan_tag)
    key = timestamp
    if not redis_store.hget(name, key):
        redis_store.hset(name, key, war_log)


def cache_clan_info(redis_store, clan_tag, clan_info):
    name = CLAN_INFO.format(clan_tag)
    redis_store.hset(name, clan_tag, clan_info)
