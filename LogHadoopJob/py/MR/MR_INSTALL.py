#!/usr/bin/env python
# coding=utf8

from MR_BASE import *

reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "INSTALL"
class MR_INSTALL(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'APP_K', 'type':'s', 'mt':r'APP_K:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    #{'key':'APP_V', 'type':'s', 'mt':r'APP_V:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'QUALITY','type':'s', 'mt':common_def.MT_VALUE_BETWEEN('S','CHANNEL_NAME'),'cb_kv':self.MapperKvCb},
                    {'key':'U',     'type':'i', 'mt': common_def.MT_VALUE_U + ".*"},
                    {'key':'N',     'type':'i', 'mt':r'N:' + '([^>]*)' + common_def.MT_VALUE_END}
                  ]
        mr_base.__init__(self,mt_type,str_act)

    def ProcessMapper(self,value):
        res = re.search("SRC:MUSIC_.*",value)
        if res is not None:
            mr_base.ProcessMapper(self,value)

mr_obj = MR_INSTALL()

if __name__ == '__main__':
    test_str = r'59:59| [INFO]: <SRC:MUSIC_8.1.2.0_BD1|DEV:|ACT:INSTALL{KwMusicSetup_bd.exe}|SUBCHANNEL:160003_01|U:30315749|N:1>(31.205.38.97)TM:1462467600'
    #res = re.search("(INSTALL){.*}.*(SUBCHANNEL){0,1}.*$",test_str,re.IGNORECASE)
    res = re.findall("(ACT:|SUBCHANNEL:)([^\|]*)\|",test_str,re.IGNORECASE)

    for k,v in res:
        print(v)
        #print(res.group(1))
    #print(res.pos)
    #print(res.group(1))
    mr_obj.LocalTest(test_str)
    pass
