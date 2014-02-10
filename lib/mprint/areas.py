import mprint

class Area(mprint.Client):

    def __init__(self, *args, **kwargs):
        super(Area, self).__init__(*args, **kwargs)

    def get_areas(self):
        method = 'GET'
        path = '/areas'
        params = {}
        (res, data) = self.api_call(method, path, params)
        return data
