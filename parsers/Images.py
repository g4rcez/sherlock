import utils
from utils.UrlUtils import UrlUtils


class Images:
    def __init__(self, html):
        self.html = html

    def getImages(self, url):
        imgList = self.html.findAll('img')
        images = []
        for img in imgList:
            if img not in images:
                linkToImg = img.get('src')
                if UrlUtils.containsHTTP(img.get('src')) == False:
                    linkToImg = url + img.get('src')
                images.append(linkToImg)
        images.sort()
        return images
