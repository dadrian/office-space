import urllib2
import datetime
import cosign

class Client(object):

    HOST = 'mprint.umich.edu'

    def __init__(self, credentials, *args, **kwargs):
        self.creds = credentials
        self._debug = kwargs.get("debug", False)

    def _build_uri(self, path):
        return ''.join(['https://', Client.HOST, '/api', path])

    def api_call(self, method, path, params, auth=True):
        """
        Call an MPrint API method

        * method: HTTP request method (e.g. POST)
        * path: Path of the endpoint e.g. /areas
        * params: Dictionary of 
        """
        host = Client.HOST
        port = 80
        uri = self._build_uri(path)
        d = datetime.datetime.now()
        now = d.strftime("%a, %d %b %Y %H:%M:%S %z")
        print uri

        body = ''
        req = urllib2.Request(
            uri
            )
        opener = urllib2.build_opener(cosign.CosignHandler(self.creds))
        res = opener.open(req)
        data = res.read()
        return (res, data)


if __name__ == '__main__':
    import sys
    creds = cosign.Credentials(sys.argv[1], sys.argv[2])
    c = Client(creds, debug=True)
    (r, d) = c.api_call('GET', '/areas/', {})
    print r
    print d


