#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "COMMON_START_1011"
class MR_COMMON_START_1013(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'exist','type':'i', 'mt':r'exist:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_COMMON_START_1013()

if __name__ == '__main__':
    test_str = r'44:35| [INFO]: <SRC:KWSHELLEXT_1.0.6.9060_MUSIC8031PQ|S:1011|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.2.6|GID:552|CHID:MUSIC8031PQ|PN:rundll32.exe|MAC:D8CB8A68A2AC|UAC:1|ADMIN:1|MVER:MUSIC_8.5.0.0_GN2|MCID:15710039|ST:1487817846|CFGVER:25|ACT:COMMON_START_1011||exist:0|{}|U:>(111.207.202.3)TM:1487817849'
    mr_obj.LocalTest(test_str)
    pass
