#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_MC_PLAY_INFO"
class MR_ACT_MC_PLAY_INFO(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MCID','type':'s', 'mt':r'MCID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'c_type','type':'i', 'mt':r'c_type:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_ACT_MC_PLAY_INFO()

if __name__ == '__main__':
    test_str = r'39:42| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8720BCS4|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:2.0.4.0|GID:4251|CHID:MUSIC8720BCS4|PN:rundll32.exe|MAC:7429AF4027C0|UAC:1|ADMIN:1|MVER:MUSIC_8.7.2.0_BCS4|MCID:14445747|ST:1493280406|CFGVER:17|ACT:ACT_MC_PLAY_INFO|c_type:3|{}|U:>(111.207.202.7)TM:1493282383'
    mr_obj.LocalTest(test_str)
    pass
