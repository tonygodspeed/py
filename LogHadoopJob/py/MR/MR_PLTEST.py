#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "PLTEST"
class MR_PLTEST(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'APP_K', 'type':'s', 'mt':r'APP_K:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    #{'key':'APP_V', 'type':'s', 'mt':r'APP_V:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'BTNNAME','type':'s', 'mt':r'BTNNAME:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END}
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_PLTEST()

if __name__ == '__main__':
    test_str = r'35:29| [INFO]: <SRC:MUSIC_8.7.2.0_W1|ACT:PLTEST|S:KwMusic|BTNNAME:BTN_DESKLYRIC|CHANNEL_NAME:10001_01|PROD:MUSIC|VER:8.7.2.0_W1|PLAT:WIN32|FROM:kwmusic_web_1.exe|UI:214887504|{kwmusic_web_1.exe}|K:140347280|RESEND:0|U:153752287>(1.192.38.190)TM:1502159730'
    mr_obj.LocalTest(test_str)
    pass
