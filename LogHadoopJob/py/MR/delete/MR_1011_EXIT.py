#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_MUSICTIPS_EXIT"
class MR_MUSICTIPS_EXIT(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MVER','type':'s', 'mt':r'MVER:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'MCID','type':'s', 'mt':r'MCID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'ret','type':'i', 'mt':r'ret:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'subret','type':'i', 'mt':r'subret:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                    #{'key':'lp','type':'s', 'mt':r'last:'+ common_def.MT_VALUE_INVALID_POSTFIX },
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_MUSICTIPS_EXIT()

if __name__ == '__main__':
    test_str = r'43:52| [INFO]: <SRC:KWSHELLEXT_1.0.6.9030_MUSIC8500BCSP|S:1011|PROD:KWSHELLEXT|DISVER:1.0.6.9061|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.1.7|GID:1601|CHID:MUSIC8500BCSP|PN:TMusicTips.exe|MAC:FFFF577E1E34|UAC:1|ADMIN:0|MVER:MUSIC_8.5.0.0_BCS57|MCID:63044864|ST:1479278975|CFGVER:9|ACT:ACT_MUSICTIPS_EXIT||ret:4|subret:0|{}|U:>(111.207.202.10)TM:1479278634'
    mr_obj.LocalTest(test_str)
    pass
