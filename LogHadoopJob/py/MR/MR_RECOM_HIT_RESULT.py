#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_RECOM_HIT_RESULT"
class MR_RECOM_HIT_RESULT(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'total','type':'i', 'mt':r'total:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'sp_cnt','type':'i', 'mt':r'sp_cnt:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'kw_cnt','type':'i', 'mt':r'kw_cnt:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'web_cnt','type':'i', 'mt':r'web_cnt:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'spec_cnt','type':'i', 'mt':r'spec_cnt:'+ common_def.MT_VALUE_INVALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_RECOM_HIT_RESULT()

if __name__ == '__main__':
    test_str = r'2%09<SRC:KWSHELLEXT_1.0.6.9020_MUSIC8200BD2|S:1005|PROD:KWSHELLEXT|DISVER:1.0.6.9020|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.1.4|GID:733|CHID:MUSIC8200BD2|PN:rundll32.exe|MAC:D8CB8A68A2AC|UAC:1|ADMIN:1|ST:1464776927|ACT:ACT_RECOM_HIT_RESULT|total:2|sp_cnt:0|kw_cnt:0|web_cnt:2|spec_cnt:0|{}|U:>'
    mr_obj.LocalTest(test_str)
    pass
