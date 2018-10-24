#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_RECOM_HIT_DETAILS"
class MR_RECOM_HIT_DETAILS(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'total_k','type':'i', 'mt':r'total_k:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'sp_k','type':'i', 'mt':r'sp_k:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'kw_k','type':'i', 'mt':r'kw_k:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'web_k','type':'i', 'mt':r'web_k:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'total_s','type':'i', 'mt':r'total_s:'+ common_def.MT_VALUE_VALID_POSTFIX},

                    {'key':'sp_s','type':'i', 'mt':r'sp_s:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'kw_s','type':'i', 'mt':r'kw_s:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'web_s','type':'i', 'mt':r'web_s:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'svr_s','type':'i', 'mt':r'svr_s:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'full_recom','type':'i', 'mt':r'full_recom:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'org','type':'i', 'mt':r'from:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_RECOM_HIT_DETAILS()

if __name__ == '__main__':
    test_str = r'44:28| [INFO]: <SRC:KWSHELLEXT_1.0.6.9020_MUSIC8200BD2|S:RECOM_TIPS|PROD:KWSHELLEXT|DISVER:1.0.6.9040|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.2.0|GID:733|CHID:MUSIC8200BD2|PN:RecomTips.exe|MAC:D8CB8A68A2AC|UAC:1|ADMIN:1|ST:1466995463|ACT:ACT_RECOM_HIT_DETAILS|total_k:25|sp_k:1|kw_k:4|web_k:20|total_s:0|sp_s:0|kw_s:0|web_s:0|svr_s:0|full_recom:0|from:-1|{}|U:1>(111.207.202.7)TM:1466995469'
    mr_obj.LocalTest(test_str)
    pass
