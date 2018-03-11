#!/bin/bash
# @edt ASIX-M06 Curs 2017-2018
# Startup imatge hostbase:base
# ---------------------------------------------------------
/usr/sbin/xinetd    && echo "OK xinetd"
/usr/sbin/httpd     && echo "OK httpd"
/usr/sbin/vsftpd    && echo "OK vsftpd"
/usr/sbin/sshd      && echo "OK sshd"
/usr/sbin/in.tftpd -l -s /var/lib/tftpboot && echo "OK tftp"

# programa en foreground:
/usr/sbin/in.telnetd -debug 23 && echo "OK telnet"
./sendmail.sh

# Script sendmail es queda executant en primer pla
# fer docker exec -it <container> /bin/bash per accedir al container
# /bin/bash

