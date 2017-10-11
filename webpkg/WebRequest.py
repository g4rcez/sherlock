import requests
from json import loads
from webpkg.ForgeRequest import ForgeRequest


class WebRequest:
    """
    :parameter string -> url
    :return json
    """
    @staticmethod
    def getJsonFromLink(url):
        request = requests.get(url, headers=ForgeRequest.fakeHeaderHttp(url))
        if request.status_code == 200:
            return loads(request.text)
        return None

    """
    :parameter string -> url
    :return json
    """

    @staticmethod
    def isActiveLink(link):
        try:
            request = requests.get(link)
            return request.status_code
        except (requests.ConnectionError, requests.ConnectTimeout):
            return False
