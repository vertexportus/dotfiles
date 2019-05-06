# -*- coding: utf-8 -*-
#
import subprocess
import os
import os.path

from i3pystatus import Status
# from i3pystatus.updates import pacman, cower


status = Status()

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week

# status.register("updates",
#     format = "Updates: {count}",
#     format_no_updates = "",
#     on_leftclick="termite --geometry=1200x600 --title=updates -e 'pacaur --needed --noconfirm --noedit -Syu'",
#     backends = [pacman.Pacman(), cower.Cower()])

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

# status.register("battery",
#     battery_ident="BAT0",
#     interval=5,
#     format="{status} {percentage:.0f}%",
#     alert=True,
#     alert_percentage=15,
#     color="#FFFFFF",
#     critical_color="#FF1919",
#     charging_color="#E5E500",
#     full_color="#D19A66",
#     status={
#         "DIS": " ",
#         "CHR": "  ",
#         "FULL": "   ",
# },)

status.register("temp",
        format=" {temp} °C",
        lm_sensors_enabled=False,
        dynamic_color=True
                )

# status.register("cpu_usage_graph",)
status.register("cpu_usage",
    #on_leftclick="terminology --name=htop -e 'htop' &",
    format=" {usage}%",)

status.register("mem",
    color="#999999",
    warn_color="#E5E500",
    alert_color="#FF1919",
    format=" {percent_used_mem}% - {used_mem}/{total_mem} GB",
    divisor=1073741824,)

# status.register("disk",
#     color='#56B6C2',
#     path="/home",
#     on_leftclick="pcmanfm",
#     format=" {avail} GB",)

# status.register("text",
#     text="|",
#     color="#222222")

# status.register("disk",
#     hints = {"separator": False, "separator_block_width": 3},
#     color='#ABB2BF',
#     path="/",
#     format=": {avail} GB",)

status.register('github',
    format=" {status} [{unread}][{update_error}]",
    notify_status=True,
    notify_unread=True,
    access_token='b283b649b95a00d93e4e3cb6e4560681107f08a5',)

status.register('ping',
   format_disabled='-ping-',
   color='#61AEEE')

status.register('scratchpad',)

# status.register("keyboard_locks",
#     format='{caps}{num}',
#     caps_on='A',
#     caps_off='a',
#     num_on='0',
#     num_off=' ',
#     color='#e60053',
#     )

# status.register("mpd",
#     host='localhost',
#     port='6600',
#     format="{status}",
#     on_leftclick="switch_playpause",
#     on_rightclick=["mpd_command", "stop"],
#     on_middleclick=["mpd_command", "shuffle"],
#     on_upscroll=["mpd_command", "next_song"],
#     on_downscroll=["mpd_command", "previous_song"],
#     status={
#         "pause": " ",
#         "play": " ",
#         "stop": " ",
#     },)

status.run()
