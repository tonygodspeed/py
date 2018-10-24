#!/usr/bin/env python
# coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

class MR_DOWN_AD(mr_base):
    def __init__(self):
        mt_type = [
                      {'key':'SRC',    'type':'s', 'mt':r'^.*<SRC:' + common_def.MT_VALUE_INVALID_POSTFIX,'cb_kv':self.MapperKvCb},
                      {'key':'MSG',     'type':'s', 'mt':r'S:KwMusic\|'+common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,"DOWN_AD")

    def MapperKvCb(self,key,data):
    	# 只输出 8400以后的版本
        if(key == "SRC"):
            if len(data) > 13:
                try:
                    ver = data[6:13]
                    if ver >= '8.4.0.0':
                    	return data
                except Exception,message:
                    pass

        return -1

mr_obj = MR_DOWN_AD()
if __name__ == '__main__':
    #test()
    strTest = r'<SRC:MUSIC_8.0.2.0_PQ|ACT:DOWN_AD|S:KwMusic|ShowAd:ID:462|GROUP:1, index = 1|CHANNEL_NAME:150001_01|PROD:MUSIC|VER:8.1.2.0_PQ|PLAT:WIN32|FROM:酷我音乐_8.1.2.0.exe|UI:|{酷我音乐_8.1.2.0.exe}|K:280919160|RESEND:0|U:50108822>(183.185.11.213)TM:1464796801'
    mr_obj.LocalTest(strTest)
    pass