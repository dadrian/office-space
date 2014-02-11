import urllib2
import datetime
import cosign
import itertools
import urllib

class Client(object):

    HOST = 'mprint.umich.edu'

    def __init__(self, credentials, *args, **kwargs):
        self.creds = credentials
        self._debug = kwargs.get("debug", False)

    def _build_uri(self, path, urlparams=None):
        base = ['https://', Client.HOST, '/api', path]
        if self._debug:
            if not urlparams:
                urlparams = dict()
            urlparams.update({
                    'debug': ''
                })
        if urlparams:
            uri_parts = itertools.chain(
                    base,
                    ['?', urllib.urlencode(urlparams)],
                )
            return ''.join(uri_parts)
        else:
            return ''.join(base)

    def api_call(self, method, path, params, auth=True):
        """
        Call an MPrint API method

        * method: HTTP request method (e.g. POST)
        * path: Path of the endpoint e.g. /areas
        * params: Dictionary of 
        """
        method = method.upper()

        if method in [ 'POST', 'PUT' ]:
            body = urllib.urlencode(params)
            uri = self._build_uri(path)
        else:
            body = None
            uri = self._build_uri(path, params)

        req = urllib2.Request(
            uri,
            body
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


