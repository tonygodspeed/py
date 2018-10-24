#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_TIPS_EXIT"
class MR_ACT_TIPS_EXIT(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'ret','type':'i', 'mt':r'ret:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'subret','type':'i', 'mt':r'subret:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_ACT_TIPS_EXIT()

if __name__ == '__main__':
    test_str = r'32:24| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8700BCS13|S:1012|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:10.0.14393.2_|PLAT:X64|VER:1.0.0.1|GID:3371|CHID:MUSIC8700BCS13|PN:rundll32.exe|MAC:7845C403A55A|UAC:1|ADMIN:0|MVER:MUSIC_8.7.0.0_BCS13|MCID:|ST:1482485302|CFGVER:9|ACT:ACT_TIPS_EXIT||ret:4|subret:0|{}|U:>(111.207.202.8)TM:1482485546'
    mr_obj.LocalTest(test_str)
    pass
