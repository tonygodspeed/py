#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "NETEASE_COOKIES_RET"
class MR_NETEASE_COOKIES_RET(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'bret','type':'i', 'mt':r'bret:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_NETEASE_COOKIES_RET()

if __name__ == '__main__':
    test_str = r'06:59| [INFO]: <SRC:KWSHELLEXT_1.0.6.9060_MUSIC8700BCS25|S:1013|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:5.1.2600.2_Service Pack 3|PLAT:WIN32|VER:1.0.0.1|GID:552|CHID:MUSIC8700BCS25|PN:rundll32.exe|MAC:64D954A9CA53|UAC:0|ADMIN:1|MVER:MUSIC_8.7.0.0_BCS25|MCID:|ST:1487570877|CFGVER:17|ACT:NETEASE_COOKIES_RET|bret:0|{}|U:>(111.207.202.7)TM:1487570821'
    mr_obj.LocalTest(test_str)
    pass
