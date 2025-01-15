# tp3

## 🌞 Script autoconfig.sh

```bash
#!/bin/bash

if [ "$(id -u)" -ne 0 ]; then
  echo "$(date '+%H:%M:%S') [ERROR] Ce script doit être exécuté en root."
  exit 1
fi

echo "$(date '+%H:%M:%S') [INFO] Le script d'autoconfiguration a démarré"

if sestatus | grep -q "Current mode: enforcing"; then
  echo "$(date '+%H:%M:%S') [WARN] SELinux est toujours activé !"
  setenforce 0
  echo "$(date '+%H:%M:%S') [INFO] Désactivation de SELinux temporaire (setenforce)"
fi


if grep -q "SELINUX=enforcing" /etc/selinux/config; then
  sed -i 's/^SELINUX=enforcing/SELINUX=permissive/' /etc/selinux/config
  echo "$(date '+%H:%M:%S') [INFO] Désactivation de SELinux définitive (fichier de config)"
fi


if systemctl is-active --quiet firewalld; then
  echo "$(date '+%H:%M:%S') [INFO] Service de firewalling firewalld est activé"
else
  echo "$(date '+%H:%M:%S') [ERROR] Le service firewalld n'est pas actif."
  exit 1
fi


current_ssh_port=$(grep ^Port /etc/ssh/sshd_config | awk '{print $2}')
if [ "$current_ssh_port" == "22" ]; then
  echo "$(date '+%H:%M:%S') [WARN] Le service SSH tourne toujours sur le port 22/TCP"
  new_ssh_port=$((1025 + RANDOM % 64510))
  sed -i "s/^#Port 22/Port $new_ssh_port/" /etc/ssh/sshd_config
  sed -i "s/^Port 22/Port $new_ssh_port/" /etc/ssh/sshd_config
  echo "$(date '+%H:%M:%S') [INFO] Modification du fichier de configuration SSH pour écouter sur le port $new_ssh_port/TCP"
  systemctl restart sshd
  echo "$(date '+%H:%M:%S') [INFO] Redémarrage du service SSH"
  firewall-cmd --add-port=${new_ssh_port}/tcp --permanent
  firewall-cmd --remove-port=22/tcp --permanent
  firewall-cmd --reload
  echo "$(date '+%H:%M:%S') [INFO] Ouverture du port $new_ssh_port/TCP dans firewalld"
else
  echo "$(date '+%H:%M:%S') [INFO] Le service SSH ne tourne pas sur le port 22/TCP, il est déjà configuré correctement."
fi


if [ "$(hostnamectl --static)" == "localhost" ]; then
  machine_name=${1:-"default.hostname"}
  hostnamectl set-hostname "$machine_name"
  echo "$(date '+%H:%M:%S') [INFO] Changement du nom pour $machine_name"
else
  echo "$(date '+%H:%M:%S') [INFO] Le nom de la machine est déjà configuré correctement."
fi


admin_user="admin"
if ! id -nG "$admin_user" | grep -qw "wheel"; then
  echo "$(date '+%H:%M:%S') [WARN] L'utilisateur $admin_user n'est pas dans le groupe wheel !"
  usermod -aG wheel "$admin_user"
  echo "$(date '+%H:%M:%S') [INFO] Ajout de l'utilisateur $admin_user au groupe wheel"
fi

echo "$(date '+%H:%M:%S') [INFO] Le script d'autoconfiguration s'est correctement déroulé"


```

# script id.sh (bien coloré comme il faut)

```bash

#!/bin/bash
# Apagnan
# Léni Cinna (aka le mec qui fait la musique la)

USER=$(whoami)
DATE=$(date '+%d/%m/%Y %H:%M:%S')
SHELL=$(echo $SHELL)
OS=$(hostnamectl | grep "Operating System" | cut -d ':' -f2 | xargs)
KERNEL=$(uname -r)
RAM=$(free -mh | awk '/Mem:/ {print $7}')
DISK=$(df -h / | awk 'NR==2 {print $4}')
INODE=$(df -i / | awk 'NR==2 {print $4}')
PACKETS=$(rpm -qa | wc -l)
PORTS=$(ss -tuln | grep LISTEN | wc -l)
PYTHON=$(command -v python3)

# Couleurs
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
BLUE="\e[34m"
CYAN="\e[36m"
MAGENTA="\e[35m"
BOLD="\e[1m"
NC="\e[0m"

echo -e "${GREEN}Salu a toa ${BOLD}${USER}${NC}."
echo -e "${CYAN}Nouvelle connexion ${BOLD}${DATE}${NC}."
echo -e "${YELLOW}Connecté avec le shell ${BOLD}${SHELL}${NC}."
echo -e "${MAGENTA}OS : ${BOLD}${OS}${NC} - Kernel : ${BOLD}${KERNEL}${NC}"
echo -e "${BLUE}Ressources :${NC}"
echo -e "  ${GREEN}- ${BOLD}${RAM}${NC} RAM dispo"
echo -e "  ${YELLOW}- ${BOLD}${DISK}${NC} espace disque dispo"
echo -e "  ${CYAN}- ${BOLD}${INODE}${NC} fichiers restants"
echo -e "${BLUE}Actuellement :${NC}"
echo -e "  ${MAGENTA}- ${BOLD}${PACKETS}${NC} paquets installés"
echo -e "  ${RED}- ${BOLD}${PORTS}${NC} port(s) ouvert(s)"
echo -e "${RED}Python est bien installé sur la machine au chemin : ${BOLD}${PYTHON}${NC}"

```
