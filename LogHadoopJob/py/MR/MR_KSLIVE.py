#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

class MR_KSLIVE(mr_base):
    def __init__(self):
        mt_type =  [
                      {'key':'SRC',    'type':'s', 'mt':r'^.*<SRC:KWSHELLEXT_[\.0-9]*_'+ common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'NONE',     'type':'s', 'mt':r'.*\|T:I\|'},
                      {'key':'Reg',     'type':'i', 'mt':r'Reg:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'File',    'type':'i', 'mt':r'File:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'Times',   'type':'i', 'mt':r'Times:'+  common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'MAC',    'type':'s', 'mt':r'MAC:' + common_def.MT_VALUE_INVALID_POSTFIX + common_def.MT_VALUE_END},
                    ]
        mr_base.__init__(self,mt_type,"KSLIVE")

mr_obj = MR_KSLIVE()

if __name__ == '__main__':
    strTest =  r'<SRC:KWSHELLEXT_1.0.3.5034_MUSIC8022P2T1|ACT:KSLIVE|T:I|Reg: 1|Mutex:0|File: |Exp:0|Times:1|S:KWTASKMODULE|PROD:KWSHELLEXT|VER:1.0.3.5030|PLAT:WIN32|FROM:KWSHELLEXT_1.0.3.5034_MUSIC8022P2T1|MAC:D43D7E3D7CBE|X64:0|UAC:0|ADMIN:1|OS:5.1.2600|MN:rundll32.exe|INT:2016-02-19|{KWSHELLEXT_1.0.3.5034_MUSIC8022P2T1}|U:9554203>(119.183.236.35)TM:1460476825'
    mr_obj.LocalTest(strTest)
    pass
