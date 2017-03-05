from wakeonlan import wol
import config


target_mac = config.WAKE_ON_LAN_TARGET

print('Sending magic packet to {}'.format(target_mac))
wol.send_magic_packet(target_mac)
