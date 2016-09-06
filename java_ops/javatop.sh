#!/usr/bin/env bash
# write by    : vekergu@163.com
# date        : 2014-01-16
# version     : 0.01

top=${1:-10}
pid=${2:-$(pgrep -u $USER java)}
tmp_file=/tmp/java_${pid}_$$.trace

# fix for alibaba-inc.com
#export JAVA_HOME=/opt/taobao/java

$JAVA_HOME/bin/jstack $pid > $tmp_file
#java1.7  直接会显示pid不用再转换为16进制

#-H 显示树状结构
#-e 显示环境变量
#-o format        specify user-defined format. Identical to -o and --format.  用户定义格式
#--sort=%cpu  以cpu使用率排序
#--no-headers
ps H -eo user,pid,ppid,tid,time,%cpu --sort=%cpu --no-headers\
	| tail -$top\
	| awk -v "pid=$pid" '$2==pid{print $4"\t"$6}'\
	| while read line;
do
	nid=$(echo "$line"|awk '{printf("0x%x",$1)}')
    cpu=$(echo "$line"|awk '{print $2}')
    awk -v "cpu=$cpu" '/nid='"$nid"'/,/^$/{print $0"\t"(isF++?"":"cpu="cpu"%");}' $tmp_file
done

rm -f $tmp_file