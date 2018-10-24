#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_MC_MAX_CNT"
class MR_ACT_MC_MAX_CNT(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'max_cnt','type':'i', 'mt':r'max_cnt:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'total_cnt','type':'i', 'mt':r'total_cnt:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_ACT_MC_MAX_CNT()

if __name__ == '__main__':
    test_str = r'04:34| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8700BCS13|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:10.0.14393.2_|PLAT:X64|VER:2.0.3.0|GID:3371|CHID:MUSIC8700BCS13|PN:rundll32.exe|MAC:7845C403A55A|UAC:1|ADMIN:0|MVER:MUSIC_8.5.0.0|MCID:28479825|ST:1482483645|CFGVER:9|ACT:ACT_MC_MAX_CNT|max_cnt:4|total_cnt:10|{}|U:>(111.207.202.8)TM:1482483875'
    mr_obj.LocalTest(test_str)
    pass
