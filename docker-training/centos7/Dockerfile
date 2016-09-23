#
# MAINTAINER        Carson,C.J.Zeong <zcy@nicescale.com>
# DOCKER-VERSION    1.6.2
#
# Dockerizing CentOS7: Dockerfile for building CentOS images
#
#父镜像
FROM       centos:centos7.1.1503
#维护者
MAINTAINER Carson,C.J.Zeong <zcy@nicescale.com>
#时区的环境变量
ENV TZ "Asia/Shanghai"
ENV TERM xterm

#用于copy文件，复制文件到容器里
#ADD多两个功能 软连接  解压功能
ADD aliyun-mirror.repo /etc/yum.repos.d/CentOS-Base.repo
ADD aliyun-epel.repo /etc/yum.repos.d/epel.repo

#执行shell方法
RUN yum install -y curl wget tar bzip2 unzip vim-enhanced passwd sudo yum-utils hostname net-tools rsync man && \
    yum install -y gcc gcc-c++ git make automake cmake patch logrotate python-devel libpng-devel libjpeg-devel && \
    yum install -y --enablerepo=epel pwgen python-pip && \
    yum clean all

RUN pip install supervisor
ADD supervisord.conf /etc/supervisord.conf

RUN mkdir -p /etc/supervisor.conf.d && \
    mkdir -p /var/log/supervisor

#暴漏出22端口
EXPOSE 22

#启动那个进程，最后一条ENTRYPOINT生效
ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]
