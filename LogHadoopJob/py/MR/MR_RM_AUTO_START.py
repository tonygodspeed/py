#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "RM_AUTO_START"
class MR_RM_AUTO_START(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'ret','type':'i', 'mt':r'ret:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'last_err','type':'i', 'mt':r'last_err:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'org','type':'i', 'mt':r'from:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_RM_AUTO_START()

if __name__ == '__main__':
    test_str = r'28:00| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8520PQ3|S:TipUtility|PROD:KWSHELLEXT|MAC:201A06BBF9A5|ACT:RM_AUTO_START|ret:0|last_err:0|{}|U:>=(1.180.212.145)TM:1485066482'
    mr_obj.LocalTest(test_str)
    pass
