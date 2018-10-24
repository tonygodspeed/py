#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_MUSICTIP_PLAYMUSIC"
class MR_MUSICTIP_PLAYMUSIC(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MVER','type':'s', 'mt':r'MVER:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'MCID','type':'s', 'mt':r'MCID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'pt','type':'s', 'mt':r'type:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'lp','type':'s', 'mt':r'last:'+ common_def.MT_VALUE_INVALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_MUSICTIP_PLAYMUSIC()

if __name__ == '__main__':
    test_str = r'04:56| [INFO]: <SRC:|S:1011|PROD:KWSHELLEXT|DISVER:|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.1.7|GID:|CHID:|PN:rundll32.exe|MAC:54353098D1FE|UAC:0|ADMIN:1|MVER:MUSIC_8.5.1.0_PQ|MCID:19621865|ST:1479287079|CFGVER:0|ACT:ACT_MUSICTIP_PLAYMUSIC|type:1|last:0|{}|U:>(111.207.202.3)TM:1479287097'
    #test_str = r'00:00| [INFO]: <SRC:KWSHELLEXT_1.0.6.9030_funmusic|S:1003|PROD:KWSHELLEXT|DISVER:1.0.6.9030|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.1.5|GID:935|CHID:funmusic|PN:rundll32.exe|MAC:7824AF9B6D67|UAC:0|ADMIN:1|ST:1467215928|ACT:ACT_CL_QUIT|quit_err:2|from:1|{}|U:>(183.31.115.135)TM:1467215997'
    mr_obj.LocalTest(test_str)
    pass
