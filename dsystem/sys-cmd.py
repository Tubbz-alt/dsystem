#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os

from systemcommand.test_useradd import Useradd
from systemcommand.test_userdel import Userdel
from systemcommand.test_passwd import Passwd

from systemcommand.test_pwd import Pwd
from systemcommand.test_cd import Cd
from systemcommand.test_mkdir import Mkdir
from systemcommand.test_rmdir import Rmdir
from systemcommand.test_cp import Cp
from systemcommand.test_mv import Mv
from systemcommand.test_rm import Rm
from systemcommand.test_file import File
from systemcommand.test_find import Find
from systemcommand.test_grep import Grep
from systemcommand.test_chown import Chown
from systemcommand.test_sort import Sort
from systemcommand.test_wc import Wc

from systemcommand.test_ifconfig import Ifconfig
from systemcommand.test_ping import Ping
from systemcommand.test_ping_ip import Ping_ip
from systemcommand.test_ping_local_ip import Ping_local_ip
from systemcommand.test_netstat_i import Netstat_i
from systemcommand.test_netstat_r import Netstat_r
from systemcommand.test_telnet import Telnet
from systemcommand.test_traceroute import Traceroute

from systemcommand.test_tar import Tar
from systemcommand.test_gzip import Gzip
from systemcommand.test_gunzip import Gunzip

from systemcommand.test_kill import Kill
from systemcommand.test_ps import Ps

from systemcommand.test_vi import Vi

from systemcommand.test_apt_get import Apt_get
from systemcommand.test_apt_cache import Apt_cache

from systemcommand.test_man import Man
from systemcommand.test_who import Who
from systemcommand.test_whoami import Whoami
from systemcommand.test_cal import Cal
from systemcommand.test_date import Date
from systemcommand.test_more import More
from systemcommand.test_redirect import Redirect
from systemcommand.test_pipe import Pipe

from osd.test_keyboardlayout import KbLayout

def main():
    classes = []

    # 桌面环境
    classes.append(KbLayout)

    # 常用命令测试

    # 用户管理命令
    classes.append(Useradd)
    classes.append(Userdel)
    classes.append(Passwd)

    # 文件/文件夹操作命令
    classes.append(Pwd)
    classes.append(Cd)
    classes.append(Mkdir)
    classes.append(Rmdir)
    classes.append(Cp)
    classes.append(Mv)
    classes.append(Rm)
    classes.append(File)
    classes.append(Find)
    classes.append(Grep)
    classes.append(Chown)
    classes.append(Sort)
    classes.append(Wc)

    # 网络管理命令
    classes.append(Ifconfig)
    classes.append(Ping)
    classes.append(Ping_ip)
    classes.append(Ping_local_ip)
    classes.append(Netstat_i)
    classes.append(Netstat_r)
    classes.append(Telnet)
    classes.append(Traceroute)

    # 备份、压缩和解压缩操作命令
    classes.append(Tar)
    classes.append(Gzip)
    classes.append(Gunzip)

    # 进程管理
    classes.append(Kill)
    classes.append(Ps)

    # 文本编辑命令
    classes.append(Vi)

    # 其他命令
    classes.append(Man)
    classes.append(Who)
    classes.append(Whoami)
    classes.append(Cal)
    classes.append(Date)
    classes.append(More)
    classes.append(Redirect)
    classes.append(Pipe)

    # 软件包管理命令
    classes.append(Apt_get)
    classes.append(Apt_cache)

    for c in classes:
        suite = c.suite()
        unittest.TextTestRunner(resultclass=c.MyTestResult).run(suite)

if __name__ == "__main__":
    main()
