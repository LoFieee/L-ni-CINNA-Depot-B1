## 1. Analyse du service

##### 🌞 S'assurer que le service sshd est démarré

```bash
systemctl status sshd
```

##### 🌞 Analyser les processus liés au service SSH

```bash
ps -ef | grep sshd
```

##### 🌞 Déterminer le port sur lequel écoute le service SSH

```bash
ss  -tulnp | grep sshd
```

##### 🌞 Consulter les logs du service SSH

```bash
journalctl -u sshd (trié par unité)
```

## 2 Modification du service

##### 🌞 Identifier le fichier de configuration du serveur SSH

##### 🌞 Modifier le fichier de conf


