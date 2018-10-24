#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "COMMON_START_1011"
class MR_COMMON_START_1011(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MVER','type':'s', 'mt':r'MVER:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'MCID','type':'s', 'mt':r'MCID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'exist_ret','type':'i', 'mt':r'exist:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                    #{'key':'lp','type':'s', 'mt':r'last:'+ common_def.MT_VALUE_INVALID_POSTFIX },
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_COMMON_START_1011()

if __name__ == '__main__':
    test_str = r'54:17| [INFO]: <SRC:|S:1011|PROD:KWSHELLEXT|DISVER:|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.1.8|GID:|CHID:|PN:rundll32.exe|MAC:54353098D1FE|UAC:0|ADMIN:1|MVER:MUSIC_8.5.1.0_PQ|MCID:19621865|ST:1479293663|CFGVER:0|ACT:COMMON_START_1011||exist:0|{}|U:>(111.207.202.3)TM:1479293659'
    mr_obj.LocalTest(test_str)
    pass
