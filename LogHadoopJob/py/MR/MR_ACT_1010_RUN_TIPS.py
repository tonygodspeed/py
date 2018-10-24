#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_1010_RUN_TIPS"
class MR_MUSICTIP_POPUP_SHOW(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MVER','type':'s', 'mt':r'MVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'task_name','type':'s', 'mt':r'task_name:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'nret','type':'i', 'mt':r'nret:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'last_err','type':'i', 'mt':r'last_err:'+ common_def.MT_VALUE_INVALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_MUSICTIP_POPUP_SHOW()

if __name__ == '__main__':
    test_str = r'41:05| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8500PQ|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:2.0.4.15|GID:2518|CHID:MUSIC8500PQ|PN:rundll32.exe|MAC:408D5C0B1AF2|UAC:0|ADMIN:1|MVER:|MCID:|ST:1517801397|CFGVER:40|ACT:ACT_1010_RUN_TIPS|task_name:ad_tips|nret:0|last_err:0|{}|U:>(221.198.135.201)TM:1517802066'
    mr_obj.LocalTest(test_str)
    pass
