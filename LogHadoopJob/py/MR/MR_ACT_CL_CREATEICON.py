#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_CL_CREATEICON"
class MR_ACT_CL_CREATEICON(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'err_ret','type':'i', 'mt':r'err_ret:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'sub_ret','type':'i', 'mt':r'sub_ret:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'name','type':'s', 'mt':r'name:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'icon_id','type':'i', 'mt':r'id:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'org','type':'i', 'mt':r'from:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_ACT_CL_CREATEICON()

if __name__ == '__main__':
    test_str = r'08:23| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSICDATAREPAIR|S:1003|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:6.1.7601.2_Service Pack 1|PLAT:WIN32|VER:1.0.1.8|GID:3873|CHID:MUSICDATAREPAIR|PN:rundll32.exe|MAC:B8975AA983C6|UAC:0|ADMIN:1|ST:1488988070|CFGVER:26|ACT:ACT_CL_CREATEICON||err_ret:0|sub_ret:-1|name:美女秀|id:0|from:1|{}|U:>(124.130.103.234)TM:1488989304'
    mr_obj.LocalTest(test_str)
    pass
