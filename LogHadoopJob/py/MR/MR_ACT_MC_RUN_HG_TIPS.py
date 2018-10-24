#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_MC_RUN_HG_TIPS"
class MR_ACT_MC_RUN_HG_TIPS(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'c_type','type':'i', 'mt':r'c_type:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    #{'key':'total_cnt','type':'i', 'mt':r'total_cnt:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_ACT_MC_RUN_HG_TIPS()

if __name__ == '__main__':
    test_str = r'17:01| [INFO]: <SRC:KWSHELLEXT_1.0.6.9060_MUSIC8500PQ|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:2.0.4.5|GID:552|CHID:MUSIC8500PQ|PN:TKwMonitor.exe|MAC:D8CB8A68A2AC|UAC:1|ADMIN:1|MVER:MUSIC_8.6.0.0_W0|MCID:15710039|ST:1495077171|CFGVER:17|ACT:ACT_MC_RUN_HG_TIPS|c_type:4|{}|U:>(111.207.202.9)TM:1495077422'
    mr_obj.LocalTest(test_str)
    pass
