#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "LOCAL_TMP"
class MR_LOCAL_TMP(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'APP_K', 'type':'s', 'mt':r'APP_K:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    #{'key':'APP_V', 'type':'s', 'mt':r'APP_V:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'TONE_QUALITY','type':'s', 'mt':common_def.MT_VALUE_BETWEEN('S','CHANNEL_NAME'),'cb_kv':self.MapperKvCb},
                    {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END}
                  ]
        mr_base.__init__(self,mt_type,str_act)

    def MapperKvCb(self,key,data):
        return data[1:]

mr_obj = MR_LOCAL_TMP()

if __name__ == '__main__':
    test_str = r'32:48| [INFO]: <SRC:MUSIC_8.4.0.0_BCS17|ACT:LOCAL_TMP|S:KwMusic|ADDSONGCLICK|CHANNEL_NAME:10001_01|PROD:MUSIC|VER:8.4.0.0_BCS17|PLAT:WIN32|FROM:kwmusic2016_web_4_BCS.exe|UI:|{kwmusic2016_web_4_BCS.exe}|K:238750344|RESEND:0|U:55783734>(121.22.253.205)TM:1468222369'
    mr_obj.LocalTest(test_str)
    pass
