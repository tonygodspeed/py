#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_KWMONITOR_CAN_EXCUTE"
class MR_ACT_KWMONITOR_CAN_EXCUTE(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'NONE','type':'s', 'mt':r'name:LiveShow.*'},
                    {'key':'ret','type':'i', 'mt':r'ret:'+ common_def.MT_VALUE_VALID_POSTFIX },
                    {'key':'subret','type':'i', 'mt':r'subret:'+ common_def.MT_VALUE_VALID_POSTFIX },
                    #{'key':'total_cnt','type':'i', 'mt':r'total_cnt:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_ACT_KWMONITOR_CAN_EXCUTE()

if __name__ == '__main__':
    test_str = r'00:00| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSICDATAREPAIR|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9076|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:2.0.3.0|GID:1985|CHID:MUSICDATAREPAIR|PN:rundll32.exe|MAC:74E543C61B40|UAC:0|ADMIN:1|MVER:MUSIC_8.4.1.0_UG3|MCID:47757432|ST:1484669310|CFGVER:19|ACT:ACT_KWMONITOR_CAN_EXCUTE|name:LiveShow|ret:0|subret:-1|{}|U:>(113.142.247.210)TM:1484668818'
    mr_obj.LocalTest(test_str)
    pass
