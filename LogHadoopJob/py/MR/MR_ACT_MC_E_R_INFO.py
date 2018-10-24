#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_MC_E_R_INFO"
class MR_ACT_MC_E_R_INFO(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MCID','type':'s', 'mt':r'MCID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'1_e','type':'i', 'mt':r'1_e:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'2_e','type':'i', 'mt':r'2_e:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'3_e','type':'i', 'mt':r'3_e:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'4_e','type':'i', 'mt':r'4_e:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'5_e','type':'i', 'mt':r'5_e:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'1_r','type':'i', 'mt':r'1_r:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'2_r','type':'i', 'mt':r'2_r:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'3_r','type':'i', 'mt':r'3_r:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'4_r','type':'i', 'mt':r'4_r:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'5_r','type':'i', 'mt':r'5_r:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'1_play_times','type':'i', 'mt':r'1_play_times:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'2_play_times','type':'i', 'mt':r'2_play_times:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_ACT_MC_E_R_INFO()

if __name__ == '__main__':
    test_str = r'31:31| [INFO]: <SRC:KWSHELLEXT_1.0.6.9060_MUSIC8720BCS4|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:5.1.2600.2_Service Pack 3|PLAT:WIN32|VER:2.0.4.0|GID:552|CHID:MUSIC8720BCS4|PN:rundll32.exe|MAC:64D954A9CA53|UAC:0|ADMIN:1|MVER:MUSIC_8.7.2.0_BCS4|MCID:|ST:1493281915|CFGVER:17|ACT:ACT_MC_E_R_INFO|1_e:1|2_e:1|3_e:1|4_e:0|5_e:1|1_r:0|2_r:0|3_r:0|4_r:0|5_r:0||1_play_times:0|2_play_times:0|{}|U:>(111.207.202.7)TM:1493281892'
    mr_obj.LocalTest(test_str)
    pass
