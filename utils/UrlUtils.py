import requests


class UrlUtils:
    @staticmethod
    def containsWWW(url):
        if 'www.' in url:
            return True
        return False

    @staticmethod
    def httpsTohttp(url):
        if 'http://' in url:
            return url
        elif 'https://' in url:
            return url.replace('https://', 'http://')
        return False

    @staticmethod
    def containsHTTP(url):
        if 'http://' in url:
            return True
        elif 'https://' in url:
            return True
        return False

    @staticmethod
    def makeDomain(url, complement):
        if UrlUtils.containsWWW:
            return "http://" + complement.replace("\n", "") + "." + url
        else:
            return "http://" + complement.replace("\n", "") + "." + url.replace("www.", "")

    @staticmethod
    def isValidUrl(url):
        if UrlUtils.containsHTTP(url):
            if requests.get(url).status_code == 200:
                return True
        return False

    @staticmethod
    def assertSiteWithFile(url, uri):
        if url[-1] == '/':
            return url + uri
        return url + '/' + uri

    @staticmethod
    def externalLink(url, link):
        if UrlUtils.containsHTTP(link) and url not in link:
            return True
        return False
