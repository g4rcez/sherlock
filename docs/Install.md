# Guia de Instalação

Para aqueles que querem fazer uma instalação na mão, aqui está o guia:

> $ cd /tmp

> $ wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz | tar -xf

> $ cd Python-3.6.2/

> $ sudo ./configure && sudo make && sudo make install

> $ cd /tmp

> $ wget https://bootstrap.pypa.io/get-pip.py

> $ sudo python3.6 get-pip.py

> $ sudo pip install requests bs4

Caso você queira fazer a instalação utilizando gerenciadores de dependência, pode seguir os seguintes passos:

### Ubuntu, Debian, Kali, KurupiraOS, Parrot...
> sudo apt install python3.6 python3-pip


### CentOS, Fedora...
> sudo yum install python3.6 python3-pip

### Arch Linux, Manjaro, Antergos...
> sudo pacman -S python python-pip

**Verifique se o pacote Python3.6 encontra-se disponível em seus repositórios.**

Com todas as dependências resolvidas, você pode executar:

> sudo pip install requests bs4

Com estes passos realizados, você poderá executar o Sherlock sem problemas, apenas seguindo as opções de ajuda mostradas em tela. Caso ainda tenha dúvidas, por favor, abra um Issue com todas as perguntas necessárias que estarei disponível para ajudar.
