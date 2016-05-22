import re


DETECTOR = [
    # Featured Phone
    r'(?P<agent>DoCoMo)',
    r'(?P<agent>SoftBank)',
    r'^(?P<agent>KDDI)',     # if no KDDI, HDML browser.
    r'(?P<agent>Vodafone)',
    r'(?P<agent>Nokia)',
    r'(?P<agent>MOT-)',
    r'(?P<agent>J-PHONE)',
    r'(?P<agent>BlackBerry)',
    r'(?P<agent>Symbian)',
    # Smart Device
    r'\((?P<agent>iPhone);',
    r'\((?P<agent>iPod);',
    r'\((?P<agent>iPad);',
    r'(?P<agent>Android)',
    r'(?P<agent>Windows\sPhone)',
    # Game Console
    r'(?P<agent>Nitro)',             # Nintendo DS
    r'(?P<agent>PlayStation)',
    r'(?P<agent>Wii)',               # Nintendo DS
    # PC
    r'(?P<agent>Trident)',           # Internet Explorer
    r'(?P<agent>Chrome)',
    r'(?P<agent>Firefox)',
    r'(?P<agent>Safari)',
    #    r'(?P<agent>Lunascape)',
    r'(?P<agent>Opera)',
    r'(?P<agent>MSIE)',
    r'(?P<agent>Konqueror)',
    # Bot
    r'(?P<agent>Googlebot)',
    r'(?P<agent>Yahoo)',
    r'(?P<agent>msnbot)',
    r'(?P<agent>Infoseek)',
]


def agent_type(agent_string):
    for d in DETECTOR:
        m = re.search(d, agent_string, flags=re.IGNORECASE)
        m = m and m.groupdict() or {}
        if m:
            return m['agent'].lower().replace('-', '').replace(' ', '')
    return "generic"
