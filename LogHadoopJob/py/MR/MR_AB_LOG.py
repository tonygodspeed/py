#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ABLOG"
class MR_AB_LOG(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'APP_K', 'type':'s', 'mt':r'APP_K:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    #{'key':'APP_V', 'type':'s', 'mt':r'APP_V:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VALUE','type':'s', 'mt':common_def.MT_VALUE_BETWEEN('S','CHANNEL_NAME'),'cb_kv':self.MapperKvCb},
                    {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END}
                  ]
        mr_base.__init__(self,mt_type,str_act)

    def MapperKvCb(self,key,data):
        if(key == "VALUE"):
            v = -1
            if len(data) > 0:
                try:
                    v = data[1:] #temp.split(":",1)
                    if v == "LISTENINGTEST_FIRSTSUCCESS" \
                        or v == "LISTENINGTEST_SUCCESS" \
                        or v == "LISTENINGTEST_PLAY" \
                        or v == "VISUALDBLCLK":
                        return v
                    else:
                        v = -1
                except Exception,message:
                    v = -1
            return v
        else:
            return -1

mr_obj = MR_AB_LOG()

if __name__ == '__main__':
    test_str = r'00:00| [INFO]: <SRC:MUSIC_8.2.0.0_BCS17|ACT:ABLOG|S:KwMusic|LISTENINGTEST_FIRSTSUCCESS|CHANNEL_NAME:10001_01|PROD:MUSIC|VER:8.2.0.0_BCS17|PLAT:WIN32|FROM:kwmusic2016_web_4.exe|UI:|{kwmusic2016_web_4.exe}|K:70099029|RESEND:0|U:35738119>(123.14.96.215)TM:1462791603'
    mr_obj.LocalTest(test_str)
    pass
