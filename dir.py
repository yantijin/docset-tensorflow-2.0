import os
root ='./out'
mat_name = [os.path.join(path, file_name) 
			for path, _, file_list in os.walk(root) 
			for file_name in file_list if file_name.endswith('.html')]
print(mat_name)
k=1
print(r'\\')
html1 = '''
<html lang="zh-cn">
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<link href="
''' 
html2 ='''
default.css" rel="stylesheet">
<link href="
''' 
html3 = '''
github.css" rel="stylesheet">
</head>
<body>
%s
</body>
</html>
'''
print(html1[:-1]+'../'*k+html2[1:-1]+'../'*k+html3[1:-1])