#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 顾少
#        Email: vekergu@163.com
#     HomePage: https://github.com/vekergu
#      Version: 0.0.1
#   LastChange: 
#      History:
#=============================================================================
#code: https://github.com/kennethreitz/pip-pop/blob/master/bin/pip-diff
"""Usage:
  pip-diff (--fresh | --stale) <reqfile1> <reqfile2> [--exclude <package>...]
  pip-diff (-h | --help)
Options:
  -h --help     Show this screen.
  --fresh       List newly added packages.
  --stale       List removed packages.
"""
import os
from docopt import docopt
from pip.req import parse_requirements
from pip.index import PackageFinder
from pip._vendor.requests import session

requests = session()


class Requirements(object):
    def __init__(self, reqfile=None):
        super(Requirements, self).__init__()
        #super引用为了当父继承更换后，可以不用再代码中再进行替换
        self.path = reqfile
        self.requirements = []

        if reqfile:
            self.load(reqfile)

    def __repr__(self):
        return '<Requirements \'{}\'>'.format(self.path)

    def load(self, reqfile):
        #如果这个reqfile是存在的
        if not os.path.exists(reqfile):
            #raise是引出异常的，raise后面的语句将不再执行
            raise ValueError('The given requirements file does not exist.')

        finder = PackageFinder([], [], session=requests)
        for requirement in parse_requirements(reqfile, finder=finder, session=requests):
            if requirement.req:
                if not getattr(requirement.req, 'name', None):
                    # Prior to pip 8.1.2 the attribute `name` did not exist.
                    requirement.req.name = requirement.req.project_name
                self.requirements.append(requirement.req)


    def diff(self, requirements, ignore_versions=False, excludes=None):
        r1 = self
        r2 = requirements
        results = {'fresh': [], 'stale': []}

        # Generate fresh packages.
        other_reqs = (
            [r.name for r in r1.requirements]
            if ignore_versions else r1.requirements
        )

        for req in r2.requirements:
            r = req.name if ignore_versions else req

            if r not in other_reqs and r not in excludes:
                results['fresh'].append(req)

        # Generate stale packages.
        other_reqs = (
            [r.name for r in r2.requirements]
            if ignore_versions else r2.requirements
        )

        for req in r1.requirements:
            r = req.name if ignore_versions else req

            if r not in other_reqs and r not in excludes:
                results['stale'].append(req)

        return results


def diff(r1, r2, include_fresh=False, include_stale=False, excludes=None):
    include_versions = True if include_stale else False
    excludes = excludes if len(excludes) else []

    try:
        r1 = Requirements(r1)
        r2 = Requirements(r2)
    except ValueError:
        print('There was a problem loading the given requirements files.')
        exit(os.EX_NOINPUT)

    results = r1.diff(r2, ignore_versions=True, excludes=excludes)

    if include_fresh:
        for line in results['fresh']:
            print(line.name if include_versions else line)

    if include_stale:
        for line in results['stale']:
            print(line.name if include_versions else line)


def main():
    args = docopt(__doc__, version='pip-diff')
    #docopt根据你写的文档描述，可以自动为你生成解析器，可以非常容易的为你的python程序创建命令行界面
    #把开始注释的部分打印了出来
    kwargs = {
        'r1': args['<reqfile1>'],
        'r2': args['<reqfile2>'],
        'include_fresh': args['--fresh'],
        'include_stale': args['--stale'],
        'excludes': args['<package>']
    }

    diff(**kwargs)


if __name__ == '__main__':
    main()