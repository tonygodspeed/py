#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_MUSICTIP_POPUP_SHOW"
class MR_MUSICTIP_POPUP_SHOW(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MVER','type':'s', 'mt':r'MVER:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'MCID','type':'s', 'mt':r'MCID:'+ common_def.MT_VALUE_INVALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_MUSICTIP_POPUP_SHOW()


if __name__ == '__main__':
    test_str = r'29:15| [INFO]: <SRC:KWSHELLEXT_1.0.6.9030_MUSIC8500BCSP|S:1011|PROD:KWSHELLEXT|DISVER:1.0.6.9061|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.2.0|GID:1601|CHID:MUSIC8500BCSP|PN:TMusicTips.exe|MAC:FFFF577E1E34|UAC:1|ADMIN:0|MVER:MUSIC_8.5.0.0_BCS57|MCID:63044864|ST:1479364549|CFGVER:9|ACT:ACT_MUSICTIP_POPUP_SHOW||{}|U:111>(111.207.202.102)TM:1479364156'
    #mt = re.match(".*U:([0-9]*).*\((\s*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s*)\)",test_str,re.IGNORECASE)

    #if mt:
    #    uid = mt.group(1)
    #    ip = mt.group(2);
    #pass;
    mr_obj.LocalTest(test_str)
    pass
