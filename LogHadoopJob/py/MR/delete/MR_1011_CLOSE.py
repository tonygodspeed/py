#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_MUSICTIP_POPUP_CLOSE"
class MR_MUSICTIP_POPUP_CLOSE(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MVER','type':'s', 'mt':r'MVER:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'MCID','type':'s', 'mt':r'MCID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'autoclose','type':'i', 'mt':r'autoclose:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'closeret','type':'i', 'mt':r'closeret:'+ common_def.MT_VALUE_INVALID_POSTFIX + common_def.MT_VALUE_END},
                    #{'key':'quit_err','type':'i', 'mt':r'quit_err:'+ common_def.MT_VALUE_VALID_POSTFIX },
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_MUSICTIP_POPUP_CLOSE()

if __name__ == '__main__':
    test_str = r'11:05| [INFO]: <SRC:|S:1011|PROD:KWSHELLEXT|DISVER:|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.1.7|GID:|CHID:|PN:rundll32.exe|MAC:54353098D1FE|UAC:0|ADMIN:1|MVER:MUSIC_8.5.1.0_PQ|MCID:19621865|ST:1479287409|CFGVER:0|ACT:ACT_MUSICTIP_POPUP_CLOSE||autoclose:0|closeret:2|{}|U:>(111.207.202.3)TM:1479287467'
    mr_obj.LocalTest(test_str)
    pass
