__author__ = 'hentenka'
from routing import Routing

def test_client():
    app_code = 'AJKnXv84fjrb0KIHawS0Tg'
    app_id = 'DemoAppId01082013GAL'

    try:
        api = Routing(app_code=app_code, app_id=app_id)
    except:
        raise Exception
    return api

def test_url():
    api = test_client()
    origin = {'lat': 57.3434, 'lon': 24.45454}
    destination = {'lat': 55.3231, 'lon': 22.433}
    api.routing(origin=origin, destination=destination, routing_mode='fastest', transport_mode='car', traffic_mode='enabled', resource='calculateroute')

test_url()


