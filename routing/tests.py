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
    #waypoints = {'waypoint0': {'lat': 60.2294, 'lon': 25.0278}, 'waypoint1': {'lat': 60.2294, 'lon': 25.0278}}

    origin = {'lat': 60.2294, 'lon': 25.0278}
    dest = {'lat': 60.1606, 'lon': 24.9407}
    departure = "2015-01-14T08:00:00Z"

    results = api.routing(origin = origin, destination=dest, departure = departure) #, routing_mode='fastest', transport_mode='car', traffic_mode='enabled', resource='calculateroute') #origin=origin, destination=destination

    print results

test_url()


