#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_REG"
class MR_MUSIC_REG(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'mac',   'type':'s', 'mt':r'.*\|mac:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'hd','type':'s', 'mt':r'hd:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'vmac','type':'s', 'mt':r'vmac:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'act','type':'s', 'mt':r'\|act:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_MUSIC_REG()

if __name__ == '__main__':
    test_str = r'00:01:21]recv:124.13.98.112&.auth&72&EAFYWFBdXRRJU1JKBA4NHU9dI1tbVy8RTVNXXE8HCh1fEwgNClJeED8jUS5eXl5hTiZDGgwdUwYKFwZRAhoZT0tVVFlHChZF|ret:5|req:id=49234067&mac=68F728A14620&hd=&vmac=00FF4B710A7C&ver=&src=kuwo2015.exe|type:0|id:49234067|mac:68F728A14620|hd:|vmac:00FF4B710A7C|ver:|src:kuwo2015.exe|dev:|subchl:|act:badRecv|replyid:0|idfrom:'
    mr_obj.LocalTest(test_str)
    pass
