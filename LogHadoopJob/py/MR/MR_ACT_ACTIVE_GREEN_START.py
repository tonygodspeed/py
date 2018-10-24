#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_ACTIVE_GREEN_START"
class MR_ACT_ACTIVE_GREEN_START(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'filter_type','type':'i', 'mt':r'filter_type:'+ common_def.MT_VALUE_VALID_POSTFIX },
                    #{'key':'total_cnt','type':'i', 'mt':r'total_cnt:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_ACT_ACTIVE_GREEN_START()

if __name__ == '__main__':
    test_str = r'14:48| [INFO]: <SRC:KWSHELLEXT_1.0.6.9072_MUSIC8520P2T2|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:2.0.3.0|GID:2304|CHID:MUSIC8520P2T2|PN:rundll32.exe|MAC:D8CB8A68A2AC|UAC:1|ADMIN:1|MVER:|MCID:|ST:1482473624|CFGVER:16|ACT:ACT_ACTIVE_GREEN_START||filter_type:2|{}|U:>(111.207.202.4)TM:1482473688'
    mr_obj.LocalTest(test_str)
    pass
