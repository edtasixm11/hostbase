# Imatge hostbase:base
# @edt ASIX-M06 Curs 2017-2018
# Version 1.0
#
# Host amb serveis de xarxa engegats
#
# ---------------------------------------------------------
FROM fedora:24
MAINTAINER @edt "@edt ASIX-M06 Curs 2017-2018"
RUN dnf -y update vi
RUN dnf -y install vim iputils iproute procps mlocate man-db nmap tree \
                   uw-imap sendmail tftp tftp-server vsftpd httpd telnet telnet-server openssh openssh-server openssh-clients \
                   policycoreutils
#RUN mkdir /opt/docker
COPY ./ /opt/docker
RUN chmod +x /opt/docker/startup.sh /opt/docker/sendmail.sh
COPY data-files/index.html /var/www/html
COPY data-files/index.html data-files/README.txt /var/ftp/pub/
COPY data-files/index.html data-files/README.txt /var/lib/tftpboot/
COPY xinetd-files/* /etc/xinetd.d/
RUN /usr/bin/ssh-keygen -A
CMD ["/opt/docker/startup.sh"]



