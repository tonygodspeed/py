#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

class MR_CRASH_REPORT(mr_base):
    def __init__(self):
        mt_type =  [
                      {'key':'SRC',    'type':'s', 'mt':r'^.*<SRC:KWSHELLEXT_[\.0-9]*_'+common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'DISVER', 'type':'s', 'mt':r'DISVER:'+ common_def.MT_VALUE_VALID_POSTFIX},
                      {'key':'OS',     'type':'s', 'mt':r'OS:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                      #{'key':'GID',    'type':'i', 'mt':r'GID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'MAC',    'type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'MODULE',  'type':'s', 'mt':r'MOD:'+ common_def.MT_VALUE_VALID_POSTFIX},
                      {'key':'FVER',   'type':'s', 'mt':r'.*_[0-9A-Za-z]+_([0-9.]+)_'},
                      {'key':'FNAME',  'type':'s', 'mt':r'([0-9A-Za-z_.]*)_.*\|' + common_def.MT_VALUE_END},
                    ]
        mr_base.__init__(self,mt_type,"ACT_CRASHREPORT")

mr_obj = MR_CRASH_REPORT()

if __name__ == '__main__':
    #strTest = r'<SRC:KWSHELLEXT_1.0.6.9012_MUSIC8032P2T1|S:DumpReport|PROD:KWSHELLEXT|DISVER:1.0.6.9012|OS:6.1.7601.2_Service Pack 1|PLAT:WIN32|VER:1.0.1.4|GID:510|CHID:MUSIC8032P2T1|PN:KsDumpReport.exe|MAC:000B2F3F53FA|UAC:0|ADMIN:1|ST:1461083069|ACT:ACT_CRASHREPORT||MOD:DISPATCHER|FEXT:_MUSIC8032P2T1_1.0.6.9012_kflask510_core.dll_000B2F3F53FA.dmp|FTIME:201604200024|{}|U:>(111.15.60.55)TM:1461083058'
    strTest = r'17:34| [INFO]: <SRC:KWSHELLEXT_0.0.0.0_MUSIC8120W1|S:DISPATCHER|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:6|VER:1.0.6.9072|CHID:MUSIC8120W1|PN:rundll32.exe|MAC:605718DB02F3|UAC:0|ADMIN:1|ST:1473981455|CFGVER:10|ACT:ACT_CRASHREPORT|MOD:DISPATCHER|MODVER:1.0.6.9072|FEXT:_MUSIC8120W1_1.0.6.9072_kclap503_core.dll_605718DB02F3_x86.dmp|FTIME:201609160717|SCfg:1|{}|U:>(122.194.165.145)TM:1473981455'
    mr_obj.LocalTest(strTest)
    pass