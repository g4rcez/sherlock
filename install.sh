#!/bin/bash
if [[ "$(whoami)" == "root" ]]; then
	cd /tmp

	defaultDir="$(pwd)"
	pipUrl="https://bootstrap.pypa.io/get-pip.py"


	wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz | tar -xf
	cd Python-3.6.2/
	sudo ./configure && sudo make && sudo make install

	# Em alguns ambientes o wget padrão é bloqueado, com uma pequena definição de
	# user-agent, isso é consertado. xD

	cd /tmp && wget "$pipUrl" --user-agent 'Firefox HueBr' -v

	sudo python3 get-pip.py

	cd "$defaultDir"

	sudo pip install -r requirements.txt

else

	echo "Você precisa ser um usuário root"

fi
