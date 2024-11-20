# TP5 : Le compilateur ton pire meilleur ami

## 0. Prérequis

Créer un répertoire de travail dans votre répertoire personnel

sur la machine Linux que vous utiliserez pour le TP
prouve avec une commande que tu es bien dans ton répertoire personnel
créer un dossier work ou un autre nom si tu veux
tous les fichiers utilisés dans ce TP devront être créés dans ce dossier


```powershell
lofie@efreios:~$ mkdir repperso
lofie@efreios:~$ ls
lofie@efreios:~$ cd repperso/
lofie@efreios:~/repperso$
```

## Partie I : Compilation étou tavu

# I. Programme minimal

## 1. Compilation

## 2. Analyse du programme compilé

Retrouvez à l'aide de readelf l'architecture pour laquelle le programme est compilé

vous devriez voir que c'est un ELF destiné à être exécuté par un CPU 32-bit

```powershell
lofie@efreios:~/repperso$ readelf -h hello1
```

Afficher la liste des sections contenues dans le programme

on devrait notamment y voir une section .text qui est celle qui contient le code assembleur du programme

```powershell
lofie@efreios:~/repperso$ readelf -S hello1
```

Affichez le code assembleur de la section .text à l'aide d'objdump

```powershell
lofie@efreios:~/repperso$ objdump -M inter -j .text -d hello1
```

## 2. Librairie et compilation dynamique

```powershell
lofie@efreios:~/repperso$ ldd hello2
lofie@efreios:~/repperso$ ldd hello1
lofie@efreios:~$ ldd /bin/ls
lofie@efreios:~$ file /bin/ls
lofie@efreios:~$ ldd /usr/bin/firefox
```

```powershell
lofie@efreios:~/repperso$ ldd hello2
        linux-gate.so.1 (0xf7f2c000)
        libc.so.6 => /lib32/libc.so.6 (0xf7ce5000)
        /lib/ld-linux.so.2 (0xf7f2e000)
lofie@efreios:~/repperso$ file /lib32/libc.so.6
/lib32/libc.so.6: ELF 32-bit LSB shared object, Intel 80386, version 1 (GNU/Linux), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=b3f5646d25dc90cc34d2507f197561065c7e630c, for GNU/Linux 3.2.0, stripped
```

## 3. Compilation statique

```powershell
lofie@efreios:~/repperso$ file hello3
hello3: ELF 32-bit LSB executable, Intel 80386, version 1 (GNU/Linux), statically linked, BuildID[sha1]=c4650c64e3969516aee2fb281f0f2e07584966b6, for GNU/Linux 3.2.0, with debug_info, not stripped
lofie@efreios:~/repperso$ file hello2
hello2: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=51aeede16c0387d6cde545e09c5c3e3ea4d7783d, for GNU/Linux 3.2.0, with debug_info, not stripped
```

Affichez leurs tailles

```powershell
lofie@efreios:~/repperso$ du -h hello2
16K     hello2
lofie@efreios:~/repperso$ du -h hello3
728K    hello3
```

##### 4. Compilation cross-platform


```powershell
lofie@efreios:~$ cat /proc/cpuinfo
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 186
model name      : 13th Gen Intel(R) Core(TM) i9-13900H
stepping        : 2
microcode       : 0xffffffff
cpu MHz         : 2995.200
cache size      : 24576 KB
physical id     : 0
siblings        : 1
core id         : 0
cpu cores       : 1
apicid          : 0
initial apicid  : 0
fpu             : yes
fpu_exception   : yes
cpuid level     : 26
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 cx16 sse4_1 sse4_2 movbe popcnt aes rdrand hypervisor lahf_lm abm 3dnowprefetch ibrs_enhanced fsgsbase bmi1 bmi2 invpcid rdseed adx clflushopt sha_ni arat md_clear flush_l1d arch_capabilities
bugs            : spectre_v1 spectre_v2 spec_store_bypass swapgs retbleed eibrs_pbrsb rfds bhi
bogomips        : 5990.40
clflush size    : 64
cache_alignment : 64
address sizes   : 39 bits physical, 48 bits virtual
power management:
```

Vérifiez que vous avez la commande x86-64-linux-gnu-gcc

prouvez-le avec la commande de votre choix

```powershell
lofie@efreios:~$ which x86_64-linux-gnu-gcc
/usr/bin/x86_64-linux-gnu-gcc
```

