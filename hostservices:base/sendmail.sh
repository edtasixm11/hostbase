#!/bin/bash
# Starting sendmail daemon
# @edt ASIX-M06
# -----------------------------------------------------------------------------
#/usr/lib/systemd/system/sm-client.service
#/usr/lib/systemd/system/sendmail.service
# -----------------------------------------------------------------------------
/bin/touch /run/sm-client.pid
/bin/chown smmsp:smmsp /run/sm-client.pid
/sbin/restorecon /run/sm-client.pid
/etc/mail/make
/etc/mail/make aliases
/usr/sbin/sendmail -L sm-msp-queue -Ac -q1h $SENDMAIL_OPTARG
/usr/sbin/sendmail  -q1h  $SENDMAIL_OPTARG

# si es vol que no es quedi en foreground fer:
#/usr/sbin/sendmail -bd -q1h  $SENDMAIL_OPTARG

