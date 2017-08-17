import os
import linecache
from utils.UrlUtils import UrlUtils


class Bouncer:
    def __init__(self, domain):
        self.__setDomain(domain)
        self._readUrls = []
        self._path = ''
        self._currentLine = 0
        self._fileLines = ''
        self._allpages = []
        self._external = []

    def __setDomain(self, domain):
        tmp = domain
        if UrlUtils.containsHTTP(domain):
            tmp = tmp.replace('http://','').replace('https://','')
        if UrlUtils.containsWWW(tmp):
            tmp = tmp.replace('www.','')
        self._domain = tmp.split('/')[0]

    def getDomain(self):
        return self._domain

    def getReadUrl(self):
        return self._readUrls

    def isReadUrl(self, url):
        if url in self.getReadUrl():
            return False
        return True

    def setWordlist(self, path):
        self._path = os.path.abspath(path)
        self._fileLines = len(open(self.getWordlist()).readlines())

    def getWordlist(self):
        return self._path

    def getCurrentWordFromWordlist(self):
        self._currentLine += 1
        if self._currentLine < self._fileLines:
            return linecache.getline(self.getWordlist(), self._currentLine).replace('\n','')
        return None

    def setExternals(self, externalLink):
        self._external.append(externalLink)
        list(set(self._external))

    def getExternals(self):
        return self._external

    def searchAndAddLinksFromMain(self, html, url):
        urls = []
        for link in html.findAll('a', href = True):
            page = link['href']
            if page[0] != '#' and url not in page and not UrlUtils.containsHTTP(page):
                urls.append('http://' + url + '/' + page)
            else:
                if url not in page and not UrlUtils.externalLink(url, page):
                    urls.append(url + '/' + page)
                else:
                    if url in page:
                        urls.append(page)
                    else:
                        if UrlUtils.externalLink(url, page):
                            self.setExternals(page)

        list(set(urls))
        return urls
