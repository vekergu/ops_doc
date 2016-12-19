#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 白开水
#        Email: vekergu@163.com
#     HomePage: https://github.com/vekergu
#      Version: 0.0.1
#   LastChange: 
#      History:
#=============================================================================
from __future__ import print_function
import sys
import re
import time
import textwrap

from salt_connect import saltJob
def color_print(msg, color='red', exits=False):
    """
    Print colorful string.
    颜色打印字符或者退出
    """
    color_msg = {'blue': '\033[1;36m%s\033[0m',
                 'green': '\033[1;32m%s\033[0m',
                 'yellow': '\033[1;33m%s\033[0m',
                 'red': '\033[1;31m%s\033[0m',
                 'title': '\033[30;42m%s\033[0m',
                 'info': '\033[32m%s\033[0m'}
    msg = color_msg.get(color, 'red') % msg
    print(msg)
    if exits:
        time.sleep(2)
        sys.exit()
    return msg


class Nav():
    """
    导航提示类
    """
    def search(self, str_r=''):
        # 搜索结果保存
        if str_r:
            try:
                id_ = int(str_r)
                if id_ < len(self.search_result):
                    self.search_result = [self.search_result[id_]]
                    return
                else:
                    raise ValueError

            except (ValueError, TypeError):
                # 匹配 ip, hostname, 备注
                str_r = str_r.lower()
                self.search_result = [asset for asset in self.perm_assets if str_r == str(asset.ip).lower()] or \
                                     [asset for asset in self.perm_assets if str_r in str(asset.ip).lower() \
                                      or str_r in str(asset.hostname).lower() \
                                      or str_r in str(asset.comment).lower()]
        else:
            # 如果没有输入就展现所有
            self.search_result = self.perm_assets

    def search_result(self):
        key_list = saltJob()
        return key_list.list_all_key()[0]

    @staticmethod
    def get_max_asset_property_length(key_list):
        try:
            return max([len(key_list)])
        except ValueError:
            return 30

    def print_search_result(self):
        key_max_length = self.get_max_asset_property_length(self.search_result())
        line = '[ %-3s] %-' + str(key_max_length) + 's'
        color_print(line % ('ID', 'Hostname'))
        for index, asset in enumerate(self.search_ressult()):
            print(line % (index,asset))
        print()

    @staticmethod
    def print_nav():
        """
        Print prompt
        打印提示导航
        """
        msg = """\n\033[1;32m###    欢迎使用saltstack文本操作系统   ### \033[0m

        1) 输入 \033[32mID\033[0m 直接登录 或 输入\033[32m部分 IP,主机名,备注\033[0m 进行搜索登录(如果唯一).
        2) 输入 \033[32m/\033[0m + \033[32mIP, 主机名 or 备注 \033[0m搜索. 如: /ip
        3) 输入 \033[32mP/p\033[0m 显示您有权限的主机.
        4) 输入 \033[32mG/g\033[0m 显示您有权限的主机组.
        5) 输入 \033[32mG/g\033[0m\033[0m + \033[32m组ID\033[0m 显示该组下主机. 如: g1
        6) 输入 \033[32mE/e\033[0m 批量执行命令.
        7) 输入 \033[32mU/u\033[0m 批量上传文件.
        8) 输入 \033[32mD/d\033[0m 批量下载文件.
        9) 输入 \033[32mH/h\033[0m 帮助.
        0) 输入 \033[32mQ/q\033[0m 退出.
        """
        print(textwrap.dedent(msg))


def main():
    """
    主程序
    """
    gid_pattern = re.compile(r'^g\d+$')
    nav = Nav()
    nav.print_nav()

    try:
        while True:
            try:
                option = raw_input("\033[1;32mOpt or ID>:\033[0m ").strip()
            except EOFError:
                nav.print_nav()
                continue
            except KeyboardInterrupt:
                sys.exit(0)
            if option in ['P', 'p', '\n', '']:
                nav.search()
                nav.print_search_result()
                continue
            if option.startswith('/'):
                nav.search(option.lstrip('/'))
                nav.print_search_result()
            elif gid_pattern.match(option):
                nav.get_asset_group_member(str_r=option)
                nav.print_search_result()
            elif option in ['G', 'g']:
                nav.print_asset_group()
                continue
            elif option in ['E', 'e']:
                nav.exec_cmd()
                continue
            elif option in ['U', 'u']:
                nav.upload()
            elif option in ['D', 'd']:
                nav.download()
            elif option in ['H', 'h']:
                nav.print_nav()
            elif option in ['Q', 'q', 'exit']:
                sys.exit()
            else:
                nav.search(option)
                if len(nav.search_result) == 1:
                    print('Only match Host:  %s ' % nav.search_result[0].hostname)
                    nav.try_connect()
                else:
                    nav.print_search_result()

    except IndexError, e:
        color_print(e)
        time.sleep(5)

if __name__ == '__main__':
    main()