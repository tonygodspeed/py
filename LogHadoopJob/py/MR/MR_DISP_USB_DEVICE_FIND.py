#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_DISP_USB_DEVICE_FIND"
class MR_DISP_USB_DEVICE_FIND(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'kuwo_run','type':'i', 'mt':r'kuwo_run:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_DISP_USB_DEVICE_FIND()

if __name__ == '__main__':
    test_str = r'59:02| [INFO]: <SRC:KWSHELLEXT_1.0.6.9060_MUSIC8310PT|S:DISPATCHER|PROD:KWSHELLEXT|DISVER:1.0.6.9060|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.6.9060|GID:552|CHID:MUSIC8310PT|PN:rundll32.exe|MAC:D8CB8A68A2AC|UAC:1|ADMIN:1|ST:1471575167|CFGVER:0|ACT:ACT_DISP_USB_DEVICE_FIND|app_device_plugin:1|kuwo_run:0|{}|U:>(111.207.202.7)TM:1471575543'
    mr_obj.LocalTest(test_str)
    pass
