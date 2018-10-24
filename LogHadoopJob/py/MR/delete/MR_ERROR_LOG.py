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
                      {'key':'NONE',     'type':'s', 'mt':r'ERR:DLMUSIC.*'},
                      #{'key':'SUBERR',  'type':'s', 'mt':r'SUBERR:' + common_def.MT_VALUE_VALID_POSTFIX},
                      #{'key':'MSG',     'type':'s', 'mt':r'MSG:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                      {'key':'U',     'type':'i', 'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END},
                    ]
        mr_base.__init__(self,mt_type,"ERROR_LOG")

mr_obj = MR_ERROR_LOG()

if __name__ == '__main__':
    #strTest = r'<SRC:MUSIC_8.1.2.0_P2T1|ACT:ERROR_LOG|S:KwMusic|ERRTYPE:CLIENT|MODULE:kwmusic|ERR:SERVICECRASH|SUBERR:kwservice|MSG:CheckServerThread|CHANNEL_NAME:kuwo_jm637.exe|PROD:MUSIC|VER:8.1.2.0_P2T1|PLAT:WIN32|FROM:kuwo_jm637.exe|UI:|{kuwo_jm637.exe}|K:222468|RESEND:0|U:46653413>(171.215.12.69)TM:1459958397'
    strTest = r'13:00| [INFO]: <SRC:MUSIC_8.5.0.0_BCS53|ACT:ERROR_LOG|S:KwMusic|ERRTYPE:CLIENT|MODULE:kwmusic|ERR:DLMUSIC|SUBERR:|MSG:U:17103272|N:1486218735393weixin|UID:355525668|NA:开心就好(《福星高照猪八戒》电视剧主题曲)|AR:王子鸣|AL:|F:mp3|RID:MUSIC_558723|S1:58201423|S2:954034441|PSRC:VER=2015;FROM=曲库->分类->开车->开心就好|FINISH:0|ERRORCODE:0|ISVIP:1|VIPTY:1|VIPLV:-1|UQ:HQ|RQ:HQ|DP:|DSRC:|DMOD:netsong2015|FROM:普通下载|CHANNEL_NAME:10001_01|PROD:MUSIC|VER:8.5.0.0_BCS53|PLAT:WIN32|FROM:kwmusic2016_web_1_BCS_20161028.exe|UI:355525668|{kwmusic2016_web_1_BCS_20161028.exe}|K:225929544|RESEND:0|U:17103272|DEP:1>(111.56.13.172)TM:1486223891'
    mr_obj.LocalTest(strTest)
    pass
