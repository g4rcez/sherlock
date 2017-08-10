class Getopt:
    # Os parameters podem ser uma lista, afim de chamar o método somente uma vez
    @staticmethod
    def getOptAndValue(stdin, parameters):
        try:
            for flag in stdin:
                if flag in parameters:
                    return stdin[stdin.index(flag) + 1]
        except:
            return None

    @staticmethod
    def getOpt(stdin, parameters):
        try:
            for flag in stdin:
                if flag in parameters:
                    return True
        except:
            return False

    @staticmethod
    def requiredArgs(stdin, parameters):
        if Getopt.getOptAndValue(stdin, parameters) == None:
            return input('Informe o argumento ' + ''.join(parameters[0]) + ' (obrigatório): ')
        return Getopt.getOptAndValue(stdin, parameters)