Compilez votre fichier hello3.c dans un fichier cible nommé hello4 vers une autre architecture que la vôtre

vous devez donc trouver une autre commande gcc que x86-64-linux-gnu-gcc qui est en réalité celle que vous utilisez depuis le début
par exemple, trouvez un commande gcc qui permet de compiler vers une architecture ARM

```powershell
lofie@efreios:~/repperso$ arm-linux-gnueabi-gcc hello3.c -o hello4
lofie@efreios:~/repperso$ ls
hello1  hello1.c  hello2  hello2.c  hello3  hello3.c  hello4
```

Désassemblez hello3 et hello4 à l'aide d'objdump

vous devriez constater que malgré le même programme C d'entrée, le contenu des deux programmes une fois compilés est bien différent

```powershell
lofie@efreios:~/repperso$ objdump -d hello4

hello4:     file format elf32-littlearm


Disassembly of section .init:

000003a4 <_init>:
 3a4:   e92d4008        push    {r3, lr}
 3a8:   eb000025        bl      444 <call_weak_fn>
 3ac:   e8bd8008        pop     {r3, pc}

Disassembly of section .plt:

000003b0 <.plt>:
 3b0:   e52de004        push    {lr}            @ (str lr, [sp, #-4]!)
 3b4:   e59fe004        ldr     lr, [pc, #4]    @ 3c0 <.plt+0x10>
 3b8:   e08fe00e        add     lr, pc, lr
 3bc:   e5bef008        ldr     pc, [lr, #8]!
 3c0:   00001c40        .word   0x00001c40

000003c4 <__libc_start_main@plt>:
 3c4:   e28fc600        add     ip, pc, #0, 12
 3c8:   e28cca01        add     ip, ip, #4096   @ 0x1000
 3cc:   e5bcfc40        ldr     pc, [ip, #3136]!        @ 0xc40

000003d0 <__cxa_finalize@plt>:
 3d0:   e28fc600        add     ip, pc, #0, 12
 3d4:   e28cca01        add     ip, ip, #4096   @ 0x1000
 3d8:   e5bcfc38        ldr     pc, [ip, #3128]!        @ 0xc38

000003dc <puts@plt>:
 3dc:   e28fc600        add     ip, pc, #0, 12
 3e0:   e28cca01        add     ip, ip, #4096   @ 0x1000
 3e4:   e5bcfc30        ldr     pc, [ip, #3120]!        @ 0xc30

000003e8 <__gmon_start__@plt>:
 3e8:   e28fc600        add     ip, pc, #0, 12
 3ec:   e28cca01        add     ip, ip, #4096   @ 0x1000
 3f0:   e5bcfc28        ldr     pc, [ip, #3112]!        @ 0xc28

000003f4 <abort@plt>:
 3f4:   e28fc600        add     ip, pc, #0, 12
 3f8:   e28cca01        add     ip, ip, #4096   @ 0x1000
 3fc:   e5bcfc20        ldr     pc, [ip, #3104]!        @ 0xc20

Disassembly of section .text:

00000400 <_start>:
 400:   e3a0b000        mov     fp, #0
 404:   e3a0e000        mov     lr, #0
 408:   e49d1004        pop     {r1}            @ (ldr r1, [sp], #4)
 40c:   e1a0200d        mov     r2, sp
 410:   e52d2004        push    {r2}            @ (str r2, [sp, #-4]!)
 414:   e52d0004        push    {r0}            @ (str r0, [sp, #-4]!)
 418:   e59fa01c        ldr     sl, [pc, #28]   @ 43c <_start+0x3c>
 41c:   e28f3018        add     r3, pc, #24
 420:   e08aa003        add     sl, sl, r3
 424:   e3a03000        mov     r3, #0
 428:   e52d3004        push    {r3}            @ (str r3, [sp, #-4]!)
 42c:   e59f000c        ldr     r0, [pc, #12]   @ 440 <_start+0x40>
 430:   e79a0000        ldr     r0, [sl, r0]
 434:   ebffffe2        bl      3c4 <__libc_start_main@plt>
 438:   ebffffed        bl      3f4 <abort@plt>
 43c:   00001bc4        .word   0x00001bc4
 440:   0000002c        .word   0x0000002c

00000444 <call_weak_fn>:
 444:   e59f3014        ldr     r3, [pc, #20]   @ 460 <call_weak_fn+0x1c>
 448:   e59f2014        ldr     r2, [pc, #20]   @ 464 <call_weak_fn+0x20>
 44c:   e08f3003        add     r3, pc, r3
 450:   e7932002        ldr     r2, [r3, r2]
 454:   e3520000        cmp     r2, #0
 458:   012fff1e        bxeq    lr
 45c:   eaffffe1        b       3e8 <__gmon_start__@plt>
 460:   00001bac        .word   0x00001bac
 464:   00000028        .word   0x00000028

00000468 <deregister_tm_clones>:
 468:   e59f002c        ldr     r0, [pc, #44]   @ 49c <deregister_tm_clones+0x34>
 46c:   e59f302c        ldr     r3, [pc, #44]   @ 4a0 <deregister_tm_clones+0x38>
 470:   e08f0000        add     r0, pc, r0
 474:   e08f3003        add     r3, pc, r3
 478:   e1530000        cmp     r3, r0
 47c:   e59f3020        ldr     r3, [pc, #32]   @ 4a4 <deregister_tm_clones+0x3c>
 480:   e08f3003        add     r3, pc, r3
 484:   012fff1e        bxeq    lr
 488:   e59f2018        ldr     r2, [pc, #24]   @ 4a8 <deregister_tm_clones+0x40>
 48c:   e7933002        ldr     r3, [r3, r2]
 490:   e3530000        cmp     r3, #0
 494:   012fff1e        bxeq    lr
 498:   e12fff13        bx      r3
 49c:   00001bc4        .word   0x00001bc4
 4a0:   00001bc0        .word   0x00001bc0
 4a4:   00001b78        .word   0x00001b78
 4a8:   00000024        .word   0x00000024

000004ac <register_tm_clones>:
 4ac:   e59f0038        ldr     r0, [pc, #56]   @ 4ec <register_tm_clones+0x40>
 4b0:   e59f3038        ldr     r3, [pc, #56]   @ 4f0 <register_tm_clones+0x44>
 4b4:   e08f0000        add     r0, pc, r0
 4b8:   e08f3003        add     r3, pc, r3
 4bc:   e0433000        sub     r3, r3, r0
 4c0:   e1a01fa3        lsr     r1, r3, #31
 4c4:   e0811143        add     r1, r1, r3, asr #2
 4c8:   e59f3024        ldr     r3, [pc, #36]   @ 4f4 <register_tm_clones+0x48>
 4cc:   e1b010c1        asrs    r1, r1, #1
 4d0:   e08f3003        add     r3, pc, r3
 4d4:   012fff1e        bxeq    lr
 4d8:   e59f2018        ldr     r2, [pc, #24]   @ 4f8 <register_tm_clones+0x4c>
 4dc:   e7933002        ldr     r3, [r3, r2]
 4e0:   e3530000        cmp     r3, #0
 4e4:   012fff1e        bxeq    lr
 4e8:   e12fff13        bx      r3
 4ec:   00001b80        .word   0x00001b80
 4f0:   00001b7c        .word   0x00001b7c
 4f4:   00001b28        .word   0x00001b28
 4f8:   00000030        .word   0x00000030

000004fc <__do_global_dtors_aux>:
 4fc:   e59f304c        ldr     r3, [pc, #76]   @ 550 <__do_global_dtors_aux+0x54>
 500:   e59f204c        ldr     r2, [pc, #76]   @ 554 <__do_global_dtors_aux+0x58>
 504:   e08f3003        add     r3, pc, r3
 508:   e5d33000        ldrb    r3, [r3]
 50c:   e08f2002        add     r2, pc, r2
 510:   e3530000        cmp     r3, #0
 514:   112fff1e        bxne    lr
 518:   e59f3038        ldr     r3, [pc, #56]   @ 558 <__do_global_dtors_aux+0x5c>
 51c:   e92d4010        push    {r4, lr}
 520:   e7923003        ldr     r3, [r2, r3]
 524:   e3530000        cmp     r3, #0
 528:   0a000002        beq     538 <__do_global_dtors_aux+0x3c>
 52c:   e59f3028        ldr     r3, [pc, #40]   @ 55c <__do_global_dtors_aux+0x60>
 530:   e79f0003        ldr     r0, [pc, r3]
 534:   ebffffa5        bl      3d0 <__cxa_finalize@plt>
 538:   ebffffca        bl      468 <deregister_tm_clones>
 53c:   e59f301c        ldr     r3, [pc, #28]   @ 560 <__do_global_dtors_aux+0x64>
 540:   e3a02001        mov     r2, #1
 544:   e08f3003        add     r3, pc, r3
 548:   e5c32000        strb    r2, [r3]
 54c:   e8bd8010        pop     {r4, pc}
 550:   00001b30        .word   0x00001b30
 554:   00001aec        .word   0x00001aec
 558:   00000020        .word   0x00000020
 55c:   00001b00        .word   0x00001b00
 560:   00001af0        .word   0x00001af0

00000564 <frame_dummy>:
 564:   eaffffd0        b       4ac <register_tm_clones>

00000568 <main>:
 568:   e92d4800        push    {fp, lr}
 56c:   e28db004        add     fp, sp, #4
 570:   e59f3014        ldr     r3, [pc, #20]   @ 58c <main+0x24>
 574:   e08f3003        add     r3, pc, r3
 578:   e1a00003        mov     r0, r3
 57c:   ebffff96        bl      3dc <puts@plt>
 580:   e3a03000        mov     r3, #0
 584:   e1a00003        mov     r0, r3
 588:   e8bd8800        pop     {fp, pc}
 58c:   000000b0        .word   0x000000b0

Disassembly of section .fini:

00000590 <_fini>:
 590:   e92d4008        push    {r3, lr}
 594:   e8bd8008        pop     {r3, pc}
lofie@efreios:~/repperso$ objdump -d hello3

la meme chose mais avec bcp trop de ligne
```

