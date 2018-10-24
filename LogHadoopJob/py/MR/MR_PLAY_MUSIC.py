#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")
condition = os.environ.get('condition')

vec_valid_src = [
	"MUSIC_8.7.0.2_PQ"
    "MUSIC_8.5.2.0_BDS8",
    "MUSIC_8.5.0.0_GN2",
    "MUSIC_8.6.0.0_BCS47",
    "MUSIC_8.6.0.0_BCS48",
    "MUSIC_8.5.0.0_PQ",
]

str_act = "PLAY_MUSIC"
class MR_PLAY_MUSIC(mr_base_ex):
    def __init__(self):
        mr_base_ex.__init__(self,str_act)
        self.res_type = ["i","s","s","i","i","s","s","s","s","i","i"];
        self.res_name = ["T","F","RID","GS","CACHE","UUID","UUMAC","TIMESTAMP","UMAC","U"];
        self.res_spec_str = "PROD:MUSIC"
        self.res_spec_mid = ["SRC"];

    def InitReducer(self,value):
        v = value.replace(".","");
        print("========================"+v+"===================")
        self.InitReducerCommon()

    def MapperDataCb(self):
        if self.res_data['SRC'] in vec_valid_src:
            mr_base_ex.MapperDataCb(self);
            line = "";
            for item in self.res_name:
                line = line + self.res_data[item] + "\t"

            for item in self.res_name_ap:
                line = line + self.res_data[item] + "\t"

            if line is not None:
                print(self.act_type + self.res_data['SRC'][5:] + "\t" + line);
        return False;

    '''
    def InitReducer(self,value):
        print("========================"+value+self.res_data['SRC'][5:]+"===================")
        self.InitReducerCommon()
    '''
mr_obj = MR_PLAY_MUSIC()

