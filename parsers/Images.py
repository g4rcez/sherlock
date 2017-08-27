from parsers.Parser import Parser
from utils.UrlUtils import UrlUtils
from utils.ExtensionFiles import ExtensionsFile


class Images(Parser):
    def __init__(self, html = '', arrayList = []):
        Parser.__init__(self, html, arrayList)
        self._imgs = []

    def setImages(self, html, url):
        self.setHTML(html)
        imgList = self.getHTML().findAll('img')
        images = []
        for img in imgList:
            linkToImg = img.get('src')
            if UrlUtils.containsHTTP(img.get('src')) is False:
                linkToImg = UrlUtils.assertSiteWithFile(url, img.get('src'))
            images.append(linkToImg.strip())
        self.__allImages(images)


    def __allImages(self, arrayList):
        for img in arrayList:
            if ExtensionsFile.isImage(img):
                self._imgs.append(img)
            self._imgs = self.organizeList(arrayList)

    def getImages(self):
        return self._imgs
