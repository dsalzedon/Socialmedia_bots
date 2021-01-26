"""
pip install -U instabot
git clone https://github.com/instagrambot/instabot --recursive
cd instabot/examples
"""

import datetime
import quickpost_ivmusic, quickpost_ivnavarr

iv_ph = quickpost_ivnavarr
iv_mu = quickpost_ivmusic

date = datetime.datetime.now()
day = date.strftime("%A")


if day = "Monday":
    iv_mu.upload_img()
elif day == "Tuesday":
    iv_ph.upload_img()
else:
    quit()
