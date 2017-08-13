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

    def __setDomain(self, domain):
        tmp = domain
        if UrlUtils.containsHTTP(domain):
            tmp = tmp.replace('http://','').replace('https://','')
        if UrlUtils.containsWWW(tmp):
            tmp = tmp.replace('www.','')
        domain = tmp.split('/')[0]
        self._domain = domain

    def getDomain(self):
        return self._domain

    def getReadUrl(self):
        return self._readUrls

    def setReadUrl(self, url):
        if url not in self.getReadUrl():
            self._readUrls.append(url)
        self._readUrls.sort()

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

    def searchAndAddLinksFromMain(self, html, url):
        urls = []
        for link in html.findAll('a', href = True):
            page = link['href']
            if url in page:
                urls.append(page)
        return urls
