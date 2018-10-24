#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "USRCLK_WASAPI_STATE"
class MR_USR_CLK_WASAPI_STATE(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'SUBVALUE','type':'i', 'mt':r'SUBVALUE:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END}
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_USR_CLK_WASAPI_STATE()

if __name__ == '__main__':
    test_str = r'<SRC:MUSIC_8.4.0.0_BCS17|ACT:USRCLK|S:KwMusic|SUBKEY:WASAPI_STATE|SUBVALUE:1|CHANNEL_NAME:10001_01|PROD:MUSIC|VER:8.4.0.0_BCS17|PLAT:WIN32|FROM:kwmusic2016_web_4_BCS.exe|UI:|{kwmusic2016_web_4_BCS.exe}|K:6258548|RESEND:0|U:19113468>(58.35.187.88)TM:1468124864'
    mr_obj.LocalTest(test_str)
    pass