if __name__ == '__main__':
    #strTest = r'<SRC:MUSIC_8.2.0.0_PT|ACT:PLAY_MUSIC|S:KwMV|U:28533825|N:13671013177|T:0|NONE:幻影|AR:谭咏麟|AL:港乐·Alan Live 2002|F:SQ|B:0|D:0|RID:MUSIC_92810|S1:3136182347|S2:1125609929|FV:|PF:0|UI:224079260|DT:0|PSRC:VER=2015;FROM=曲库->歌手->谭咏麟->港乐·Alan&nbsp;Live&nbsp;2002(16953)|radio_src:0|NOWPLAY:artist|SCRN:1920*1080|ENPI:001|LSRC:|ISVIP:0|VIPTY:-1|VIPLV:-1|DLY:0|MTREE:0|GS:1|FSB:0|TMM:0|TMS:0|MULTI:0||BLKTM:0|BLKCNT:0|BR:0|FMT:mp3|ENDTYPE:0|CT:|CACHE:0|CACHEDSZ:11602674|CTYPE:song0|PT:289970|DUR:290|SPEED:87252|FSIZE:11602674|DELAY:2184|FDMT:1170|FDMP:3|FSPT:2168|BLKPOS:0|STARTSIZE:409600|AACRESULT:0|CHANNEL_NAME:10001_01|PROD:MUSIC|VER:8.2.0.0_PT|PLAT:WIN32|FROM:kwmusic2016_web_1.exe|UI:|{kwmusic2016_web_1.exe}|K:420118680|RESEND:0|U:28533825>'
    #strTest = r'2%09<SRC:MUSIC_8.4.0.0_PQ|ACT:PLAY_MUSIC|S:KwMV|U:27067152|N:vvtest1|T:0|NA:青花瓷|AR:周杰伦|AL:我很忙|F:HQ|B:0|D:0|RID:MUSIC_324244|S1:1776556291|S2:2210916518|FV:|PF:0|UI:104995650|DT:0|PSRC:FROM=(0)|radio_src:0|NOWPLAY:songlib|SCRN:1366*768|ENPI:000|LSRC:|ISVIP:1|VIPTY:1|VIPLV:-1|DLY:0|MTREE:0|GS:2|FSB:0|TMM:0|TMS:0|MULTI:0||BLKTM:0|BLKCNT:0|BR:0|FMT:ape|ENDTYPE:1|CT:|CACHE:1|CACHEDSZ:25522718|CTYPE:song1|PT:54488|DUR:237|SPEED:0|FSIZE:25522718|DELAY:313|FDMT:31|FDMP:100|FSPT:203|BLKPOS:0|STARTSIZE:1531363|AACRESULT:0|CHANNEL_NAME:10001_01|PROD:MUSIC|VER:8.4.0.0_PQ|PLAT:WIN32|FROM:KwMusic8.5.0.0_BCS1.exe|UI:|{KwMusic8.5.0.0_BCS1.exe}|K:3947296|RESEND:0|U:27067152|DEP:1>'
    #strTest = r'[7872000][act][10-11 11:13:54.367][KNF]: 2%09<SRC:MUSIC_8.5.0.0_BDS4|ACT:PLAY_MUSIC|S:KwMV|U:7872000|N:|T:0|NA:告白气球|AR:周杰伦|AL:周杰伦的床边故事|F:HQ|B:0|D:0|RID:MUSIC_7149583|S1:2795477102|S2:206663274|FV:|PF:0|UI:|DT:0|PSRC:VER=2015;FROM=曲库->"周杰伦  "的搜索结果->结果列表(17085)|radio_src:0|NOWPLAY:search|SCRN:1920*1080|ENPI:000|LSRC:|ISVIP:0|VIPTY:-1|VIPLV:-1|DLY:1|MTREE:0|GS:0|FSB:0|TMM:0|TMS:0|MULTI:0|UUID:95DCBC384A3A410882F5925E8580CACBp+yNDnsKcDizzaFptbXy+uaO6OgVnn88MZI=|UMAC:D4BED9DE24AE|BLKTM:0|BLKCNT:0|BR:0|FMT:wma|ENDTYPE:1|CT:|CACHE:1|CACHEDSZ:3471055|CTYPE:song1|PT:1029|DUR:215|SPEED:0|FSIZE:3471055|DELAY:312|FDMT:16|FDMP:100|FSPT:47|BLKPOS:0|STARTSIZE:208263|AACRESULT:0|GreenVer:0|CHANNEL_NAME:|PROD:MUSIC|VER:|PLAT:WIN32|FROM:KwMusic8.5.0.0_BCS1111.exe|UI:|{KwMusic8.5.0.0_BCS1111.exe}|K:53456655|RESEND:0|U:7872000>'
    strTest = r'00:00| [INFO]: <SRC:MUSIC_8.5.2.0_BDS8|ACT:PLAY_MUSIC|S:KwMV|U:53108072|N:|T:0|NA:梦想如初|AR:雨木|AL:梦想如初|F:HQ|B:0|D:0|RID:MUSIC_6110241|S1:382800264|S2:650752489|FV:|PF:0|UI:|DT:0|PSRC:VER=2015;FROM=曲库->"梦想如初"的搜索结果->结果列表(17036)|radio_src:0|NOWPLAY:search|SCRN:1280*960|ENPI:000|LSRC:|ISVIP:0|VIPTY:-1|VIPLV:-1|DLY:1|MTREE:0|GS:0|FSB:0|TMM:0|TMS:0|MULTI:0|RUUIDOPEN:0|UUID:{5EFF8662-DCC1-5B78-E07C-C25A22643514}|UUMAC:EA42E474FED2|TIMESTAMP:2016-10-30 18:14:27.123|BLKTM:0|BLKCNT:0|BR:0|FMT:wma|ENDTYPE:0|CT:|CACHE:0|CACHEDSZ:5706079|CTYPE:song0|PT:352954|DUR:353|SPEED:51977|FSIZE:5706079|DELAY:199|FDMT:1029|FDMP:0|FSPT:9048|BLKPOS:0|STARTSIZE:248422|AACRESULT:0|GreenVer:0|CHANNEL_NAME:kwmusic2016_web_1_BDS_20161028|PROD:MUSIC|VER:8.5.0.0_BDS8|PLAT:WIN32|FROM:kwmusic2016_web_1_BDS_20161028.exe|UI:|{kwmusic2016_web_1_BDS_20161028.exe}|K:967344541|RESEND:0|U:53108072>=(106.0.5.172)TM:1478087998'
    mr_obj.LocalTest(strTest)

#pass
