import mprint
import json

class Area(mprint.Client):

    AREAS = [ 'Arbor Lakes', 'Central Campus', 'Hill, Medical Center', 'North Campus', 'South Campus']

    def __init__(self, credentials, *args, **kwargs):
        super(Area, self).__init__(credentials, *args, **kwargs)

    def areas(self):
        method = 'GET'
        path = '/areas'
        params = {}
        (res, data) = self.api_call(method, path)
        areas = json.loads(data)
        return areas

    def area(self, area_id):
        method = 'GET'
        path = ''.join(['/areas/', str(area_id)])
        params = {}
        (res, area) = self.json_call(method, path)
        return area

if __name__ == '__main__':
    import sys
    import cosign
    username = sys.argv[1]
    password = sys.argv[2]
    creds = cosign.Credentials(username, password)

    area_client = Area(creds)
    print area_client.areas()
    print area_client.area(1)


