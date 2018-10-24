#!/usr/bin/env python
# coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

class MR_ERROR_LOG(mr_base):
    def __init__(self):
        mt_type =  [
                      {'key':'SRC',    'type':'s', 'mt':r'^.*<SRC:' + common_def.MT_VALUE_INVALID_POSTFIX},
                      #{'key':'ERRTYPE','type':'s', 'mt':r'ERRTYPE:'+ common_def.MT_VALUE_INVALID_POSTFIX},

                      #{'key':'SUBERR',  'type':'s', 'mt':r'SUBERR:' + common_def.MT_VALUE_VALID_POSTFIX},
                      {'key':'MSG',     'type':'s', 'mt':r'MSG:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END},
                    ]
        mr_base.__init__(self,mt_type,"ERROR_LOG")

mr_obj = MR_ERROR_LOG()

if __name__ == '__main__':
    #strTest = r'<SRC:MUSIC_8.1.2.0_P2T1|ACT:ERROR_LOG|S:KwMusic|ERRTYPE:CLIENT|MODULE:kwmusic|ERR:SERVICECRASH|SUBERR:kwservice|MSG:CheckServerThread|CHANNEL_NAME:kuwo_jm637.exe|PROD:MUSIC|VER:8.1.2.0_P2T1|PLAT:WIN32|FROM:kuwo_jm637.exe|UI:|{kuwo_jm637.exe}|K:222468|RESEND:0|U:46653413>(171.215.12.69)TM:1459958397'
    strTest = r'00:02| [INFO]: <SRC:MUSIC_8.1.2.0_BDS2|ACT:ERROR_LOG|S:KwMusic|ERRTYPE:CLIENT|MODULE:kwmusic|ERR:CLOUD|SUBERR:[01;31m[KSYNFAIL[m[K|MSG:code_0;reson_1|CHANNEL_NAME:10001_01|PROD:MUSIC|VER:8.1.2.0_BDS2|PLAT:WIN32|FROM:kwmusic2016_web_4.exe|UI:163841964|{kwmusic2016_web_4.exe}|K:410427843|RESEND:0|U:6152741>(103.1.70.216)TM:1493740803'
    mr_obj.LocalTest(strTest)
    pass
