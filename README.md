# Termux-lock
Personnalisez votre termux 

ce script à besoin d'être améliorer

Attention !

# Commencez par modifier notre bash.bashrc 

   Ajouter cette ligne a la fin de fichier :
/data/data/com.termux/files/usr/etc/[bash.bashrc](https://github.com/Dkwebpoint/Termux-lock/blob/2ed3fc87c5c4a234b060a26847bf1797d354d04f/bash.bashrc)

`alias txl='python /data/data/com.termux/files/home/Termux-Lock/Termux-Lock.py -l'
txl`
   
   

    avant d'exécuter ce script vous devriez créer une combinaison USER/PASS 
    et enregistrer les dans un fichier de votre choix 
    
    cd /data/data/com.termux/files/usr/share/
    
    mkdir termux-user
    
    cd termux-user
    
    nano usr_pwd.txt

    et écrire vos identifiants comme ceci :
    root (la première ligne == utilisateur)
    toor (la deuxième ligne == password)
# Requirements 

pip install stdiomask
apt install figlet
pip install lolcat


# images
![termux lock in action](https://github.com/Dkwebpoint/Termux-lock/blob/0c740c6b0c3a90f1a5e88492d64661afdb56a372/Screenshot_20230702-182130.png)

![termux lock in action](https://github.com/Dkwebpoint/Termux-lock/blob/9f514f0aaff4398e8be08dbd5ca37c90e423ef3c/Screenshot_20230702-182204.png)
