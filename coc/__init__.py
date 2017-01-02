# coding=utf-8

from flask import Flask, jsonify, render_template, request
from flask_bootstrap import Bootstrap
from flask_redis import FlaskRedis

from coc.api import COCApi
from coc.model.clan_info import ClanInfo
from coc.model.war_log import WarLog

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
Bootstrap(app)
redis_store = FlaskRedis(app)
coc_api = COCApi(app.config['COC_TOKEN'])

huo_wu_qing_chun = '#9R9VLJOP'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def data():
    offset = int(request.args.get('offset', 0))
    limit = int(request.args.get('limit', -1))
    from coc.cache import get_war_log, get_war_log_size
    data = get_war_log(redis_store, huo_wu_qing_chun, offset, limit)
    rv = []
    for value in data:
        m = WarLog(value)
        rv.append(m.to_dict())
    size = get_war_log_size(redis_store, huo_wu_qing_chun)
    return jsonify({'rows': rv, 'total': size})
