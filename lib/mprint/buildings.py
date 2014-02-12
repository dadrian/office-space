import mprint

class Buildings(mprint.Client):

    def __init__(self, credentials, *args, **kwargs):
        super(Buildings, self).__init__(self, credentials, args, kwargs)

    def buildings(self):
        method = 'GET'
        path = '/buildings'
        (res, buildings) = self.json_call(method, path)
        return buildings

    def building(self, id):
        method = 'GET'
        path = ''.join(['/buildings/', str(id)])
        (res, building) = self.json_call(method, path)
        return building
        
