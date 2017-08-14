#!/bin/bash


if [[ "$(whoami)" == "root" ]]; then
	defaultDir="$(pwd)"
	pipUrl="https://bootstrap.pypa.io/get-pip.py"

	# Em alguns ambientes o wget padrão é bloqueado, com uma pequena definição de 
	# user-agent, isso é consertado. xD

	cd /tmp && wget "$pipUrl" --user-agent 'Firefox HueBr' -v

	sudo python3 get-pip.py

	cd "$defaultDir"

	sudo pip install -r requirements.txt

else

	echo "Você precisa ser um usuário root"

fi

