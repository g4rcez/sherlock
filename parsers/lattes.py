import re
import parsers

class lattes():
    def __init__(self, html):
        self.html = html

    def get_lattes(self):
        lattes = self.html.findAll('a', attrs={'href': re.compile(".*lattes")})
        lattes_list = []
        if lattes > 0:
            for curriculo in lattes:
                link = re.sub('.*href="', '', str(curriculo))
                link = re.sub('".*', ' ', str(link))
                lattes_list.append(link)
            return lattes_list
        return None
