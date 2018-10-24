#!/usr/bin/env python
#coding=utf8

import sys
import os
import re
sys.path.append('/data/client/code/py/')

import common_util
sys.path.append('MR')
'''
import MR_REGDLL
import MR_RECOM_START
import MR_RECOM_SHOW
import MR_RECOM_RUN
import MR_COMMON_START
import MR_DISP_START
import MR_CL_START
import MR_INSTALL_REG_TOOLS
import MR_INSTALL
#import MR_ERROR_LOG
import MR_DataRepairDES
import MR_AppStart
import MR_KSLIVE
import MR_DISP_KSLIVE
import MR_CRASHREPORT
import MR_DRTASKMGR
import MR_PLAY_MUSIC
import MR_APP_TREASURE
import MR_AB_LOG
import MR_INSTALL_INFO
import MR_UNINSTALL
import MR_USR_CLK
import MR_USR_CLK_VISUALDBLCLK
import MR_USR_CLK_VISUALCFGENABLED
import MR_RECOM_QUIT
import MR_RECOM_HIT_DETAILS
import MR_RECOM_HIT_RESULT
import MR_RECOM_NOTHING_TO_SHOW
import MR_RECOM_NO_KEY_REQ
import MR_ACT_INSTALL_FX
#import MR_DOWN_AD
import MR_COMMON_START_1002
import MR_COMMON_START_1003
import MR_COMMON_START_1006
import MR_COMMON_START_1007
import MR_COMMON_START_1008
import MR_COMMON_START_DISP
import MR_COMMON_START_RECOM
import MR_COMMON_START_SHELL
import MR_ACT_RECOMLOADER
import MR_1003_QUIT
import MR_DISP_UPGRADE
import MR_RECOM_CLICK
import MR_USR_CLK_WASAPI_STATE
import MR_LOCAL_TMP
import MR_DOWN_MUSIC
import MR_FEATURE_LOG
import MR_COMMON_START_1009
import MR_SW_DETECT_SW
import MR_DISP_USB_DEVICE_FIND
import MR_DISP_GREEN_START

import MR_1007_DGMUSIC
import MR_1007_LOADER
import MR_1007_PREINST_GMUSIC
import MR_NSIS_UNINST
import MR_FIRST_PLAY
import MR_DR_P2PSETTING
import MR_UUIDGEN
import MR_ANDROID_CONNECT
import MR_WPS_LAUNCH
import MR_1007_CHECK_INST_GMUSIC
#import MR_APP_START
'''
g_Handlers = {}
#import importlib

def from_this_dir(filename):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

