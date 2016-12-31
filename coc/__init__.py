# coding=utf-8
import time
from flask import Flask, jsonify, render_template
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
def test():
    return render_template('index.html')
