#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ANDROID_CONNECT"
class MR_ANDROID_CONNECT(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'a_vid', 'type':'s', 'mt':r'a_vid:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'a_pid', 'type':'s', 'mt':r'a_pid:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'a_manu', 'type':'s', 'mt':r'a_manu:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'a_product', 'type':'s', 'mt':r'a_product:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'a_note', 'type':'s', 'mt':r'a_note:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END}
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_ANDROID_CONNECT()

if __name__ == '__main__':
    test_str = r'[KNF]: SRC:MUSIC_8.5.0.0_BCS48|ACT:ANDROID_CONNECT|S:KwMusic|a_vid:1EBF|a_pid:702B|a_serial:Coolpad8675-HD-0x02a22c6e|a_manu:MediaTek|a_product:MT65xx Android Phone|a_note:coolpad 8675-hd|CHANNEL_NAME:|PROD:MUSIC|VER:8.6.0.0_BCS19|PLAT:WIN32|FROM:KwMusic8.4.0.0_BCS36.exe|UI:202460999|{KwMusic8.4.0.0_BCS36.exe}|K:300126687|RESEND:0|U:22592927'
    mr_obj.LocalTest(test_str)
    pass
