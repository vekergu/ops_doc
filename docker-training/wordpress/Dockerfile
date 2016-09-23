from csphere/php-fpm:5.4

add init.sh /init.sh

#先执行了init.sh脚本，然后启动/usr/bin/supervisord，能自动判断参数？
#是通过init.sh中结尾
#我执行了这个脚本，我会执行后面的这条指令
#exec "$@"
#来指引出执行后面的脚本
entrypoint ["/init.sh", "/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]
