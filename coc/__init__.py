# coding=utf-8
import time
from operator import itemgetter

from flask import Flask, jsonify, render_template, request
from flask_redis import FlaskRedis
from coc.api import COCApi
from coc.model.war_log import WarLog
from coc.model.clan_info import ClanInfo
from flask_bootstrap import Bootstrap

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
Bootstrap(app)
redis_store = FlaskRedis(app)
coc_api = COCApi(app.config['COC_TOKEN'])

huo_wu_qing_chun = '#9R9VLJOP'
# huo_wu_qing_chun = '#RY2VYVOR'
Each = 10
rv = []
for i in range(100):
    b = dict()

    my = dict()
    op = dict()
    b['clan'] = my
    b['opponent'] = op
    my['name'] = u'fuxk'
    op['name'] = u'you'
    if i % 2 == 0:
        b['result'] = u'win'
    else:
        b['result'] = u'lose'
    rv.append(b)


#
# @app.route('/clans')
# def clans():
#     status_code, rv = coc_api.get_war_log(huo_wu_qing_chun, {})
#     if status_code == 200:
#         for obj in rv['items']:
#             m = WarLog(obj)
#             from coc.cache import cache_war_log
#             cache_war_log(redis_store, huo_wu_qing_chun, m.timestamp, m.data)
#     return jsonify(rv)
#
#
# @app.route('/')
# def clan_info():
#     status_code, rv = coc_api.get_clan_info(huo_wu_qing_chun)
#     if status_code == 200:
#         m = ClanInfo(rv)
#         from coc.cache import cache_clan_info
#         m.data.update({'last_update': time.time()})
#         cache_clan_info(redis_store, huo_wu_qing_chun, m.data)
#     return jsonify(rv)

@app.route('/')
def index():
    # status_code, rv = coc_api.get_war_log(huo_wu_qing_chun, {})
    return render_template('index.html')


import json

import datetime
from operator import attrgetter


@app.route('/data')
def data():
    offset = int(request.args.get('offset', 0))
    limit = int(request.args.get('limit', -1))
    from coc.cache import get_war_log
    data = get_war_log(redis_store, huo_wu_qing_chun, offset, limit)
    rv = []
    for value in data:
        m = WarLog(value)
        print m
        rv.append(m)
    print len(data)
    return jsonify()
