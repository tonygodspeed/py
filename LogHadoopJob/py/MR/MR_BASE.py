#!/usr/bin/env python
#coding=utf8

import sys
sys.path.append('..')
import os
import re
import common_def
import common_util
import check_valid
import copy

reload(sys)
sys.setdefaultencoding("utf-8")

vec_check_valid = [
    "AppStart",
    "FIRST_PLAY",
    "UUIDGEN",
    "PLAY_MUSIC"
]

class mr_base_ex:
    def __init__(self,str_act):
        self.res_data = {};
        self.res_spec_mid = [];
        self.res_spec_str = "";
        self.act_type = str_act;
        if self.act_type in vec_check_valid:
            self.res_name_ap = ["checked"];
        else:
            self.res_name_ap = [];

    def InitReducerCommon(self):
        strKeysNameFeild = ""
        strKeysTypeFeild = ""
        for item in self.res_name:
            if item == "from":
                item = "org"
            if item == "GROUP":
                item = "GP"
            strKeysNameFeild = strKeysNameFeild + item + "\t"

        for item in self.res_name_ap:
            strKeysNameFeild = strKeysNameFeild + item + "\t"

        for item in self.res_type:
            strKeysTypeFeild = strKeysTypeFeild + item + "\t"

        print(strKeysNameFeild)
        print(strKeysTypeFeild)

    def InitReducer(self,value):
        print("========================"+value+"===================")
        self.InitReducerCommon()

    def MapperDataCb(self):
        if len(self.res_name_ap) == 1:
            bret = "-1"
            if self.res_data['UUID'] != "-1":
                bret = check_valid.check_valid(self.res_data['SRC'],self.res_data['UUID'],self.res_data['UMAC']);#"E807E5486ECE462F83775690B4C078AD2jfUfl/+dx+yT2WnhPVAnOr7u16TnBg8","D8CB8A68A2AC");

            self.res_data['checked'] = bret;
        return True;

    def ProcessMapper(self,value):
        try:
            if len(value) > 0:
                matched = True;
                if (self.res_spec_str is not None):
                    if (re.search(self.res_spec_str,value,re.IGNORECASE) is None):
                        matched = False;

                if matched:
                    pos = value.rfind('>');
                    if pos != -1 and value.find('<') != -1:
                        value = value[0:pos];
                    pos = value.find('SRC');
                    if pos != -1:
                        value = value[pos:];

                    words = value.split("|")
                    r = copy.deepcopy(self.res_name);
                    if len(self.res_spec_mid) > 0:
                        for item in self.res_spec_mid:
                            r.append(item);

                    for word in words:
                        if word.find(":") == -1:
                            continue

                        k,v = word.split(":",1)
                        if len(v) > 0:
                            for key in r:
                                if re.match(key,k, re.IGNORECASE):#.find(key) != -1:
                                    self.res_data[key] = v
                                    r.remove(key)
                                    break
                        if len(r) == 0:
                            break

                    for l in r:
                        self.res_data[l] = "-1"

                    if self.MapperDataCb():
                        line = "";
                        for item in self.res_name:
                            line = line + self.res_data[item] + "\t"

                        for item in self.res_name_ap:
                            line = line + self.res_data[item] + "\t"

                        if line is not None:
                            print(self.act_type + "\t" + line)
                    pass
        except BaseException,e:
            return

    def ProcessReducer(self,value):
        try:
            key, value = value.split('\t', 1)
            if len(value) > 0:
                print(value)
        except ValueError:
            return

    def LocalTest(self,test_str):
        try:
            print("-----------------------test begin-----------------------")
            #self.InitMapper(test_str)
            #mt = re.match(self.mt_string, test_str)
            #dicRet = common_util.X_ParserLine(test_str,self.mt_string,self.mt_type)
            self.ProcessMapper(test_str)
            self.InitReducer('test')
            print("-----------------------test end-----------------------")
        except BaseException,e:
            print e.message
        pass


class mr_base:
    def __init__(self,mt_type,act_type):
        self.mt_type = mt_type
        self.mt_string = ""
        self.act_type = act_type

    def InitReducer(self,value):
        try:
            common_util.X_InitReducer(value,self.mt_type)
        except BaseException,e:
            return

    def InitMapper(self,value):
        try:
            if len(self.mt_string) > 0:
                return
            self.mt_string = common_util.X_UpdateMatchString(self.mt_type)
        except BaseException,e:
            return

    def MapperDataCb(self,data):
        return ""

    def ProcessMapper(self,value):
        try:
            self.InitMapper(value)
            line = value.strip()
            strMapperText = ""
            #if mapper_type is not None:
            strMapperText = common_util.X_GetMapperTextEx(self.act_type,line,self.mt_string,self.mt_type)
            #else:
            #    strMapperText = common_util.X_GetMapperText(self.act_type,line,self.mt_string,self.mt_type)
            if strMapperText != None:
                strMapperText += self.MapperDataCb(line)
                if strMapperText == "0":
                    print('err')
                print(strMapperText)
            return
        except BaseException,e:
            return

    def ProcessReducer(self,value):
        try:
            key, value = value.split('\t', 1)
            if len(value) > 0:
                print(value)
        except ValueError:
            return

    def LocalTest(self,test_str):
        try:
            print("-----------------------test begin-----------------------")
            self.InitMapper(test_str)
            mt = re.match(self.mt_string, test_str)
            dicRet = common_util.X_ParserLine(test_str,self.mt_string,self.mt_type)
            self.ProcessMapper(test_str)
            self.InitReducer('test')
            print("-----------------------test end-----------------------")
        except BaseException,e:
            print e.message
        pass