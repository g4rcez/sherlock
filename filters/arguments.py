import filters

class getopt(object):
    # Os parameters podem ser uma lista, afim de chamar o método somente uma vez
    @staticmethod
    def get_opt_value(stdin, parameters):
        try:
            for flag in stdin:
                if flag in parameters:
                    return stdin[stdin.index(flag) + 1]
        except:
            return None

    @staticmethod
    def get_opt(stdin, parameters):
        try:
            for flag in stdin:
                if flag in parameters:
                    return True
        except:
            return False

    @staticmethod
    def required_arg(stdin, parameters):
        if getopt.get_opt_value(stdin, parameters) == None:
            return input('Informe o argumento ' + ''.join(parameters[0]) + ' (obrigatório): ')
        return getopt.get_opt_value(stdin, parameters)
