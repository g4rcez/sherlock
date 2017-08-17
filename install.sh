#!/bin/bash
if [[ "$(whoami)" == "root" ]]; then
	cd /tmp
	defaultDir="$(pwd)"

	# Em alguns ambientes o wget padrão é bloqueado, com uma pequena definição de
	# user-agent, isso é consertado. xD

	wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz --user-agent Firefox| tar -xf
	cd Python-3.6.2/
	sudo ./configure && sudo make && sudo make install

	# Mesma coisa citada anteriormente
	cd /tmp && wget "https://bootstrap.pypa.io/get-pip.py" --user-agent 'Firefox HueBr' -v

	sudo python3 get-pip.py
	cd "$defaultDir"
	sudo pip install -r requirements.txt
else
	echo "Você precisa ser um usuário root"
fi
