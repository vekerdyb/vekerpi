import os
from flask import Flask, render_template, jsonify, url_for
from wakeonlan import wol

from .config import WAKE_ON_LAN_TARGET, BASE_URI

target_mac = WAKE_ON_LAN_TARGET

app = Flask(__name__)


@app.route('/')
def hello_world():
    css_url = BASE_URI + url_for('static', filename='styles.css') 
    watch_url = 'https://inxui.com/emby/'
    download_url = 'https://inxui.com/couchpotato/' 
    torrent_url = 'https://inxui.com/transmission/'
    data = {
        'css_url': css_url,
        'watch_url': watch_url,
        'download_url': download_url,
        'torrent_url': torrent_url,
    }
    return render_template('index.html', server_up=check_server(), **data)


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

