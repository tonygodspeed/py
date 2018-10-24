#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_KWLIVEAD_MONITOR_STOP"
class MR_KWLIVEAD_MONITOR_STOP(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:KWSHELLEXT_[\.0-9]*_' + common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX + common_def.MT_VALUE_END},
                    #{'key':'mt','type':'s', 'mt':r'mt:'+ common_def.MT_VALUE_INVALID_POSTFIX +},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_KWLIVEAD_MONITOR_STOP()

if __name__ == '__main__':
    test_str = r'<SRC:KWSHELLEXT_1.0.6.9051_MUSIC8500PT|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:10.0.14393.2_|PLAT:X64|VER:2.0.2.17|GID:2746|CHID:MUSIC8500PT|PN:rundll32.exe|MAC:507B9D78CC15|UAC:1|ADMIN:0|MVER:MUSIC_8.5.1.0_PT|MCID:49692127|ST:1481424388|CFGVER:14|ACT:ACT_KWLIVEAD_MONITOR_STOP|mt:【声优乐】双十二，你要剁了吗？-斗鱼 - 每个人的直播平台 和 3 个其他页面 ?- Microsoft Edge|{}|U:>(222.223.152.167)TM:1481472007'
    mr_obj.LocalTest(test_str)
    pass
