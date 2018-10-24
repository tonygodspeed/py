#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "COMMON_START_1009"
class MR_COMMON_START_1009(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_COMMON_START_1009()

if __name__ == '__main__':
    test_str = r'52:49| [INFO]: <SRC:KWSHELLEXT_1.0.6.9060_MUSIC8310PT|S:1009|PROD:KWSHELLEXT|DISVER:1.0.6.9060|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.0.1|GID:552|CHID:MUSIC8310PT|PN:rundll32.exe|MAC:D8CB8A68A2AC|UAC:1|ADMIN:1|ST:1471575167|CFGVER:0|ACT:COMMON_START_1009||{}|U:>(111.207.202.7)TM:1471575170'
    mr_obj.LocalTest(test_str)
    pass
