#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "FEATURE_LOG"
class MR_FEATURE_LOG(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'APP_K', 'type':'s', 'mt':r'APP_K:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    #{'key':'APP_V', 'type':'s', 'mt':r'APP_V:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'UPQFINISH','type':'i', 'mt':r'UPQFINISH:'+common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END}
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_FEATURE_LOG()

if __name__ == '__main__':
    test_str = r'<SRC:MUSIC_8.4.0.0_BCS36|ACT:FEATURE_LOG|S:KwMusic|FEATURE:UPQUALITY|UPQFINISH:0|CHANNEL_NAME:10001_01|PROD:MUSIC|VER:8.4.0.0_BCS36|PLAT:WIN32|FROM:kwmusic2016_web_1_BCS.exe|UI:48147722|{kwmusic2016_web_1_BCS.exe}|K:72474590|RESEND:0|U:64092752|DEP:1>(111.161.96.70)TM:1469619829'
    mr_obj.LocalTest(test_str)
    pass
