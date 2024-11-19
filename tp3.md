# Utilisateurs

## 1 - Liste des users

#####  Afficher la ligne du fichier qui concerne votre utilisateur
```
lofie@vbox:~$ cat /etc/passwd | grep lofie
lofie:x:1000:1000:lofie CINNA,,,:/home/lofie:/bin/bash
```

### Afficher la ligne du fichier qui concerne votre utilisateur ET celle de root en même temps
```
lofie@vbox:~$ cat /etc/passwd | grep -e lofie -e root
```

### Afficher la liste des groupes d'utilisateurs de la machine
```
lofie@vbox:~$ cat /etc/group
```

### Afficher la ligne du fichier qui concerne votre utilisateur ET celle de root en même temps

```
lofie@vbox:~$ cat /etc/passwd | grep -e lofie -e root
```


## 2 - Hash des passwords
### Afficher la ligne qui contient le hash du mot de passe de votre utilisateur

```
lofie@vbox:~$ sudo cat /etc/shadow | grep lofie
```


## 3 - Sudo


## B. Practice
### Créer un groupe d'utilisateurs

```
sudo groupadd stronk_admins
```
### Créer un utilisateur

```
sudo useradd imbob
sudo passwd imbob
sudo usermod -aG stronk_admins imbob
```
### Prouver que l'utilisateur imbob est créé


```
lofie@vbox:~$ cat /etc/passwd | grep imbob
```
### Prouver que l'utilisateur imbob a un password défini

```
lofie@vbox:~$ sudo cat /etc/shadow | grep imbob
```

### Prouver que l'utilisateur imbob appartient au groupe stronk_admins

```
lofie@vbox:~$ cat /etc/group | grep imbob
```
### Créer un deuxième utilisateur

```
lofie@vbox:~$ sudo useradd imnotbobsorry
lofie@vbox:~$ sudo passwd imnotbobsorry
```

### Modifier la configuration de sudo pour que

```
lofie@vbox:~$ sudo visudo # pour modifier le dossier et ajouter %stronk_admins ALL=(ALL) NOPASSWD: ALL
lofie@vbox:~$ su imbob  
sudo cat /etc/passwd
```

### Créer le dossier /home/goodguy (avec une commande)
```
lofie@vbox:/home$ sudo mkdir goodguy
```

### Changer le répertoire personnel de imbob

```
lofie@vbox:~$ sudo usermod -d /home/goodguy -m imbob
lofie@vbox:~$ cat /etc/passwd | grep imbob
```

### Créer le dossier /home/badguy


```
lofie@vbox:/home$ sudo mkdir badguy
lofie@vbox:/home$ sudo usermod -d /home/badguy -m imnotbobsorry
```


🌞 Prouver que les permissions du dossier /home/gooduy sont incohérentes



```
lofie@vbox:/home$ ls -la
```

🌞 Modifier les permissions de /home/goodguy

```
lofie@vbox:/home$ sudo chown imbob:imbob goodguy
lofie@vbox:/home$ sudo chmod 700 goodguy
lofie@vbox:/home$ ls -la
```
🌞 Modifier les permissions de /home/badguy


```
lofie@vbox:/home$ sudo chown imnotbobsorry:imnotbobsorry badguy
lofie@vbox:/home$ sudo chmod 700 badguy
lofie@vbox:/home$ ls -l
```

🌞 Connectez-vous sur l'utilisateur imbob
```
lofie@vbox:~$ su imbob
```
🌞 Connectez-vous sur l'utilisateur imnotbobsorry

```
$ su imnotbobsorry
```

# 1. Jouer avec la commande ps

### Affichez les processus bash

- une commande ps puis vous filtrez la sortie pour afficher que les bash

```
lofie@vbox:~$ ps -ef | grep bash
```



### Affichez tous les processus lancés par votre utilisateur


```
lofie@vbox:~$ ps -ef | grep "lofie"
```


### Affichez le top 5 des processus qui utilisent le plus de RAM


```
lofie@vbox:~$ ps aux --sort=-%mem | head -n 6 | awk '{print $11, $4}'
```

### Affichez le PID du processus du service SSH

```
lofie@vbox:~$ ps -ef | grep sshd | head -n 1


### Affichez le nom du processus avec l'identifiant le plus petit

```
lofie@vbox:~$ ps -ef --sort=pid | head -n 2
```


## 1. Parent, enfant, et meurtre

### Déterminer le PID de votre shell actuel

```
lofie@vbox:~$ echo $$
1871
```
### Déterminer le PPID de votre shell actuel

```
lofie@vbox:~$ ps -ef | grep 885 | head -n 1

### Déterminer le nom de ce processus

```
lofie@vbox:~$ ps -ef | grep 883 | head -n 1
```
###  Lancer un processus sleep 9999 en tâche de fond

```
lofie@vbox:~$ sleep 9999 &
lofie@vbox:~$ ps -ef | grep sleep | head -n 1

```

🌞 S'assurer que le service ssh est démarré

```
lofie@vbox:~$ systemctl status
```

🌞 Déterminer le port sur lequel écoute le service SSH
```
lofie@vbox:~$ sudo ss -lnpt | grep sshd
```

🌞 Consulter les logs du service SSH

```
lofie@vbox:~$ journalctl | grep sshd
```

🌞 Identifier le fichier de configuration du serveur SSH

```
lofie@vbox:/etc$ ls -l | grep ssh
```
🌞 Modifier le fichier de conf

```
lofie@vbox:/etc$ echo $RANDOM
lofie@vbox:/etc/ssh$ cat sshd_config | grep Port | head -n 1
```
🌞 Redémarrer le service

```
PS C:\Users\lofie> ssh lofie@192.168.163.10 -p 7551

```

🌞 Effectuer une connexion SSH sur le nouveau port

```
ssh lofie@192.168.166.13 -p 7551
```


🌞 Trouver le fichier ssh.service
```
lofie@vbox:/etc/ssh$ sudo find / -name "ssh.service"
```
🌞 Déterminer quel est le programme lancé

```
lofie@vbox:/usr/lib/systemd/system$ cat ssh.service | grep ExecStart=
ExecStart=/usr/sbin/sshd -D $SSHD_OPTS
```
🌞 Déterminer le dossier qui contient la commande python3

```
lofie@vbox:~$ which python3
/usr/bin/python3
```

🌞 Créez un fichier /etc/systemd/system/meow_web.service

```
lofie@vbox:/etc/systemd/system$ sudo touch meow_web.service
lofie@vbox:/etc/systemd/system$ sudo nano meow_web.service
lofie@vbox:/etc/systemd/system$ ls | grep meow_web.service
```

🌞 Indiquez à l'OS que vous avez modifié les services

```
lofie@vbox:/etc/systemd/system$ sudo systemctl daemon-reload
```
🌞 Démarrez votre service

```
lofie@vbox:/etc/systemd/system$ sudo systemctl start meow_web
```

🌞 Déterminer le PID du processus Python en cours d'exécution
Le PID est 967
```
lofie@vbox:/etc/systemd/system$ ps -ef | grep python3
```
🌞 Prouvez que le programme écoute derrière le port 8888
```
lofie@vbox:~$ sudo ss -lnpt | grep python
```

🌞 Faire en sote que le service se lance automatiquement au démarrage de la machine

```
lofie@vbox:~$ sudo systemctl enable meow_web.service
```
