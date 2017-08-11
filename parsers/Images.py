import utils
from utils.UrlUtils import UrlUtils
from utils.ExtensionFiles import ExtensionsFile


class Images:
    def __init__(self, html):
        self.setHTML(html)
        self._imgs = []

    def getHTML(self):
        return self._html

    def setHTML(self, html):
        self._html = html

    def setImages(self, url):
        imgList = self.getHTML().findAll('img')
        images = []
        for img in imgList:
            if img not in images:
                linkToImg = img.get('src')
                if UrlUtils.containsHTTP(img.get('src')) is False:
                        linkToImg = url + img.get('src')
                images.append(linkToImg)
        self.__allImages(images)

    def __allImages(self, arrayList):
        for img in arrayList:
            if ExtensionsFile.hasExtension(img) and img not in self._imgs:
                self._imgs.append(img)
        self._imgs.sort()

    def getImages(self):
        return self._imgs
