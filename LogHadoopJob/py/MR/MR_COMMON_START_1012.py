#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "COMMON_START_1012"
class MR_COMMON_START_1012(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'org','type':'s', 'mt':r'from:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'is_run','type':'s', 'mt':r'is_run:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'TipsIDS','type':'s', 'mt':r'TipsIDS:'+ common_def.MT_VALUE_VALID_POSTFIX},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_COMMON_START_1012()

if __name__ == '__main__':
    test_str = r'44:46| [INFO]: <SRC:KWSHELLEXT_1.0.6.9072_MUSIC8520P2T2|S:1012|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.0.1|GID:2304|CHID:MUSIC8520P2T2|PN:TMusicTips.exe|MAC:D8CB8A68A2AC|UAC:1|ADMIN:1|MVER:MUSIC_8.5.0.0_GN2|MCID:15710039|ST:1482486283|CFGVER:16|ACT:COMMON_START_1012|from:4|is_run:0|TipsIDS:tips_cdguide|{}|U:>(111.207.202.4)TM:1482486288'
    mr_obj.LocalTest(test_str)
    pass
