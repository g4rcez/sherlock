from utils.ExtensionFiles import ExtensionsFile
from utils.UrlUtils import UrlUtils


class Files:
    def __init__(self):
        self._list = []

    def getHTML(self):
        return self._html

    def setHTML(self, html):
        self._html = html

    def getFiles(self):
        return self._list

    # @param List
    # return void

    def __setNewFilesInList(self, arrayList):
        for thisFile in arrayList:
            if ExtensionsFile.hasExtension(thisFile):
                self._list.append(thisFile)
        list(set(self._list))

    # @param BeautifulSoup4Obj, string
    # @return void

    def setFiles(self, html, url):
        self.setHTML(html)
        internalList = []
        for files in self.getHTML().findAll('a', href = True):
            linkToFile = files['href']
            if UrlUtils.containsHTTP(linkToFile) is False:
                linkToFile = UrlUtils.assertSiteWithFile(url, linkToFile)
            internalList.append(linkToFile)
        self.__setNewFilesInList(internalList)