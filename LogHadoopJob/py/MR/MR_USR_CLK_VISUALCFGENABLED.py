#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "USRCLK_VISUALCONFIG_ENABLED"
class MR_USR_CLK_VISUALDBLCLK(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'SUBVALUE','type':'i', 'mt':r'SUBVALUE:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END}
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_USR_CLK_VISUALDBLCLK()

if __name__ == '__main__':
    test_str = r'44:23| [INFO]: <SRC:MUSIC_8.2.0.0_BCS29|ACT:USRCLK|S:KwMusic|SUBKEY:VISUALCONFIG_ENABLED|SUBVALUE:1|CHANNEL_NAME:|PROD:MUSIC|VER:8.2.0.0_BCS29|PLAT:WIN32|FROM:KwMusic8.1.2.0_BCS49.exe|UI:164378301|{KwMusic8.1.2.0_BCS49.exe}|K:248514238|RESEND:0|U:7872000>(111.207.202.6)TM:1464169464'
    mr_obj.LocalTest(test_str)
    pass
