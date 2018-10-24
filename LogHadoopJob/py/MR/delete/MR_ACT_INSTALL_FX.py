#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_INSTALL_FX"
class MR_INSTALL_FX(mr_base):
    def __init__(self):
        mt_type = [
					{'key':'SRC',    'type':'s', 'mt':r'^.*<SRC:KWSHELLEXT_[\.0-9]*_'+common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'DISVER', 'type':'s', 'mt':r'DISVER:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'OS',     'type':'s', 'mt':r'OS:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'GID',    'type':'i', 'mt':r'GID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC',    'type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'RET','type':'i', 'mt':r'RET:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'SubRet','type':'i', 'mt':r'SubRet:'+ common_def.MT_VALUE_VALID_POSTFIX},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_INSTALL_FX()

if __name__ == '__main__':
    #test_str = r'<SRC:KWSHELLEXT_1.0.6.9030_MUSIC8030PQ2|S:1008|PROD:KWSHELLEXT|DISVER:1.0.6.9030|OS:5.1.2600.2_Service Pack 3|PLAT:WIN32|VER:1.0.1.1|GID:544|CHID:MUSIC8030PQ2|PN:rundll32.exe|MAC:000C29E46305|UAC:0|ADMIN:1|ST:1465783078|ACT:ACT_INSTALL_FX|T:FXEXE|RET:0|SubRet:-1|Suc:1|ExcuRet:42|run:0|{}|U:>(111.207.202.4)TM:1465783081'
    test_str = r'<SRC:KWSHELLEXT_1.0.6.9030_MUSIC8200BCS35|S:1008|PROD:KWSHELLEXT|DISVER:1.0.6.9030|OS:10.0.10586.2_|PLAT:WIN32|VER:1.0.1.1|GID:869|CHID:MUSIC8200BCS35|PN:rundll32.exe|MAC:50465D5B11B2|UAC:1|ADMIN:0|ST:1465794805|ACT:ACT_INSTALL_FX|T:FXEXE|RET:4|SubRet:-1|{}|U:>(121.239.96.219)TM:1465794804'
    mr_obj.LocalTest(test_str)
    pass
