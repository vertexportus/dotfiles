# -*- coding: utf-8 -*-
#
import subprocess
import os
import os.path

from i3pystatus import Status
from keyrings.alt.file import PlaintextKeyring

status = Status()

status.register("clock",
    format=" %H:%M:%S ",
    color='#C678DD',
    interval=1,
    on_leftclick="/usr/bin/gsimplecal",)

status.register("clock",
    format="  %a %d-%m-%Y ",
    color='#61AEEE',
    interval=1,)

status.register("pulseaudio",
    color_unmuted='#98C379',
    color_muted='#E06C75',
    format_muted=' [muted]',
    format=" {volume}%")

status.register("network",
   interface="eno1",
   color_up="#8AE234",
   color_down="#EF2929",
   format_up=": {v4cidr}",
   format_down="",)

status.register("network",
   interface="wlo1",
   color_up="#8AE234",
   color_down="#EF2929",
   format_up=": {v4cidr}",
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
        "DIS": " ",
        "CHR": "  ",
        "FULL": "   ",
},)

status.register("temp",
        format=" {temp} °C",
        lm_sensors_enabled=False,
        dynamic_color=True
                )

status.register("cpu_usage",
    #on_leftclick="terminology --name=htop -e 'htop' &",
    format=" {usage}%",)

status.register("mem",
    color="#999999",
    warn_color="#E5E500",
    alert_color="#FF1919",
    format=" {percent_used_mem}% - {used_mem}/{total_mem} GB",
    divisor=1073741824,)

status.register('github',
    log_level=10,
    notify_status=True,
    notify_unread=True,
    access_token='f36fc1397ac1591c3507898fd34ff3be3ed8e709',
    hints={'markup': 'pango'},
    update_error='<span color="#ff0000">!</span>',
    refresh_icon='<span color="#ff5f00">⟳</span>',
    status={
        'good': '✓',
        'minor': '!',
        'major': '!!',
    },
    colors={
        'good': '#008700',
        'minor': '#d7ff00',
        'major': '#af0000',
    },
    format=' {status}[{unread_count}][{update_error}]',
    keyring_backend=PlaintextKeyring(),
    api_methods_url='https://www.githubstatus.com/api/v2/status.json'
)

status.register('ping',
   format_disabled='-ping-',
   color='#61AEEE')

status.register('scratchpad',)

status.run()
