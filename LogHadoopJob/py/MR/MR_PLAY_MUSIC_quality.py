#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")
condition = os.environ.get('condition')

class MR_PLAY_MUSIC(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'NONE',    'type':'s',  'mt':r'^.*<SRC:MUSIC_8.3.0.0_PT.*T:0.*'},
                    {'key': 'F', 'type': 's', 'mt': r'F:' + common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key': 'NONE', 'type': 's', 'mt': r'RID:.*'},
                    {'key': 'CACHE', 'type': 'i', 'mt': r'CACHE:' + common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'U',      'type':'i',  'mt':common_def.MT_VALUE_U + common_def.MT_VALUE_END},
                      #{'key':'IMEI',   'type':'i',  'mt':r'IMEI:' + common_def.MT_VALUE_INVALID_POSTFIX},
                      #{'key':'DEV',    'type':'s',  'mt':r'DEV:' + common_def.MT_VALUE_VALID_POSTFIX},
                      #{'key':'OSV',    'type':'s',  'mt':r'OSV:' + common_def.MT_VALUE_INVALID_POSTFIX + "$"},
                  ]
        mr_base.__init__(self,mt_type,"PLAY_MUSIC")

    def InitReducer(self, value):
        try:
            common_util.X_InitReducer(value+"QUALITY", self.mt_type)
        except BaseException, e:
            return
    """
    def ProcessMapper(self,value):
        if condition != "word_count":
            mr_base.ProcessMapper(self,value)
        else:
            mr_base.ProcessMapper(self,value)

    def MapperKvCb(self,key,data):
        if key == "NAME":
            print(common_def.WORD_COUNT + "sn:"+lst_v[2])
        elif key == "AR":
            print(common_def.WORD_COUNT + "at:"+lst_v[3])
        elif key == "AL":
            print(common_def.WORD_COUNT + "an:"+lst_v[4])

        return ""
    """
mr_obj = MR_PLAY_MUSIC()

if __name__ == '__main__':
    #strTest = r'<SRC:MUSIC_8.2.0.0_PT|ACT:PLAY_MUSIC|S:KwMV|U:28533825|N:13671013177|T:0|NONE:幻影|AR:谭咏麟|AL:港乐·Alan Live 2002|F:SQ|B:0|D:0|RID:MUSIC_92810|S1:3136182347|S2:1125609929|FV:|PF:0|UI:224079260|DT:0|PSRC:VER=2015;FROM=曲库->歌手->谭咏麟->港乐·Alan&nbsp;Live&nbsp;2002(16953)|radio_src:0|NOWPLAY:artist|SCRN:1920*1080|ENPI:001|LSRC:|ISVIP:0|VIPTY:-1|VIPLV:-1|DLY:0|MTREE:0|GS:1|FSB:0|TMM:0|TMS:0|MULTI:0||BLKTM:0|BLKCNT:0|BR:0|FMT:mp3|ENDTYPE:0|CT:|CACHE:0|CACHEDSZ:11602674|CTYPE:song0|PT:289970|DUR:290|SPEED:87252|FSIZE:11602674|DELAY:2184|FDMT:1170|FDMP:3|FSPT:2168|BLKPOS:0|STARTSIZE:409600|AACRESULT:0|CHANNEL_NAME:10001_01|PROD:MUSIC|VER:8.2.0.0_BCS29|PLAT:WIN32|FROM:kwmusic2016_web_1.exe|UI:|{kwmusic2016_web_1.exe}|K:420118680|RESEND:0|U:28533825>'
    strTest = r'2%09<SRC:MUSIC_8.3.0.0_PT|ACT:PLAY_MUSIC|S:KwMV|U:27067152|N:vvtest1|T:0|NA:青花瓷|AR:周杰伦|AL:我很忙|F:HQ|B:0|D:0|RID:MUSIC_324244|S1:1776556291|S2:2210916518|FV:|PF:0|UI:104995650|DT:0|PSRC:FROM=(0)|radio_src:0|NOWPLAY:songlib|SCRN:1366*768|ENPI:000|LSRC:|ISVIP:1|VIPTY:1|VIPLV:-1|DLY:0|MTREE:0|GS:2|FSB:0|TMM:0|TMS:0|MULTI:0||BLKTM:0|BLKCNT:0|BR:0|FMT:ape|ENDTYPE:1|CT:|CACHE:1|CACHEDSZ:25522718|CTYPE:song1|PT:54488|DUR:237|SPEED:0|FSIZE:25522718|DELAY:313|FDMT:31|FDMP:100|FSPT:203|BLKPOS:0|STARTSIZE:1531363|AACRESULT:0|CHANNEL_NAME:10001_01|PROD:MUSIC|VER:8.5.0.0_BCS1|PLAT:WIN32|FROM:KwMusic8.5.0.0_BCS1.exe|UI:|{KwMusic8.5.0.0_BCS1.exe}|K:3947296|RESEND:0|U:27067152|DEP:1>'
    mr_obj.LocalTest(strTest)
    pass
