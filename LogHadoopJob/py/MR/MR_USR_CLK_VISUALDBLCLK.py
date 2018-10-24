#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "USRCLK_VISUALDBLCLK"
class MR_USR_CLK_VISUALDBLCLK(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'SUBVALUE','type':'s', 'mt':r'SUBVALUE:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END}
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_USR_CLK_VISUALDBLCLK()

if __name__ == '__main__':
    test_str = r' [INFO]: <SRC:MUSIC_8.4.1.0_PQ|ACT:USRCLK|S:KwMusic|SUBKEY:VISUALDBLCLK|SUBVALUE:SoundVisualView|CHANNEL_NAME:150001_01|PROD:MUSIC|VER:8.4.1.0_PQ|PLAT:WIN32|FROM:酷我音乐_8.4.1.exe|UI:231913301|{酷我音乐_8.4.1.exe}|K:64510600|RESEND:0|U:27720792|DEP:1>(106.37.236.179)TM:1476720010'
    mr_obj.LocalTest(test_str)
    pass
