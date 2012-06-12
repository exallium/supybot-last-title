import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    from supybot.questions import expect, anything, something, yn
    LastTitle = conf.registerPlugin('LastTitle', True)

LastTitle = conf.registerPlugin('LastTitle')