Essayez d'exécuter le programme hello4

sproutch !
should NOT work

```powershell
lofie@efreios:~/repperso$ ./hello4
-bash: ./hello4: cannot execute binary file: Exec format error
```

# II. Ptits challenges de cracking

## 1. Install Ghidra

 Avec une commande apt search, déterminez si le paquet ghidra est disponible

normalement, il ne l'est pas :d

```powershell
lofie@efreios:~$ apt search ghidra
```

 Ajouter l'URL des dépôts Kali à vos dépôts existants

le fichier qui contient les URLs des dépôts sous Debian c'est /etc/apt/sources.list

il faut ajouter une ligne pour ajouter une nouvelle URL d'un nouveau dépôt
la ligne suivante pour ajouter les dépôts de Kali :

```powershell
lofie@efreios:~$ sudo nano /etc/apt/sources.list
```

Ajoutez la clé publique des gars de chez Kali


```powershell
lofie@efreios:~$ sudo wget https://archive.kali.org/archive-key.asc -O /etc/apt/trusted.
gpg.d/kali-archive-keyring.asc
```

 Mettez à jour la liste des dépôts que votre OS connaît actuellement

le but, c'est qu'il voit le nouveau dépôt Kali qu'on a ajouté
c'est la commande

```powershell
lofie@efreios:~$ sudo apt update -y
```

