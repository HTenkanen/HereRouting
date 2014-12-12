from client import Client

class Routing(Client):
    ROUTING_URL = 'routing/7.2/'

    def routing(self, origin, destination, way_points=None, routing_mode=None, transport_mode=None, traffic_mode=None, resource=None):
        routing_url = "%s%s" % (self.ROUTING_URL, resource)

        parameters = dict(
            origin = self.require_latlon(origin),
            destination = self.require_latlon(destination),
            waypoints=way_points,
            routing_mode=routing_mode,
            transport_mode=transport_mode,
            traffic_mode=traffic_mode
        )
        return self._make_request(routing_url, parameters, "routes")


