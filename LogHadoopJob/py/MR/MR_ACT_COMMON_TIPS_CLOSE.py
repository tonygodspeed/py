#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_COMMON_TIPS_CLOSE"
class MR_ACT_COMMON_TIPS_CLOSE(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'tips_id','type':'i', 'mt':r'tips_id:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'auto_close','type':'i', 'mt':r'auto_close:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_ACT_COMMON_TIPS_CLOSE()

if __name__ == '__main__':
    test_str = r'59:40| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8410SG1|S:1011|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.0.6|GID:2213|CHID:MUSIC8410SG1|PN:rundll32.exe|MAC:BC5FF46DB772|UAC:0|ADMIN:1|MVER:|MCID:|ST:1488297388|CFGVER:26|ACT:ACT_COMMON_TIPS_CLOSE|tips_id:1001|auto_close:0|{}|U:>(114.238.105.108)TM:148829758'
    mr_obj.LocalTest(test_str)
    pass
