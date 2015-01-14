from client import Client

class Routing(Client):
    ROUTING_URL = 'routing/7.2/'

    def routing(self, origin=None, destination=None, departure=None, waypoints=None, routing_mode='fastest', transport_mode='car', traffic_mode='enabled', resource='calculateroute'):
        routing_url = "%s%s" % (self.ROUTING_URL, resource)

        mode = "%s;%s;traffic:%s" % (routing_mode, transport_mode, traffic_mode)

        parameters = dict(
            waypoint0 = "geo!%s" % self.require_latlon(origin),
            waypoint1 = "geo!%s" % self.require_latlon(destination),
            mode = mode,
            departure = departure

        )
        return self._make_request(routing_url, parameters, "routes")


