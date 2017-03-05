from flask import Flask
from wakeonlan import wol
import config
import os


target_mac = config.WAKE_ON_LAN_TARGET

print('Sending magic packet to {}'.format(target_mac))
wol.send_magic_packet(target_mac)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/wakeup/')
def wake_up():
    wol.send_magic_packet(target_mac)
    return 'All righty mate, we are waking up azazel'

@app.route('/status/')
def statu():
    hostname = '192.168.1.80'
    response = os.system('ping -c 1 -w 2 ' + hostname)

    if response == 0:
        return '{} is up'.format(hostname)
    else:
        return '{} is down'.format(hostname)

