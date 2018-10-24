#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_DISP_UPGRADE"
class MR_DISP_UPGRADE(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID',   'type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'file_type','type':'i', 'mt':r'file_type:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'err_type','type':'i', 'mt':r'err_type:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'last_err','type':'i', 'mt':r'last_err:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'local_ver','type':'s', 'mt':r'local_ver:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'svr_ver','type':'s', 'mt':r'svr_ver:'+ common_def.MT_VALUE_INVALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_DISP_UPGRADE()

if __name__ == '__main__':
    test_str = r'<SRC:KWSHELLEXT_1.0.6.9030_MUSIC8120P2T1|S:DISPATCHER|PROD:KWSHELLEXT|DISVER:1.0.6.9030|OS:10.0.10586.2_|PLAT:WIN32|VER:1.0.6.9030|GID:1380|CHID:MUSIC8120P2T1|PN:rundll32.exe|MAC:204747370716|UAC:0|ADMIN:1|ST:1467221493|ACT:ACT_DISP_UPGRADE|file_type:1|err_type:0|last_err:0|local_ver:1.0.6.8001|svr_ver:1.0.6.8001|{}|U:>(120.2.85.155)TM:1467221494'
    mr_obj.LocalTest(test_str)
    pass
