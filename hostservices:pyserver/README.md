# Imatge hostbasse:base
## @edt ASIX-M06 Cuts 2017-2018
Creació de la imatge **hostbase:base**

Conté una imatge base fedora:24 amb tot de serveis de xarxa activats per fer-hi proves de connectivitat. Conté activats tant serveis sand alone com xinetd.

### serveis (port,transport)

 * xinetd:
   * echo     (7, tcp, udp)
   * discard  (9,tcp, udp)
   * daytime  (13, tcp, udp)
   * chargen  (19, tcp, udp)
   * time     (37, tcp, udp)
   * ipop3    (110, tcp)
   * pop3s    (995, tcp)
   * imap     (143, tcp)
   * imaps    (993, tcp)

   * daytime-bis (2013, tcp, redirect localhost:13)
   * echo-bis    (2007, tcp, redirect localhost:7)
   * http-switch (2080, tcp, redirect localhost:80)

 * httpd  (80,tcp)
 * vsftpd (20,21, tcp)
 * tftp   (69, udp)
 * smtp   (25, tcp)
 * ssh    (22, tcp)
 * telnet (23, tcp)
 * pyserver (50001, tcp)


## Utilització

docker build -t imatge .

docker run --name container -h container -d imatge

docker exec -it container /bin/bash

docker run --rm --name h2 -h h2 -p 7:7 -p 9:9 -p 13:13 -p 19:19 -p 20-21:20-21 -p 22:22 -p23:23 -p 25:25 -p 37:37 -p 69:69 -p 80:80 -p 110:110 -p 143:143 -p 993:993 -p 995:995  -p 2007:2007 -p 2013:2013 -p 2080:2080  -p 50001:50001 -d prova

