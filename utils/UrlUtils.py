class UrlUtils:
    @staticmethod
    def containsWWW(url):
        return 'www.' in url

    @staticmethod
    def httpsTohttp(url):
        if 'http://' in url:
            return url
        elif 'https://' in url:
            return url.replace('https://', 'http://')
        return ''

    @staticmethod
    def httpAndWww(url):
        if UrlUtils.containsWWW(url):
            if UrlUtils.containsHTTP(url):
                return url
            elif UrlUtils.httpsTohttp is False:
                url = 'http://' + url
                return url
        if UrlUtils.containsHTTP(url):
            if UrlUtils.containsWWW(url):
                return url
            else:
                url = UrlUtils.httpsTohttp(url)
                url = url.replace('http://', '')
                url = 'http://www.' + url
                return url
        return url

    @staticmethod
    def forceLink(url, link):
        if not UrlUtils.externalLink(url, link):
            if UrlUtils.containsHTTP(link):
                link = UrlUtils.httpsTohttp(link)
                link = link.replace('www', '')
                return 'http://www.' + link
        return False

    @staticmethod
    def containsHTTP(url):
        return 'http://' in url or 'https://' in url

    @staticmethod
    def makeDomain(url, complement):
        if UrlUtils.containsWWW:
            return "http://" + complement.replace("\n", "") + "." + url
        else:
            return "http://" + complement.replace("\n", "") + "." + url.replace("www.", "")

    @staticmethod
    def assertSiteWithFile(url, uri):
        if url[-1] == '/':
            return url + uri
        return url + '/' + uri

    @staticmethod
    def externalLink(url, link):
        return UrlUtils.containsHTTP(link) and url not in link
