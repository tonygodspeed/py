#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_DISP_GREEN_START"
class MR_DISP_GREEN_START(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'filter_type','type':'i', 'mt':r'filter_type:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'filter_ret','type':'i', 'mt':r'filter_ret:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'tips_exist','type':'i', 'mt':r'tips_exist:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'tips_running','type':'i', 'mt':r'tips_running:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_DISP_GREEN_START()

if __name__ == '__main__':
    test_str = r'06:14| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8120AN0|S:DISPATCHER|PROD:KWSHELLEXT|DISVER:1.0.6.9060|OS:5.1.2600.2_Service Pack 3|PLAT:WIN32|VER:1.0.6.9060|GID:552|CHID:MUSIC8120AN0|PN:rundll32.exe|MAC:000C296B8503|UAC:0|ADMIN:1|ST:1472011763|CFGVER:9|ACT:ACT_DISP_GREEN_START||filter_type:2|filter_ret:0|tips_exist:1|tips_running:0|{}|U:>(111.207.202.7)TM:1472011575'
    mr_obj.LocalTest(test_str)
    pass
