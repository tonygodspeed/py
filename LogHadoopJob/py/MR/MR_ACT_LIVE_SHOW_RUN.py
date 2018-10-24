#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_LIVE_SHOW_RUN"
class MR_ACT_LIVE_SHOW_RUN(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'show_cnt','type':'i', 'mt':r'show_cnt:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'req_cnt','type':'i', 'mt':r'req_cnt:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_ACT_LIVE_SHOW_RUN()

if __name__ == '__main__':
    test_str = r'40:13| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8600AN0|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:2.0.3.2|GID:3535|CHID:MUSIC8600AN0|PN:rundll32.exe|MAC:D8CB8A68A2AC|UAC:1|ADMIN:1|MVER:MUSIC_8.6.0.0_W6|MCID:15710039|ST:1484289494|CFGVER:17|ACT:ACT_LIVE_SHOW_RUN|show_cnt:2|req_cnt:2|{}|U:>(111.207.202.10)TM:1484289614'
    mr_obj.LocalTest(test_str)
    pass
