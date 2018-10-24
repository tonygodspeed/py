#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_AUTORUN_MUSICBOX"
class MR_ACT_AUTORUN_MUSICBOX(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MVER','type':'s', 'mt':r'MVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MCID','type':'s', 'mt':r'MCID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'nret','type':'i', 'mt':r'nret:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                    #{'key':'last_err','type':'i', 'mt':r'last_err:'+ common_def.MT_VALUE_INVALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_ACT_AUTORUN_MUSICBOX()

if __name__ == '__main__':
    test_str = r'01:19| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8740PQ3|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:2.0.4.20|GID:5431|CHID:MUSIC8740PQ3|PN:TKwMonitor.exe|MAC:D8CB8A68A2AC|UAC:1|ADMIN:1|MVER:MUSIC_8.7.7.0_BCS9|MCID:15710039|ST:1522119634|CFGVER:41|ACT:ACT_AUTORUN_MUSICBOX|nret:0|{}|U:>(111.207.202.10)TM:1522119680'
    mr_obj.LocalTest(test_str)
    pass
