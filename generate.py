import os
import sys
import stat
import re

def generate(filepath):
	if not os.path.exists(filepath):
		print >>sys.stderr,'Target path not exists'
		return
	fstat = os.stat(filepath)
	if stat.S_ISDIR(fstat[stat.ST_MODE]):
		print >>sys.stderr,'Target path is dir'
		return
	print 'Parsing',filepath,'...'

	tplfile = open(filepath,'r')
	lines = tplfile.readlines()
	tplfile.close()
	content = ''
	for line in lines:
		# FIXME should not trim in block (pre etc.)
		content += line.strip()
	content = content.replace('\r','')
	content = content.replace('\n','')
	content = content.replace("'","\\'")

	tplpattern = re.compile(ur'\$\{(.*?)\}')
	tpltags = tplpattern.findall(content)
	content = tplpattern.sub(ur"'+\1+'",content)
	content = "'" + content + "'"
	tpltags = set(tpltags)

	print '==================VAR LIST======================='
	for tag in tpltags:
		print tag
	print '==================TEMPLATE======================='
	print content



if __name__ == '__main__':
	generate(sys.argv[1])