import numpy as np
from random import choice

def firefox_headers():
    platform = choice([
        'Windows NT 6.1; Win64',
        'Macintosh; Intel Mac OS X x.y',
        'X11; Linux x86_64',
    ])

    gecko_version = np.round(choice(np.arange(70.0, 84.0)),1)
    user_agent = f'Mozilla/5.0 ({platform}; rv:{gecko_version}) Gecko/20100101 Firefox/{gecko_version}'

    return {"user-agent": user_agent}
