#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "UNINSTALL"
class MR_UNINSTALL(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'APP_K', 'type':'s', 'mt':r'APP_K:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    #{'key':'APP_V', 'type':'s', 'mt':r'APP_V:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'QUALITY','type':'s', 'mt':common_def.MT_VALUE_BETWEEN('S','CHANNEL_NAME'),'cb_kv':self.MapperKvCb},
                    {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END}
                  ]
        mr_base.__init__(self,mt_type,str_act)
    def ProcessMapper(self,value):
        res = re.search("SRC:MUSIC_.*",value)
        if res is not None:
            mr_base.ProcessMapper(self,value)
mr_obj = MR_UNINSTALL()

if __name__ == '__main__':
    test_str = r'47:21| [INFO]: <SRC:MUSIC_8.1.2.0_W6|ACT:UNINSTALL{kwmusic2016_web_6.exe}|U:30040319|N:0>(61.51.129.198)TM:1462499241'
    mr_obj.LocalTest(test_str)
    pass
