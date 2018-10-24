#!/usr/bin/env python
#coding=utf8
import sys
import os
import re

OnlyMapper = True;
def ProcessReducer(value):
    try:
        key, value = value.split('\t', 1)
        if len(value) > 0:
            print(value)
    except ValueError:
        return

def X_InitReducer(value, keysInfo):
    print("========================"+value+"===================")
    
    strKeysNameFeild = ""
    strKeysTypeFeild = ""
    for item in keysInfo:
        if item["key"] != 'NONE':
            strKeysNameFeild = strKeysNameFeild + item["key"] + "\t"
            strKeysTypeFeild = strKeysTypeFeild + item["type"] + "\t"

    print(strKeysNameFeild)
    print(strKeysTypeFeild)

def X_UpdateMatchString(lstKeyInfos):
    strRet = ''
    for dec in lstKeyInfos:
        strRet = strRet  + dec['mt']

    return strRet

def X_ParserLine(strLine, strMatchString, lstKeysInfos):
    dicRet = {}
    mt = re.match(strMatchString, strLine,re.IGNORECASE)
    if mt:
        nIndex = 1
        for keyInfo in lstKeysInfos:
            keyName=keyInfo['key']
            if keyName != 'NONE':
                value = mt.group(nIndex)
                value = value.strip()
                if len(value) == 0:
                    value = -1
                dicRet[keyName] = value #mt.group(nIndex)
                nIndex = nIndex + 1

    return dicRet

def X_GetMapperText(actType, line, matchString, keysInfo):
    dicRet = X_ParserLine(line, matchString, keysInfo)
    if len(dicRet) <= 0:
        return ''

    strMapText = actType + '\t' 
    for keyInfo in keysInfo:
        keyName = keyInfo['key']
        if keyName != 'NONE':
            strMapText = strMapText + dicRet[keyName] + '\t'

    return strMapText

def X_GetMapperTextEx(actType, line, matchString, keysInfo):
    dicRet = X_ParserLine(line, matchString, keysInfo)
    if len(dicRet) <= 0:
        return ''

    strMapText = '';
    if OnlyMapper is not True:
       strMapText = actType + '\t'
    for keyInfo in keysInfo:
        keyName = keyInfo['key']
        if keyName != 'NONE':
            if 'cb_kv' in keyInfo:
                temp = keyInfo['cb_kv'](keyName,dicRet[keyName])
                if temp == -1:
                    strMapText = None
                    break
            else:
                temp = dicRet[keyName]
            strMapText += str(temp) + '\t'

    return strMapText

'''
if __name__ == '__main__':
    ProcessReducer("test\tt")
'''
