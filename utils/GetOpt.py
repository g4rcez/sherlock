class Getopt:
    # Os parameters podem ser uma lista, afim de chamar o método somente uma vez
    @staticmethod
    def getOptAndValue(stdin, parameters):
        try:
            for flag in parameters:
                if flag in stdin:
                    return stdin[stdin.index(flag) + 1]
        except:
            return None

    @staticmethod
    def getOpt(stdin, parameters):
        try:
            for flag in parameters:
                if flag in stdin:
                    return True
        except:
            return False

    @staticmethod
    def requiredArgs(stdin, parameters):
        argument = Getopt.getOptAndValue(stdin, parameters)
        if argument == None:
            argument = input('Informe o argumento ' + ''.join(parameters[0]) + ' (obrigatório): ')
        return argument
