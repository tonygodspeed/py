#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_1010_STAT_UI"
class MR_COMMON_START_1010(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'OS',   'type':'s', 'mt':r'.*OS:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'OS','type':'s', 'mt':r'OS:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MCID','type':'i', 'mt':r'MCID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'ForeApp','type':'s', 'mt':r'ForeApp:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'PlayMusic','type':'i', 'mt':r'PlayMusic:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_COMMON_START_1010()

if __name__ == '__main__':
    test_str = r'31:52| [INFO]: <SRC:KWSHELLEXT_1.0.6.9077_MUSIC9000BCS25|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:2.0.4.20|GID:552|CHID:MUSIC9000BCS25|PN:TKwMonitor.exe|MAC:D8CB8A68A2AC|UAC:1|ADMIN:1|MVER:MUSIC_8.7.5.0_PT|MCID:15710039|ST:1531898996|CFGVER:41|ACT:ACT_1010_STAT_UI|ForeApp:Xshell.exe#Xshell.exe#chrome.exe#Xshell.exe#chrome.exe|PlayMusic:1|{}|U:>(111.207.202.6)TM:1531899112'
    mr_obj.LocalTest(test_str)
    pass
