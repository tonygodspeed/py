#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_RECOM_REMOVE_STARTUP"
class MR_RECOM_REMOVE_STARTUP(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'nret','type':'i', 'mt':r'nret:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'reg_exist','type':'i', 'mt':r'reg_exist:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'org','type':'i', 'mt':r'from:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_RECOM_REMOVE_STARTUP()

if __name__ == '__main__':
    test_str = r'08:22| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8520PT|S:RECOM_TIPS|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.2.25|GID:3535|CHID:MUSIC8520PT|PN:RecomTips.exe|MAC:D8CB8A68A2AC|UAC:1|ADMIN:1|MVER:MUSIC_8.6.0.0_W0|MCID:15710039|ST:1484654884|CFGVER:17|ACT:ACT_RECOM_REMOVE_STARTUP|nret:0|reg_exist:0|from:-1|green_shot:0|is_green:0|is_auto:1|{}|U:>(111.207.202.10)TM:1484654904'
    mr_obj.LocalTest(test_str)
    pass
