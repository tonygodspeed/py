#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_KWLIVEAD_POPUP_CLICK"
class MR_KWLIVEAD_POPUP_CLICK(mr_base_ex):
    def __init__(self):
        mr_base_ex.__init__(self,str_act)
        self.res_type = ["s","s","s","i","i"];
        self.res_name = ["VER","CHID","MAC","closeret","time"];
        #self.res_spec_str = "S:1010";

mr_obj = MR_KWLIVEAD_POPUP_CLICK()

if __name__ == '__main__':
    #test_str = r'49:06| [INFO]: <SRC:MUSIC_8.5.2.0_BCS16|ACT:HIFI_LOG|S:KwMusic|TYPE:ENTER_HIFI_DOWNLOAD_PAGE|CHANNEL_NAME:10001_01|PROD:MUSIC|VER:8cs_20161208.exe}|K:546529252|RESEND:0|U:92204504>(60.181.172.98)TM:1481611747'
    test_str = r'<SRC:KWSHELLEXT_1.0.6.9051_MUSIC8500PT|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:10.0.14393.2_|PLAT:X64|VER:2.0.2.17|GID:2562|CHID:MUSIC8500PT|PN:rundll32.exe|MAC:C860009C01D8|UAC:1|ADMIN:0|MVER:MUSIC_8.5.0.0_PT|MCID:57836354|ST:1481337017|CFGVER:14|ACT:ACT_KWLIVEAD_POPUP_CLOSE||autoclose:0|closeret:2|time:5|{}|U:>(222.87.155.143)TM:1481385606'

    mr_obj.LocalTest(test_str)
    pass
