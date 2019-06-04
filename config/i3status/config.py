# -*- coding: utf-8 -*-
#
import subprocess
import os
import os.path
import netifaces

from i3pystatus import Status
from keyrings.alt.file import PlaintextKeyring

status = Status(logfile='$HOME/.logs/i3pystatus.log')

status.register("clock",
    format=" %H:%M",
    color='#C678DD',
    interval=30,
    on_leftclick="/usr/bin/gsimplecal",)

status.register("clock",
    format=" %a %d-%m-%Y ",
    color='#61AEEE',
    interval=3600,)

status.register("pulseaudio",
    color_unmuted='#98C379',
    color_muted='#E06C75',
    format_muted='ﱝ',
    format="墳 {volume}%")

status.register("external_ip",
    format=" {country_code}",
    format_hide=" {country_name} {ip}",
    format_down="",
    color="#8AC254",
    color_hide="#8AE234",
    color_down="#EF2929",
    interval=600)

interface_list = netifaces.interfaces()
interface = filter(lambda x: 'en' in x,interface_list)
for iff in interface:
    status.register("network",
        interface=iff,
        color_up="#8AE234",
        color_down="#EF2929",
        format_up="",
        format_down="",)

has_wifi = os.popen('ip a | grep wlo1').read()
if has_wifi != '':
    status.register("network",
    interface="wlo1",
    color_up="#8AE234",
    color_down="#EF2929",
    format_up="",
    format_down="",)

status.register("battery",
    battery_ident="BAT0",
    interval=5,
    format="{status} {percentage:.0f}%",
    alert=True,
    alert_percentage=15,
    color="#FFFFFF",
    critical_color="#FF1919",
    charging_color="#E5E500",
    full_color="#D19A66",
    status={
        "DIS": "",
        "CHR": "",
        "FULL": "",
    },
    not_present_text="")

# nvidia_in_use = os.popen('lspci -nnk | grep -i vga -A3 | grep nvidia').read()
# amd_in_use = os.popen('lspci -nnk | grep -i vga -A3 | grep amdgpu').read()
# if nvidia_in_use != '':
# if os.popen('prime-select query | grep nvidia').read() != '':
status.register('gpu_temp',
    format="﨏 {temp} °C",
    color="#2be5c6",
    alert_temp=70)
# elif amd_in_use != '':
#     status.register('amdgpu',
#         format=' {temp} °C',
#         color="#2be5c6")

status.register("temp",
        format="﨎 {temp} °C",
        lm_sensors_enabled=False,
        dynamic_color=True)

status.register("cpu_usage",
    on_leftclick="terminology --name=htop -e 'htop' &",
    format="龍 {usage}%",)

status.register("mem",
    color="#999999",
    warn_color="#E5E500",
    alert_color="#FF1919",
    format=" {used_mem}/{total_mem} GB",
    divisor=1073741824,)

github_access_token = os.environ.get('GITHUB_NOTIFICATIONS_TOKEN')
status.register('github',
    notify_status=True,
    notify_unread=True,
    access_token=github_access_token,
    hints={'markup': 'pango'},
    update_error='<span color="#ff0000">!</span>',
    refresh_icon='<span color="#ff5f00">⟳</span>',
    format=' [{status}][{unread_count}][{update_error}]',
    keyring_backend=PlaintextKeyring(),
    status={
        'none': '',
        'minor': '!',
        'major': '!!',
        'critical': '!!!',
    },
    colors={
        'none': '#22bb00',
        'minor': '#d7ff00',
        'major': '#af0000',
        'critical': '#640000',
    },
    interval=300,
)

status.register('ping',
   format_disabled='-ping-',
   color='#61AEEE')

status.register('spotify',
    status={
        'play':'',
        'stop':'',
        'pause':''
    },
    format=' {artist} {status}',
    format_no_player='')

status.register('scratchpad',)

status.run()
