class ExtensionsFile():

    @staticmethod
    def getExtension(file):
        extensions = [
            'jpg', 'jpeg', 'pdf', 'png', 'mp3', 'mp4', 'avi', 'docx', 'doc', 'odt',
            'txt', 'py', 'html', 'php', 'jsp', 'gif', 'cgi', 'pl', 'js', 'css', 'asp',
            'csv', 'exe', 'mov', 'psd', 'tar', 'zip', 'wav', 'xml', 'xsl', 'ppt', 'pptx',
            'm4a', 'ogg', 'm4v', 'ogv', '3gp', 'mpg', '3gp'
        ]
        try:
            ext = file.split('.')
            ext = ext[-1]
            if ext in extensions:
                return True
            return False
        except:
            return False