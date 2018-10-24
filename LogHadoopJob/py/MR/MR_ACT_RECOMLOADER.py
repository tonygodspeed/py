#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_RECOMLOADER"
class MR_RECOMLOADER(mr_base):
    def __init__(self):
        mt_type = [
					{'key':'SRC',    'type':'s', 'mt':r'^.*<SRC:KWSHELLEXT_[\.0-9]*_'+common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'DISVER', 'type':'s', 'mt':r'DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER', 'type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC',    'type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'ret','type':'i', 'mt':r'ret:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'subret','type':'i', 'mt':r'subret:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_RECOMLOADER()

if __name__ == '__main__':
    test_str = r'<SRC:KWSHELLEXT_1.0.6.9030_MUSIC8310W4|S:1007|PROD:KWSHELLEXT|DISVER:1.0.6.9040|OS:5.1.2600.2_Service Pack 3|PLAT:WIN32|VER:1.0.1.1|GID:544|CHID:MUSIC8310W4|PN:rundll32.exe|MAC:000C29E46305|UAC:0|ADMIN:1|ST:1467268340|CFGVER:2|ACT:ACT_RECOMLOADER||ret:0|subret:0|{}|U:>(111.207.202.4)TM:1467268340'
    mr_obj.LocalTest(test_str)
    pass
