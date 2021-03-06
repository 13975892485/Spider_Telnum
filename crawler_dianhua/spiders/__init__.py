# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.xlib.tx._newclient import HTTPClientParser, ParseError
old_sr = HTTPClientParser.statusReceived

def statusReceived(self, status):
    try:
        return old_sr(self, status)
    except ParseError, e:
        if e.args[0] == 'wrong number of parts':
            return old_sr(self, status + ' OK')
        raise

statusReceived.__doc__ == old_sr.__doc__
HTTPClientParser.statusReceived = statusReceived
