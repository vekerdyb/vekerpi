import os
from flask import Flask, render_template, jsonify, url_for
from wakeonlan import wol

import config

target_mac = config.WAKE_ON_LAN_TARGET

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', server_up=check_server(), css_url=url_for('static', filename='styles.css'))


@app.route('/wakeup/')
def wake_up():
    wol.send_magic_packet(target_mac)
    return 'All righty mate, we are waking up azazel'


@app.route('/status/')
def status():
    return jsonify({'serverUp': check_server()})


def check_server():
    hostname = '192.168.1.80'
    # Ping the server, wait for one successful response of 1 second
    return os.system('ping -c 1 -w 1 {}'.format(hostname)) == 0
