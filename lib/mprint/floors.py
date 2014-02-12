import mprint

class Floors(mprint.Client):

    def __init__(self, credentials, *args, **kwargs):
        super(Floors, self).__init__(credentials, *args, **kwargs)

    def floors(self, building_id):
        method = 'GET'
        uri = '/floors'
        params = {
            'buildingId': buildingId,
            }
        (res, floors) = json_call(method, uri, params)
        return floors

    def floor(self, floor_id):
        method = 'GET'
        uri = '/floors/' + floor_id
        (res, floor) = json_call(method, uri)
        return floor

