#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "INSTALL_INFO"
class MR_INSTALL_INFO(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'SUC', 'type':'s', 'mt':r'Suc:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    #{'key':'APP_V', 'type':'s', 'mt':r'APP_V:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    #{'key':'QUALITY','type':'s', 'mt':common_def.MT_VALUE_BETWEEN('S','CHANNEL_NAME'),'cb_kv':self.MapperKvCb},
                    {'key':'MAC',     'type':'s', 'mt':r'MAC:' + '([^>]*)' + common_def.MT_VALUE_END}
                  ]
        mr_base.__init__(self,mt_type,str_act)

    def MapperDataCb(self,data):
        pos = data.find('Suc:')
        str_ret = ""
        if pos!= -1:
            pos_end = data.find("|",pos)
            str_ret = data[pos+len("SUC:"):pos_end]
        else:
            str_ret = "-1"
        str_ret += "\t"

        pos = data.find('|TYPE:')
        if pos != -1:
            pos_end = data.find("|",pos+1)
            str_ret += data[pos+len("|TYPE:"):pos_end]
        else:
            str_ret += "-1"
        return str_ret

    def InitReducer(self,value):
        try:
            ap = {'key':'SUC','type':'i','mt':''}
            self.mt_type.append(ap)
            ap = {'key':'TYPE','type':'s','mt':''}
            self.mt_type.append(ap)
            common_util.X_InitReducer(value,self.mt_type)
        except BaseException,e:
            return
mr_obj = MR_INSTALL_INFO()

if __name__ == '__main__':
    test_str = r'29:09| [INFO]: <SRC:MUSIC_8.1.2.0_PQ3|ACT:INSTALL_INFO|TYPE:StartSetup|TCount:1483750|{KwMusicSetup_360.exe}|U:|MAC:003018AF8632>}(117.141.9.174)TM:1462465751'
    #test_str = r'36:36| [INFO]: <SRC:MUSIC_8.1.2.0_P2T1|ACT:INSTALL_INFO|Suc:1|DisplayCompletePage:0|HasShowCheck:0|HasUnCheck:0|HasStartMusicBox:0|ExcptionAbort:0.2|SKIPTYPE:0|AutoRun:1|Stage:93|InstallTick:137639|ExitType:1|TCount:140182|{kuwo_jm636.exe}|U:|MAC:00219B0F5F39>(139.206.195.65)TM:1462466194'
    mr_obj.LocalTest(test_str)
    pass
