from parsers.Parser import Parser
from utils.UrlUtils import UrlUtils
from utils.ExtensionFiles import ExtensionsFile


class Files(Parser):
    def __init__(self, html='', arrayList=[]):
        Parser.__init__(self, html, arrayList)
        self._list = []
        self._externals = []

    def getFiles(self):
        return self._list

    # @param List
    # return void

    def filterFiles(self, arrayList):
        for thisFile in arrayList:
            if ExtensionsFile.hasExtension(thisFile) and not ExtensionsFile.isImage(thisFile):
                self._list.append(thisFile)
        self._list = self.organizeList(self._list)

    # @param BeautifulSoup4Obj, string
    # @return void

    def setFiles(self, html, url):
        self.setHTML(html)
        internalList = []
        for files in self.getHTML().findAll('a', href=True):
            linkToFile = files['href']
            if UrlUtils.externalLink(url, linkToFile) and UrlUtils.containsHTTP(linkToFile):
                self._externals.append(linkToFile)
            else:
                if UrlUtils.containsHTTP(linkToFile) is False:
                    linkToFile = UrlUtils.assertSiteWithFile(url, linkToFile)
                if ExtensionsFile.hasExtension(linkToFile) and not UrlUtils.externalLink(url, linkToFile):
                    internalList.append(linkToFile)
        self.filterFiles(internalList)
