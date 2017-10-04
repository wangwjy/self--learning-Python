#文件压缩
import zipfile
f=zipfile.ZipFile('1.zip','w',zipfile.ZIP_DEFLATED)
f.write('2.txt')
f.close()