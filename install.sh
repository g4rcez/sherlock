#!/bin/bash
if [[ $(whoami) == "root" ]]; then
mkdir -p /usr/share/sherlock
cp -rf * /usr/share/sherlock/
echo '#!/bin/sh
cd /usr/share/sherlock
python3 Sherlock "$@"' > /usr/bin/sherlock
chmod +x /usr/bin/sherlock
else
    echo "[!] Você deve ser um usuário root para instalar o script"
fi
