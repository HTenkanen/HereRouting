# -*- coding: utf-8 -*-
import requests
import urlparse
#from routing import status
#from routing import errors

class Client(object):
    """
    Base class for Nokia Here Routing API endpoints.

    Inspired by: https://github.com/swistakm/python-gmaps
    """

    # Test environment
    BASE_API_HTTP_URL = "http://route.cit.api.here.com"

    # Production environment
    # BASE_API_HTTP_URL = "http://route.api.here.com"

    def __init__(self, app_code=None, app_id=None):
        self.app_code = app_code
        self.app_id = app_id
        self.base = self.BASE_API_HTTP_URL


    def _make_request(self, url, parameters, result_key):
        """Make http/https request to Here Routing API.

        Method prepares url parameters, drops None values, and gets default
        values. Finally makes request using protocol assigned to client and
        returns data.

        """

        #url = urlparse.urljoin(urlparse.urljoin(self.base, url), ".json")
        url = "%s%s" %(urlparse.urljoin(self.base, url), ".json")


        # drop all None values and use defaults if not set
        parameters = {key: value for key, value in parameters.items() if
                      value is not None}

        if self.app_code:
            parameters["app_code"] = self.app_code
        if self.app_id:
            parameters["app_id"] = self.app_id

        raw_response = requests.get(url, params=parameters)
        response = raw_response.json()

        return response
        """if response["status"] == "OK": #status.OK and result_key is not None:
            return response[result_key]
        elif response["status"] == "OK":  #status.OK:
            del response["status"]
            return response
        else:
            response["url"] = raw_response.url
            raise Exception
            #raise errors.EXCEPTION_MAPPING.get(
            #    response["status"],
            #    errors.HereException
            #)(response)
        """
    @staticmethod
    def require_latlon(location):
        if isinstance(location, dict):
            try:
                output = "%f,%f" % (location["lat"], location["lon"])
            except KeyError:
                raise TypeError(
                    "%s is invalid location object" % str(location)
                )
        elif hasattr(location, "__iter__") and len(location) == 2:
            output = "%f,%f" % (location[0], location[1])
        elif hasattr(location, "lat") and hasattr(location, "lon"):
            output = "%f,%f" % (location.lat, location.lon)
        else:
            raise TypeError("%s is invalid location object" % str(location))
        return output
