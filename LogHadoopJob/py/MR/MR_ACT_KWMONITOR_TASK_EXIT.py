#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_KWMONITOR_TASK_EXIT"
class MR_ACT_KWMONITOR_TASK_EXIT(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'task_name','type':'s', 'mt':r'name:'+ common_def.MT_VALUE_VALID_POSTFIX },
                    {'key':'task_type','type':'i', 'mt':r'type:'+ common_def.MT_VALUE_VALID_POSTFIX },
                    {'key':'ret','type':'i', 'mt':r'ret:'+ common_def.MT_VALUE_VALID_POSTFIX },
                    #{'key':'total_cnt','type':'i', 'mt':r'total_cnt:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_ACT_KWMONITOR_TASK_EXIT()

if __name__ == '__main__':
    test_str = r'00:00| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8520UG6|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9076|OS:6.1.7601.2_Service Pack 1|PLAT:WIN32|VER:2.0.3.0|GID:3567|CHID:MUSIC8520UG6|PN:rundll32.exe|MAC:BCAEC5C25EB9|UAC:0|ADMIN:1|MVER:MUSIC_8.5.2.0_UG6|MCID:55882373|ST:1484668528|CFGVER:19|ACT:ACT_KWMONITOR_TASK_EXIT|name:MUSICMONITOR|type:1|ret:1|{}|U:>(42.184.114.126)TM:1484668827'
    mr_obj.LocalTest(test_str)
    pass
