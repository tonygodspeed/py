#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")
condition = os.environ.get('condition')

str_act = "DR_P2PSETTING"
class MR_DR_P2PSETTING(mr_base):
    def __init__(self):
        mt_type = [
                      {'key':'SRC',    'type':'s',  'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'TTYPE',  'type':'i',  'mt':r'TTYPE:' + common_def.MT_VALUE_VALID_POSTFIX},
					  {'key':'TSETSIZE',  'type':'i',  'mt':r'TSETSIZE:' + common_def.MT_VALUE_VALID_POSTFIX},
					  {'key':'TUSEDSIZE',  'type':'i',  'mt':r'TUSEDSIZE:' + common_def.MT_VALUE_VALID_POSTFIX},
					  {'key':'TDIRPTC',  'type':'s',  'mt':r'TDIRPTC:' + common_def.MT_VALUE_VALID_POSTFIX},
					  {'key':'TFILES',  'type':'i',  'mt':r'TFILES:' + common_def.MT_VALUE_VALID_POSTFIX},
					  {'key':'TDISK',  'type':'s',  'mt':r'TDISK:' + common_def.MT_VALUE_VALID_POSTFIX},
	        		  {'key':'TDISKT',  'type':'i',  'mt':r'TDISKT:' + common_def.MT_VALUE_VALID_POSTFIX},
	        		  {'key':'TDISKF',  'type':'i',  'mt':r'TDISKF:' + common_def.MT_VALUE_VALID_POSTFIX},
					  {'key':'TUSEDDISKPTC',  'type':'s',  'mt':r'TUSEDDISKPTC:' + common_def.MT_VALUE_VALID_POSTFIX},
					  {'key':'TPATH',  'type':'s',  'mt':r'TPATH:' + common_def.MT_VALUE_VALID_POSTFIX},
					  {'key':'INSTDAY',  'type':'i',  'mt':r'INSTDAY:' + common_def.MT_VALUE_VALID_POSTFIX},
					  {'key':'IQH',  'type':'i',  'mt':r'IQH:' + common_def.MT_VALUE_VALID_POSTFIX},
					  {'key':'ITX',  'type':'i',  'mt':r'ITX:' + common_def.MT_VALUE_INVALID_POSTFIX},
	                  {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_DR_P2PSETTING()

if __name__ == '__main__':
    strTest = r'14:17| [INFO]: <SRC:MUSIC_8.1.2.0_PT|ACT:DR_P2PSETTING|S:Info||TTYPE:1|TSETSIZE:5120|TUSEDSIZE:740|TDIRPTC:0.144531|TFILES:132|TDISK:C:\|TDISKT:97|TDISKF:61|TUSEDDISKPTC:0.007400|TPATH:C:\ProgramData\mcache|INSTDAY:16860|IQH:0|ITX:1|PROD:MUSIC|VER:8.1.2.0_PT|PLAT:WIN32|FROM:kuwo_tx_8.1.2.0.exe|UI:|MAC:B8AEED98D576|{kuwo_tx_8.1.2.0.exe}|U:48461918>(58.217.233.67)TM:1474625657'
    mr_obj.LocalTest(strTest)
    pass