Avec une commande apt search, déterminez si le paquet ghidra est disponible

normalement, il l'est maintenant !

```powershell
lofie@efreios:~$ apt search ghidra
```

Installez le paquet ghidra

avec une commande apt install

```powershell
lofie@efreios:~$ sudo apt install ghidra
```

## 2. Patch manuel programme simple

Récupérez le code de password_2.c sur la machine Linux et compilez-le

vous pouvez répéter la manipulation qu'on a montré en démo pour contourner la demande de mot de passe
on en le connaîtra donc jamais ce mot de passe ! :d

```powershell
lofie@efreios:~/repperso$ gcc -fno-stack-protector -g -m32 -o password_2 password_2.c -lcrypto -lc
lofie@efreios:~/repperso$ ls
```

## 3. Root-me

ELF x86 - 0 protection
facebooklinkedintwitter
5 Points  0x0
Premier challenge de cracking, programme rédigé en C avec vi et compilé avec GCC32.

mdp : 123456789

ELF x86 - Basique
facebooklinkedintwitter
5 Points  0x0
Encore un exe à cracker, toujours compilé avec gcc32 sur x86

mdp : 987654321

## 4. Ptit chall maison

Récupérer le flag du programme kaddate_challenge

téléchargez le programme depuis votre machine Linux (avec une commande wget)
lancez-le pour voir ce qu'il fait, comment il se comporte
obtenez des infos sur lui, disséquez-le and...
... get the flag !

```powershell
b1-os{PetitB1deviendraGrandPetitB1}
```
