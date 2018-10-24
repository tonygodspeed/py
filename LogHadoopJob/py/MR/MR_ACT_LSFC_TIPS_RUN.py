#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_LSFC_TIPS_RUN"
class MR_ACT_MC_PLAY_INFO(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MCID','type':'s', 'mt':r'MCID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_ACT_MC_PLAY_INFO()

if __name__ == '__main__':
    test_str = r'12:23| [INFO]: <SRC:KWSHELLEXT_1.0.6.9077_MUSIC8730PQ|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:10.0.14393.2_|PLAT:X64|VER:2.0.4.7|GID:552|CHID:MUSIC8730PQ|PN:rundll32.exe|MAC:7845C403A55A|UAC:1|ADMIN:0|MVER:MUSIC_8.7.3.0_PQ|MCID:28479825|ST:1504580864|CFGVER:17|ACT:ACT_LSFC_TIPS_RUN||{}|U:>(111.207.202.4)TM:1504494745'
    mr_obj.LocalTest(test_str)
    pass
