#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:53:41 2021

@author: dereknadeau
"""

import json
import pprint
from lyricsgenius import Genius

# json_data = None
# with open('Lyrics_TVGirl.json', 'r') as f:
#     data = f.read()
#     json_data = json.loads(data)

# pprint.pprint(json_data["current_user_metadata"])

token = 'lBg9b0ZtrxUQoR62McnjsQO_5wPogVI8OxS9s913JA1-b_scnKZ5sClH8KyPTOBj'
genius = Genius(token)
artist = genius.search_artist('TV Girl')
artist.save_lyrics()

## client ID - AeVClwCCRKlajlfshI_g5Leb3IBa5np3XK3rPvwkbm3VFhVhW6M-09I97q7sMxZB
## key - CPOBaeVmgWPQVyPDxZ1rPNGZP7CYCBPIQYUXsYXNgpdQoQes0-BIsiX2ID8w0Xm7Bb9TsTEmbSu_4lHQCiAP9Q