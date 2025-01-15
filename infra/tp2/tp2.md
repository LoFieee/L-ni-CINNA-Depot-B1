# 2 Let's go    
    
🌞 Afficher la quantité d'espace disque disponible


```bash
df -h / | tail -n 1 | awk '{print $4}'
```