#!/usr/bin/env python
# coding=utf8

from MR_BASE import *

reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_WPS_LAUNCH"
class MR_WPS_LAUNCH(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'ret', 'type':'i', 'mt':r'ret:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'subret', 'type':'i', 'mt':r'subret:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC', 'type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_WPS_LAUNCH()

if __name__ == '__main__':
    test_str = r'35:39| [INFO]: <SRC:MUSIC_8.5.0.0_GN2|ACT:ACT_WPS_LAUNCH|S:Info|ret:0|subret:-4|PROD:MUSIC|VER:8.5.0.0_GN2|PLAT:WIN32|FROM:KwMusic8.5.0.0.exe|UI:|MAC:000C296B8503|{KwMusic8.5.0.0.exe}|U:18602200>(111.207.202.7)TM:1477470941'
    mr_obj.LocalTest(test_str)
    pass
