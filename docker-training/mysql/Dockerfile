#
# MAINTAINER        Carson,C.J.Zeong <zcy@nicescale.com>
# DOCKER-VERSION    1.6.2
#
# Dockerizing Mariadb: Dockerfile for building Mariadb images
#
FROM csphere/centos:7.1
MAINTAINER Carson,C.J.Zeong <zcy@nicescale.com>

ENV DATA_DIR /var/lib/mysql

# Install Mariadb
RUN yum install -y mariadb mariadb-server && \
    yum clean all

ADD mysqld_charset.cnf /etc/my.cnf.d/

#复制脚本目录
COPY scripts /scripts
#运行脚本
RUN chmod +x /scripts/start

EXPOSE 3306

#数据卷？映射
VOLUME ["/var/lib/mysql"]

ENTRYPOINT ["/scripts/start"]
