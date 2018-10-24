#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "SW_DETECT_SW"
class MR_SW_DETECT_SW(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'s_key','type':'s', 'mt':r'key:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'l_value','type':'s', 'mt':r'value:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_SW_DETECT_SW()

if __name__ == '__main__':
    test_str = r'26:40| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8400W6|S:1009|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:5.1.2600.2_Service Pack 3|PLAT:WIN32|VER:1.0.0.2|GID:1723|CHID:MUSIC8400W6|PN:rundll32.exe|MAC:00142A39BCDC|UAC:0|ADMIN:1|ST:1483485999|CFGVER:9|ACT:SW_DETECT_SW|key:酷我音乐|value:酷我音乐|{}|U:>(1.180.208.84)TM:1483486001'
    mr_obj.LocalTest(test_str)
    pass