def InitHandlers():
	if len(g_Handlers) == 0:
		if sys.platform != "win32":
			files = os.listdir(os.path.dirname(os.path.abspath(__file__)));
		else:
			files = os.listdir("MR");

		for f in files:
			if f.find("MR") == 0 and f.rfind(".py") == len(f) - 3:
				f = f[0:len(f) - 3];
				__import__(f);
				if f != "MR_BASE":
					mod = sys.modules[f];
					obj = getattr(mod, "mr_obj")
					insertHandler(obj);

	'''
	insertHandler(MR_RECOM_START.mr_obj)
	insertHandler(MR_RECOM_SHOW.mr_obj)
	insertHandler(MR_RECOM_RUN.mr_obj)
	insertHandler(MR_COMMON_START.mr_obj)
	insertHandler(MR_DISP_START.mr_obj)
	insertHandler(MR_INSTALL_REG_TOOLS.mr_obj)
	insertHandler(MR_INSTALL.mr_obj)
	insertHandler(MR_DataRepairDES.mr_obj)
	insertHandler(MR_AppStart.mr_obj)
	#insertHandler(MR_ERROR_LOG.mr_obj)
	insertHandler(MR_KSLIVE.mr_obj)
	insertHandler(MR_DISP_KSLIVE.mr_obj)
	insertHandler(MR_CRASHREPORT.mr_obj)
	insertHandler(MR_DRTASKMGR.mr_obj)
	insertHandler(MR_PLAY_MUSIC.mr_obj)
	insertHandler(MR_REGDLL.mr_obj)
	insertHandler(MR_CL_START.mr_obj)
	insertHandler(MR_APP_TREASURE.mr_obj)
	insertHandler(MR_INSTALL.mr_obj)
	insertHandler(MR_AB_LOG.mr_obj)
	insertHandler(MR_INSTALL_INFO.mr_obj)
	insertHandler(MR_UNINSTALL.mr_obj)
	insertHandler(MR_USR_CLK.mr_obj)
	insertHandler(MR_USR_CLK_VISUALDBLCLK.mr_obj)
	#insertHandler(MR_DOWN_AD.mr_obj)
	#insertHandler(MR_PLAY_MUSIC.mr_obj)
	insertHandler(MR_USR_CLK_VISUALCFGENABLED.mr_obj)
	insertHandler(MR_RECOM_QUIT.mr_obj)
	insertHandler(MR_RECOM_HIT_DETAILS.mr_obj)
	insertHandler(MR_RECOM_HIT_RESULT.mr_obj)
	insertHandler(MR_RECOM_NOTHING_TO_SHOW.mr_obj)
	insertHandler(MR_ACT_INSTALL_FX.mr_obj)

	insertHandler(MR_RECOM_NO_KEY_REQ.mr_obj)
	insertHandler(MR_COMMON_START_1002.mr_obj)
	insertHandler(MR_COMMON_START_1003.mr_obj)
	insertHandler(MR_COMMON_START_1006.mr_obj)
	insertHandler(MR_COMMON_START_1007.mr_obj)
	insertHandler(MR_COMMON_START_1008.mr_obj)
	insertHandler(MR_COMMON_START_DISP.mr_obj)
	insertHandler(MR_COMMON_START_RECOM.mr_obj)
	insertHandler(MR_COMMON_START_SHELL.mr_obj)
	insertHandler(MR_ACT_RECOMLOADER.mr_obj)
	insertHandler(MR_1003_QUIT.mr_obj)
	insertHandler(MR_DISP_UPGRADE.mr_obj)
	insertHandler(MR_RECOM_CLICK.mr_obj)
	insertHandler(MR_USR_CLK_WASAPI_STATE.mr_obj)
	insertHandler(MR_LOCAL_TMP.mr_obj)
	insertHandler(MR_DOWN_MUSIC.mr_obj)
	insertHandler(MR_FEATURE_LOG.mr_obj)
	insertHandler(MR_COMMON_START_1009.mr_obj)
	insertHandler(MR_SW_DETECT_SW.mr_obj)
	insertHandler(MR_DISP_USB_DEVICE_FIND.mr_obj)
	insertHandler(MR_DISP_GREEN_START.mr_obj)

	insertHandler(MR_1007_DGMUSIC.mr_obj)
	insertHandler(MR_1007_LOADER.mr_obj)
	insertHandler(MR_1007_PREINST_GMUSIC.mr_obj)
	insertHandler(MR_NSIS_UNINST.mr_obj)
	insertHandler(MR_FIRST_PLAY.mr_obj)
	insertHandler(MR_DR_P2PSETTING.mr_obj)
	insertHandler(MR_UUIDGEN.mr_obj)
	insertHandler(MR_ANDROID_CONNECT.mr_obj)
	insertHandler(MR_WPS_LAUNCH.mr_obj)
	insertHandler(MR_1007_CHECK_INST_GMUSIC.mr_obj)
	#insertHandler(MR_DISP_START_TASK.mr_obj)
	#insertHandler(MR_APP_START.mr_obj)
	'''
def insertHandler(mr_base):#strAct, funcMapper, funcRInit,funcReducer=common_util.ProcessReducer):
	if not mr_base.act_type in g_Handlers:
		#item = {'act':strAct, 'f_maper':funcMapper, 'f_redu': funcReducer, 'f_rinit':funcRInit}
		g_Handlers[mr_base.act_type] = mr_base


class Dispatcher(object):
	def __init__(self):
		InitHandlers()

	def MapperDispatch(self,act,value):
		res = re.search("(INSTALL|UNINSTALL){.*}",act,re.IGNORECASE)
		if res is not None:
			act = res.group(1)
		if act in g_Handlers:
			#item = g_Handlers[act]
			#item['f_maper'](value)
			g_Handlers[act].ProcessMapper(value)

	def ReducerInit(self,act):
		if act in g_Handlers:
			#item = g_Handlers[act]
			#item['f_rinit'](act)
			g_Handlers[act].InitReducer(act)

	def ReducerDispatch(self,act,value):
		if act in g_Handlers:
			#item = g_Handlers[act]
			#item['f_redu'](value)
			g_Handlers[act].ProcessReducer(value)
'''
def test():
    InitHandlers()
    MapperDispatch("REGDLL","test")
    ReducerDispatch("COMMONSTART","test")

if __name__ == '__main__':
	#test()
	#pro = "F:\\hadoop_py\\REGDLL.py"
	#from REGDLL import RegToolsProcess
	
	#lz.__get               attr__("RegToolsProcess");
	#print lz
	#print lz.name
	#imp.load_module("RegToolsProcess", pro, "REGDLL.py")
	#aMod = sys.modules[pro]
	#t1 = getattr(aMod,RegToolsProcess)
	#_import(RegToolsProcess)

    disp = Dispatcher()
    disp.MapperDispatch("REGDLL1","test")
    disp.ReducerDispatch("COMMONSTART","test")
    print 'end'

DLL.ProcessMapper("test")
    REGDLL.ProcessReducer("test")
    COMMONSTART.ProcessMapper("test")
    COMMONSTART.ProcessReducer("test")
    print t1.name
    t1.mapperProcess()
    t1.reducerProcess()
'''
