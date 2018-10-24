#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

class MR_APP_TREASURE(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'APP_K', 'type':'s', 'mt':r'APP_K:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'APP_V', 'type':'s', 'mt':r'APP_V:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'T',     'type':'s', 'mt':common_def.MT_VALUE_BETWEEN('VER','UI')},
                    {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END}
                  ]
        mr_base.__init__(self,mt_type,"APPTREASURE")

    """
    def ProcessMapper(self,value,mapper_type = None):
        mr_base.ProcessMapper(self,value,1)

    def MapperKvCb(self,key,data):
        if(key == "T"):
            temp = data[1:]
            k,v = temp.split(":",1)
            return v
        else:
            return data

    def MapperDataCb(self,data):
        pos = data.find('RESEND:')
        str_ret = ""
        if pos!= -1:
            pos_end = data.find("|",pos)
            str_ret = data[pos+len("RESEND:"):pos_end]
        return str_ret

    def InitReducer(self,value):
        try:
            ap = {'key':'RESEND','type':'i','mt':''}
            self.mt_type.append(ap)
            common_util.X_InitReducer(value,self.mt_type)
        except BaseException,e:
            return
    """
mr_obj = MR_APP_TREASURE()

if __name__ == '__main__':
    test_str = r'[INFO]: <SRC:MUSIC_8.0.3.2_BCS10|ACT:APPTREASURE|S:KwMusic|APP_K:Connected|APP_V:CJL7N16328033386|CHANNEL_NAME:10001_02|PROD:MUSIC|VER:8.0.3.2_BCS10|PLAT:WIN32|FROM:kuwo2016[1].exe|UI:|{kuwo2016[1].exe}|K:13977900|RESEND:0|U:54563533>(218.93.249.218)TM:1462243216'
    mr_obj.LocalTest(test_str)
    pass
