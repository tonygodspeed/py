#!/usr/bin/env python
#coding=utf8

from MR_BASE import *

reload(sys)
sys.setdefaultencoding("utf-8")

class MR_DRTASKMGR(mr_base):
    def __init__(self):
        mt_type =  [
                      {'key':'SRC',    'type':'s', 'mt':r'^.*<SRC:' + common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'err_type', 'type':'i', 'mt':r'err_type:'+common_def.MT_VALUE_VALID_POSTFIX},
                      {'key':'last_err', 'type':'i', 'mt':r'last_err:'+common_def.MT_VALUE_VALID_POSTFIX},
                      {'key':'run_ret', 'type':'i', 'mt':r'run_ret:'+common_def.MT_VALUE_VALID_POSTFIX},
                      {'key':'task_name', 'type':'s', 'mt':r'task_name:'+common_def.MT_VALUE_VALID_POSTFIX},
                      {'key':'task_ver', 'type':'s', 'mt':r'task_ver:'+common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'MAC',    'type':'s', 'mt':r'MAC:'+common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                    ]
        mr_base.__init__(self,mt_type,"DRTASKMGR")

mr_obj = MR_DRTASKMGR()

if __name__ == '__main__':
    strTest = r'<SRC:MUSIC_8.1.2.0_PQ|ACT:DRTASKMGR|S:Info|TYPE:RUN|err_type:0|last_err:0|run_ret:0|task_name:1003|task_ver:1.0.1.3|PROD:MUSIC|VER:8.1.2.0_PQ|PLAT:WIN32|FROM:KwMusic_8.1.2.0.exe|UI:67448976|MAC:BC5FF4816D8C|{KwMusic_8.1.2.0.exe}|U:48703901>(123.186.13.199)TM:1461124803'
    mr_obj.LocalTest(strTest)
    pass
