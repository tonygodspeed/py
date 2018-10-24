#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_CL_QUIT"
class MR_CL_QUIT(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'quit_err','type':'i', 'mt':r'quit_err:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_CL_QUIT()

if __name__ == '__main__':
    test_str = r'00:00| [INFO]: <SRC:KWSHELLEXT_1.0.6.9030_funmusic|S:1003|PROD:KWSHELLEXT|DISVER:1.0.6.9030|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.1.5|GID:935|CHID:funmusic|PN:rundll32.exe|MAC:7824AF9B6D67|UAC:0|ADMIN:1|ST:1467215928|ACT:ACT_CL_QUIT|quit_err:2|from:1|{}|U:>(183.31.115.135)TM:1467215997'
    mr_obj.LocalTest(test_str)
    pass
