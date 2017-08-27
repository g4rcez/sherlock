class PageCreator:
    def __init__(self, fileName, domain, ip, addressClass):
        self.setFileNameAndDirectory(fileName)
        self.setDomain(domain)
        self.setIp(ip)
        self.setAddress(addressClass)

    def getFile(self):
        return self._file

    def getDomain(self):
        return self._domain

    def getIp(self):
        return self._ip

    def getAddress(self):
        return self._address

    def setFileNameAndDirectory(self, fileName):
        fileName = fileName.replace('.html', '')
        self._file = fileName + '.html'

    def setDomain(self, domain):
        self._domain = domain

    def setIp(self, ip):
        self._ip = ip

    def setAddress(self, addressClass):
        self._address = addressClass

    def headerHTML(self):
        return '''\r<!DOCTYPE html><html><head>
                \r<meta charset="utf-8">
                \r<meta http-equiv="X-UA-Compatible" content="IE=edge">
                \r<meta name="viewport" content="width=device-width, initial-scale=1">
                \r<title>Json Value Template</title>
                \r<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
                \r<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
                \r<link href="https://fonts.googleapis.com/css?family=Montserrat|Source+Sans+Pro" rel="stylesheet">
                \r<link href="style.css" rel="stylesheet"><style>
                \rbody{ font-family: 'Source Sans Pro', sans-serif; color: #121212; }
                \rh1,h2,h3,h4,h5,h6{ font-family: 'Montserrat', sans-serif; }
                \r.box{ border: 1px  groove #121212; border-radius: 0; }
                \r.lists{ font-size: 1.35em; }</style></head>
                \r<h1 class="text-center"><i class="fa fa-globe" aria-hidden="true"></i> Domain: ''' + self.getDomain() + '''</h1>
                \r<h4 class="text-center"><i class="fa fa-server" aria-hidden="true"></i> IP: ''' + self.getIp() + '''</h4>
                \r<a href="index_{self.getFile()}Página Principal</a>"'''

    def footerHTML(self):
        return '''\r<br><br><br><footer class='text-center'>
                \r<h4>Relatório do Fluxo de Informação encontrado por
                \r<a href="https://github.com/vandalvnl/sherlock">Sherlock</a></h4>
                \r<a href="https://github.com/vandalvnl/">Desenvolvedor: Allan Garcez - Vandalvnl</a><br><br>
                \r</footer>
                \r<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
                \r<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
                \r</body></html>'''

    def createIndex(self, arrayListEmail, arrayListLattes, arrayListLinks, arrayListImage, urls, externals):
        index = open('index_' + self.getFile(), 'w')
        index.write(self.headerHTML())
        index.write(
            '''\r<div id="wrapper"><div class="container text-center"><div class="row">
            \r<div class="col-xs-12 col-sm-12 col-md-10 col-lg-10 col-md-offset-1 col-lg-offset-1">
            \r<h2 class="text-center">Índice de informações obtidas</h2><p><ul>
            \r<li><a href="files_''' + self.getFile() + '''" class="lists">Arquivos encontrados: ''' + str(
                len(arrayListLinks)) + '''</a></li>
            \r<li><a href="emails_''' + self.getFile() + '''" class="lists">Emails encontrados: ''' + str(
                len(arrayListEmail)) + '''</a></li>
            \r<li><a href="lattes_''' + self.getFile() + '''" class="lists">Lattes encontrados: ''' + str(
                len(arrayListLattes)) + '''</a></li>
            \r<li><a href="img_''' + self.getFile() + '''" class="lists">Imagens encontradas: ''' + str(
                len(arrayListImage)) + '''</a></li>
            \r<li><a href="urls_''' + self.getFile() + '''" class="lists">Urls encontradas: ''' + str(len(urls)) + '''</a></li>
            \r<li><a href="external_''' + self.getFile() + '''" class="lists">Urls externas: ''' + str(len(externals)) + '''</a></li>
            \r</ul><div class="text-center"><p>'''
        )
        for cep in self.getAddress().getAllCeps():
            self.getAddress().setFullAddress(cep)
            index.write(
                '\r' + self.getAddress().getAddress(cep) + '<br>'
            )
        index.write('''\r</div></p></div></div></div></div>''')
        index.write(self.footerHTML())
        index.close()

    def createEmailsPage(self, arrayListEmail):
        index = open('emails_' + self.getFile(), 'w')
        index.write(self.headerHTML())
        index.write(
            '''\r<div id="wrapper">
            \r<div class="container text-center">
            \r<div class="row">
            \r<div class="col-xs-12 col-sm-12 col-md-10 col-lg-10 col-md-offset-1 col-lg-offset-1">
            \r<h2 class="text-center">Índice de emails obtidos</h2><p><ul>'''
        )
        for email in arrayListEmail:
            index.write(
                '''\r<li>
                \r<a href="mailto:''' + email + '''" class="lists" target="_blank">
                \r''' + email + ''' <i class="fa fa-envelope" aria-hidden="true"></i>
                \r</a></li>'''
            )
        index.write(
            '''\r</div></div></div></div></div>'''
        )
        index.write(self.footerHTML())
        index.close()

    def createFilesPage(self, arrayListLinks):
        index = open('files_''' + self.getFile(), 'w')
        index.write(self.headerHTML())
        index.write(
            f'''\r<div id="wrapper"><div class="container text-center"><div class="row">
            \r<div class="col-xs-12 col-sm-12 col-md-10 col-lg-10 col-md-offset-1 col-lg-offset-1">
            \r<h2 class="text-center">Índice de arquivos obtidos</h2><p><ul>'''
        )
        count = 1
        for files in arrayListLinks:
            index.write(
                '''\r<li><a href="''' + files + '''" class="lists" target="_blank">
                \r''' + str(count) + ''' - ''' + files.split('/')[-1] + ''' -
                \rLink <i class="fa fa-external-link" aria-hidden="true"></i>
                \r</a></li>'''
            )
            count += 1

        index.write('''\r</div></div></div></div></div>''')
        index.write(self.footerHTML())
        index.close()

    def createImgPage(self, arrayListImage):
        index = open('img_' + self.getFile(), 'w')
        index.write(self.headerHTML())
        index.write(
            '''\r<div id="wrapper"><div class="container text-center"><div class="row">
            \r<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
            \r<h2 class="text-center">Índice de imagens obtidas</h2>
            \r<div class="row">'''
        )
        count = 5
        for img in arrayListImage:
            output = '''\r<div class="col-xs-12 col-sm-12 col-lg-2 col-md-2">
            \r<img src="''' + img + '''" class="img-responsive"/>
            \r<a href="''' + img + '''" class="text-center" target="_blank">Link para imagem <i class="fa fa-external-link" aria-hidden="true"></i></a>
            \r</div>
            '''
            if count == 0:
                index.write(
                    '''\r<div class='row'>
                    ''' + output + '''
                    \r</div>'''
                )
                count = 6
            else:
                index.write(output)
            count -= 1
        index.write('''\r</div></div></div></div></div>''')
        index.write(self.footerHTML())
        index.close()

    def createLattesPage(self, arrayListLattes):
        index = open('lattes_' + self.getFile(), 'w')
        index.write(self.headerHTML())
        index.write(
            '''\r<div id="wrapper">
            \r<div class="container text-center">
            \r<div class="row">
            \r<div class="col-xs-12 col-sm-12 col-md-10 col-lg-10 col-md-offset-1 col-lg-offset-1">
            \r<h2 class="text-center">Índice de arquivos obtidos</h2><p><ul>'''
        )
        count = 1
        for lattes in arrayListLattes:
            index.write(
                '''\r<li><a href="''' + lattes + '''" class="lists" target="_blank">
                \r''' + lattes.split('/')[-1] + ''' - Link <i class="fa fa-external-link" aria-hidden="true"></i>
                \r</a></li>'''
            )
        index.write('''\r</div></div></div></div></div>''')
        index.write(self.footerHTML())
        index.close()

    def createUrlsPage(self, uri):
        index = open('urls_' + self.getFile(), 'w')
        index.write(self.headerHTML())
        index.write(
            '''\r<div id="wrapper">
            \r<div class="container text-center">
            \r<div class="row">
            \r<div class="col-xs-12 col-sm-12 col-md-10 col-lg-10 col-md-offset-1 col-lg-offset-1">
            \r<h2 class="text-center">Índice de arquivos obtidos</h2><p><ul>'''
        )
        count = 1
        for files in uri:
            index.write(
                '''\r<li><a href="''' + files + '''" class="lists" target="_blank">
                \r''' + str(count) + ''' - ''' + files + ''' -
                \rLink <i class="fa fa-external-link" aria-hidden="true"></i>
                \r</a></li>'''
            )
            count += 1
        index.write('''\r</div></div></div></div></div>''')
        index.write(self.footerHTML())
        index.close()

    def createExternalPage(self, external):
        index = open('external_' + self.getFile(), 'w')
        index.write(self.headerHTML())
        index.write(
            '''\r<div id="wrapper">
            \r<div class="container text-center">
            \r<div class="row">
            \r<div class="col-xs-12 col-sm-12 col-md-10 col-lg-10 col-md-offset-1 col-lg-offset-1">
            \r<h2 class="text-center">Índice de links quebrados</h2><p><ul>'''
        )
        count = 1
        for files in external:
            index.write(
                '''\r<li><a href="''' + files + '''" class="lists" target="_blank">
                \r''' + str(count) + ''' - ''' + files + ''' -
                \rLink <i class="fa fa-trash" aria-hidden="true"></i>
                \r</a></li>'''
            )
            count += 1
        index.write('''\r</div></div></div></div></div>''')
        index.write(self.footerHTML())
        index.close()
