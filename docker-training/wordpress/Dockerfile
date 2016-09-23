from csphere/php-fpm:5.4

add init.sh /init.sh

#先执行了init.sh脚本，然后启动/usr/bin/supervisord，能自动判断参数？
entrypoint ["/init.sh", "/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]
