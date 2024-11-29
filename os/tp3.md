# TP3

## 1. Liste des users

##### 🌞 Afficher la ligne du fichier qui concerne votre utilisateur

```bash
grep -i "lofie" /etc/passwd
```

##### 🌞 Afficher la ligne du fichier qui concerne votre utilisateur ET celle de root en même temps

```bash
grep -i "lofie" /etc/passwd && grep -i "root" /etc/passwd
```

##### 🌞 🌞 Afficher la liste des groupes d'utilisateurs de la machine

```bash
cat /etc/group
```

##### 🌞 Afficher la ligne du fichier qui concerne votre utilisateur ET celle de root en même temps

```bash
grep -i "lofie" /etc/group && grep -i "root" /etc/group
```

## 2. Hash des passwords

##### 🌞 Afficher la ligne qui contient le hash du mot de passe de votre utilisateur

```bash
sudo grep -i "lofie" /etc/shadow
```

## 3. Sudo

##### 🌞 Créer un groupe d'utilisateurs

```bash
sudo groupadd stronk_admins
```

##### 🌞 Créer un utilisateur il devra avoir un mot de passe défini


```bash
sudo useradd -m -s /bin/bash -g stronk_admins -G sudo 
```

