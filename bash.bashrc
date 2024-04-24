GNU nano 7.2                          bash.bashrc
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
##PS1='\[\e[32m\]\u@\h:\[\e[31m\]\w\$\[\e[32m\] '
PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '

alias txl='python /data/data/com.termux/files/home/Termux-Lock/Termux-Lock.py -l'
txl
