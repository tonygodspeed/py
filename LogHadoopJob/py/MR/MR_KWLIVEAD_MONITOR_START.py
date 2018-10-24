#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_KWLIVEAD_MONITOR_START"
class MR_KWLIVEAD_MONITOR_START(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:KWSHELLEXT_[\.0-9]*_' + common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_KWLIVEAD_MONITOR_START()

if __name__ == '__main__':
    test_str = r'00:04| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8500AN0|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:6.1.7600.2_|PLAT:WIN32|VER:2.0.2.17|GID:2547|CHID:MUSIC8500AN0|PN:rundll32.exe|MAC:1078D27D5DB2|UAC:0|ADMIN:1|MVER:MUSIC_8.5.0.0_AN0|MCID:36007950|ST:1481385601|CFGVER:14|ACT:ACT_KWLIVEAD_MONITOR_START||{}|U:>(123.241.118.138)TM:1481385605'
    mr_obj.LocalTest(test_str)
    pass
