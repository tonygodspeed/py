#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "SKIN"
class MR_SKIN(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'SUBKEY',   'type':'s', 'mt':r'SUBKEY:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'APP_K', 'type':'s', 'mt':r'APP_K:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    #{'key':'APP_V', 'type':'s', 'mt':r'APP_V:'+ common_def.MT_VALUE_INVALID_POSTFIX},

                    {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END}
                  ]
        mr_base.__init__(self,mt_type,str_act)



mr_obj = MR_SKIN()

if __name__ == '__main__':
    test_str = r'[KNF]: <SRC:MUSIC_8.3.0.0_BCS23|ACT:SKIN|S:KwMusic|SUBKEY:BKSKIN|CHANNEL_NAME:|PROD:MUSIC|VER:8.3.0.0_BCS23|PLAT:WIN32|FROM:KwMusic8.1.2.0_BCS36.exe|UI:190865810|{KwMusic8.1.2.0_BCS36.exe}|K:131589172|RESEND:0|U:22592927'
    mr_obj.LocalTest(test_str)
    pass
