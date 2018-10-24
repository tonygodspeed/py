#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_COMMON_TIPS_QUIT"
class MR_ACT_COMMON_TIPS_QUIT(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'tips_id','type':'i', 'mt':r'tips_id:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'quit_err','type':'i', 'mt':r'quit_err:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_ACT_COMMON_TIPS_QUIT()

if __name__ == '__main__':
    test_str = r'06:57| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8700W1|S:1011|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.0.6|GID:3848|CHID:MUSIC8700W1|PN:rundll32.exe|MAC:4CCC6A8F412D|UAC:0|ADMIN:1|MVER:MUSIC_8.7.0.0_W1|MCID:116915785|ST:1488298020|CFGVER:26|ACT:ACT_COMMON_TIPS_QUIT||quit_err:1|{}|U:>(171.90.168.99)TM:1488298019'
    mr_obj.LocalTest(test_str)
    pass
