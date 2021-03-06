#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "USRCLK"
class MR_USR_CLK(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'APP_K', 'type':'s', 'mt':r'APP_K:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    #{'key':'APP_V', 'type':'s', 'mt':r'APP_V:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'QUALITY','type':'s', 'mt':common_def.MT_VALUE_BETWEEN('S','CHANNEL_NAME'),'cb_kv':self.MapperKvCb},
                    {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END}
                  ]
        mr_base.__init__(self,mt_type,str_act)

    def MapperKvCb(self,key,data):
        if(key == "QUALITY"):
            v = data
            if len(data) > 0:
                try:
                    v = data[1:] #temp.split(":",1)
                except Exception,message:
                    v = data
            return v
        else:
            return -1

mr_obj = MR_USR_CLK()

if __name__ == '__main__':
    test_str = r'[KNF]: <SRC:MUSIC_8.3.0.0_BCS23|ACT:USRCLK|S:KwMusic|Eff_Close Click|CHANNEL_NAME:|PROD:MUSIC|VER:8.3.0.0_BCS23|PLAT:WIN32|FROM:KwMusic8.1.2.0_BCS36.exe|UI:190865810|{KwMusic8.1.2.0_BCS36.exe}|K:131589172|RESEND:0|U:22592927'
    mr_obj.LocalTest(test_str)
    pass
