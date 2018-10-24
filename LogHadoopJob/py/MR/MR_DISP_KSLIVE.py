#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_DISP_KSLIVE"
class MR_DISP_KSLIVE(mr_base):
    def __init__(self):
        mt_type =  [
					{'key':'SRC',    'type':'s',  'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
	                {'key':'MAC',    'type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
					{'key':'awn',     'type':'s', 'mt':r'awn:'+ common_def.MT_VALUE_INVALID_POSTFIX},
					{'key':'reg',     'type':'i', 'mt':r'reg:'+ common_def.MT_VALUE_VALID_POSTFIX},
					{'key':'file',    'type':'i', 'mt':r'file:'+ common_def.MT_VALUE_INVALID_POSTFIX},
					{'key':'Times',   'type':'i', 'mt':r'times:'+ common_def.MT_VALUE_INVALID_POSTFIX + common_def.MT_VALUE_END},

                    ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_DISP_KSLIVE()

if __name__ == '__main__':
    strTest =  r'00:09| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8120PE|S:DISPATCHER|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.6.9077|GID:2349|CHID:MUSIC8120PE|PN:rundll32.exe|MAC:FCAA1482B884|UAC:0|ADMIN:1|MVER:MUSIC_8.4.1.0_AN0|MCID:9573280|ST:1501515241|CFGVER:37|ACT:ACT_DISP_KSLIVE|awn:360安全卫士 ;360安全卫士 ;360安全卫士 ;360安全卫士 ;|reg:0|file:1|core:1|times:940|{}|U:>(183.204.45.5)TM:1501516810'
    mr_obj.LocalTest(strTest)
    pass