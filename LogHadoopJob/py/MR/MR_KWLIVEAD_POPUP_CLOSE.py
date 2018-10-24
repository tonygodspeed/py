#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_KWLIVEAD_POPUP_CLOSE"
class MR_KWLIVEAD_POPUP_CLOSE(mr_base_ex):
    def __init__(self):
        mr_base_ex.__init__(self,str_act)
        self.res_type = ["s","s","s","i","i","i"];
        self.res_name = ["VER","CHID","MAC","autoclose","closeret","time"];
        #self.res_spec_str = "S:1010";

mr_obj = MR_KWLIVEAD_POPUP_CLOSE()

if __name__ == '__main__':
    #test_str = r'49:06| [INFO]: <SRC:MUSIC_8.5.2.0_BCS16|ACT:HIFI_LOG|S:KwMusic|TYPE:ENTER_HIFI_DOWNLOAD_PAGE|CHANNEL_NAME:10001_01|PROD:MUSIC|VER:8cs_20161208.exe}|K:546529252|RESEND:0|U:92204504>(60.181.172.98)TM:1481611747'
    test_str = r'00:04| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8500AN0|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:6.1.7601.2_Service Pack 1|PLAT:WIN32|VER:2.0.2.17|GID:2496|CHID:MUSIC8500AN0|PN:rundll32.exe|MAC:D8CB8A093AA4|UAC:0|ADMIN:1|MVER:MUSIC_8.5.0.0_AN0|MCID:35958679|ST:1481324071|CFGVER:14|ACT:ACT_KWLIVEAD_POPUP_CLOSE||autoclose:1|closeret:4|time:30|{}|U:>(14.204.86.100)TM:1481385606'

    mr_obj.LocalTest(test_str)
    pass
