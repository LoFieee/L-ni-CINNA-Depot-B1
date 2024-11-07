# FILES AND USERS

## 1. Fichier

##### 🌞 Trouver le chemin vers le répertoire personnel de votre utilisateur

```bash
echo $HOME
```

##### 🌞 Vérifier les permissions du répertoire personnel de votre utilisateurs

```bash
ls -l $HOME
```

##### 🌞 Trouver le chemin du fichier de configuration du serveur SSH

```bash
ls -l /etc/ssh/sshd_config
```

##### 🌞 Trouver le chemin du fichier de logs SSH

```bash
ls -l /var/log/auth.log
```
# 2. Users


##### 🌞 Créer un nouvel utilisateur

```bash
sudo adduser user
```

##### 🌞 Prouver que cet utilisateur a été créé

```bash
cat /etc/passwd | grep user
```


##### 🌞 Déterminer le hash du password de l'utilisateur marmotte

```bash
sudo grep marmotte /etc/shadow
```

##### 🌞 Tapez une commande pour vous déconnecter : fermer votre session utilisateur

```bash
exit
```

##### 🌞 Assurez-vous que vous pouvez vous connecter en tant que l'utilisateur marmotte

```bash
ssh marmotte@localhost
```

# Programmes et paquets 

## 1. Programmes et processus

##### 🌞 Lancer un processus sleep

```bash
sleep 1000 &
```

##### 🌞 Terminez le processus sleep depuis le deuxième terminal

```bash
ps aux | grep sleep
kill -9 <PID de sleep>
```

##### 🌞 Terminez le processus sleep depuis le deuxième terminal

```bash
ps aux | grep sleep
kill -9 <PID de sleep>
```

##### 🌞 Lancer un nouveau processus sleep, mais en tâche de fond

```bash
sleep 1000 &
```

##### 🌞 Visualisez la commande en tâche de fond

```bash
jobs
```

##### 🌞 Trouver le chemin où est stocké le programme sleep

```bash
which sleep
```

##### 🌞 Vérifier que les commandes sleep, ssh, et ping sont bien des programmes stockés dans l'un des dossiers listés dans votre PATH

```bash
which sleep
which ssh
which ping
```

## 2. Paquets

##### 🌞 Installer le paquet firefox

```bash
sudo apt install firefox
```

##### 🌞 Utiliser une commande pour lancer Firefox

```bash
firefox
```

# Poupée russe

##### 🌞 Récupérer le fichier meow

```bash
wget https://gitlab.com/it4lik/b1-os/-/raw/main/tp/2/meow?inline=false
```


##### 🌞 Trouver le dossier dawa/

```bash
file meow
mv meow meow.zip
unzip meow.zip
cd dawa
```

##### 🌞 Dans le dossier dawa/, déterminer le chemin vers

1. le fichier meow récupéré est une archive compressée
2. utilisez la commande file /path/vers/le/fichier pour déterminer le type du fichier
3. renommez-le fichier correctement (si c'est une archive compressée ZIP, il faut ajouter .zip à son nom)
4. décompressez l'archive
5. répétez ces opérations jusqu'à trouver le dossier dawa/

```bash
file meow
mv meow meow.zip
unzip meow.zip
cd dawa
```

##### 🌞 Dans le dossier dawa/, déterminer le chemin vers


```bash

find . -type f -size 15M
find . -type f -size 7c
find . -type f -name cookie
find . -type f -name ".*"
find . -type f -newermt 2014-01-01 ! -newermt 2015-01-01
find . -path "*/folderX/folderX/folderX/folderX/folderX/*"
```

