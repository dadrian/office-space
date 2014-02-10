import cookielib
import httplib
import datetime
import urllib
import urllib2

class Credentials(object):
    
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._jar = cookielib.CookieJar()
        self._valid = False

    @property
    def valid(self):
        return self._valid

    def urlencode(self):
        creds =  { 
            'login': self._username,
            'password': self._password,
            'tokencode': '',
            'service': '',
            'required': '',
        }
        return urllib.urlencode(creds)

    def authenticate(self):
        url = ''.join([
            CosignHandler.DEFAULT_COSIGN_URL, 
            CosignHandler.DEFAULT_COSIGN_ENDPOINT
            ])
        page_req = urllib2.Request(
            CosignHandler.DEFAULT_COSIGN_URL
            )
        opener = urllib2.build_opener(
            urllib2.HTTPCookieProcessor(self._jar)
            )
        login_page = opener.open(page_req)
        self._jar.extract_cookies(login_page, page_req)
        login_req = urllib2.Request(
            url,
            self.urlencode()
        )
        login_res = opener.open(login_req)
        #print login_res.read()
        #mprint_req = urllib2.Request(
        #    'https://mprint.umich.edu/api/areas/'
        #)
        #mprint_res = opener.open(mprint_req)
        #print mprint_res.read()
        self._valid = True

    def invalidate(self):
        self._jar.clear()
        self._valid = False

class CosignHandler(urllib2.HTTPCookieProcessor):

    DEFAULT_COSIGN_URL = 'https://weblogin.umich.edu'
    DEFAULT_COSIGN_ENDPOINT = '/cosign-bin/cosign.cgi'

    def __init__(self, credentials):
        urllib2.HTTPCookieProcessor.__init__(self, credentials._jar)
        if not credentials.valid:
            credentials.authenticate()

if __name__ == '__main__':
    import sys
    c = Credentials(sys.argv[1], sys.argv[2])
    c.authenticate()




