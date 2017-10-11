class ExtensionsFile:
    @staticmethod
    def hasExtension(file):
        extensions = [
            'jpg', 'jpeg', 'pdf', 'png', 'mp3', 'mp4', 'avi', 'docx', 'doc', 'odt',
            'txt', 'gif', 'js', 'css', 'asp', 'csv', 'exe', 'mov', 'psd', 'tar',
            'zip', 'wav', 'xml', 'xsl', 'ppt', 'pptx', 'm4a', 'ogg', 'm4v',
            'ogv', '3gp', 'mpg', '3gp', 'xls'
        ]
        try:
            ext = file.split('.')[-1]
        except:
            return False
        if ext in extensions:
            return True
        return False

    @staticmethod
    def isImage(file):
        extensions = [
            'jpg', 'jpeg', 'png', 'gif'
        ]
        try:
            ext = file.split('.')[-1]
        except:
            return False
        if ext in extensions:
            return True
        return False

    @staticmethod
    def extensionForWebPage(file):
        extensions = [
            'php', 'html', 'jsp', 'asp', 'xhtml', 'xml', 'jspx', 'jhml',
            'htm', 'wss', 'action', 'pl', 'phtml', 'py', 'rhtml', 'rb',
            'shtml', 'cgi', 'dll', "asx", ''
        ]
        try:
            ext = file.split('.')[-1]
        except:
            return False
        return ext in extensions
