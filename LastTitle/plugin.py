import supybot.callbacks as callbacks
import supybot.utils as utils
from supybot.commands import *
import lxml.html

SITEEND = ["com", "org", "edu", "gov", "it", "ca"]
FILEEXT = ["jpg", "jpeg", "gif", "pdf", "tif", "png"]

class LastTitle(callbacks.PluginRegexp):
    threaded = True
    regexps = ['checkForTitle']

    def checkForTitle(self, irc, msg, match):
        x = match.group(0)

        for ext in FILEEXT:
            if x.endswith(".%s" % ext):
                self.last_title = "file: %s" % ext.upper()
                return

        for end in SITEEND:
            if x.endswith(end):
                x += '/'

        last_title = lxml.html.parse(x).find(".//title")
        self.last_title = last_title.text if last_title is not None else "No title available!"

    checkForTitle = urlSnarfer(checkForTitle)
    checkForTitle.__doc__ = utils.web._httpUrlRe

    def lt(self, irc, msg, *args, **kwargs):
        try:
            irc.reply("'%s'" % self.last_title)
        except AttributeError:
            irc.reply("No title available!")
    lt = wrap(lt, ['channeldb'])


Class = LastTitle
