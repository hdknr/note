- [rsyncオプション](http://qiita.com/bezeklik/items/22e791df7187958d76c1)


~~~bash 
time rsync -av --delete --exclude-from ${PATTERNFILE} -e "ssh -i /root/.ssh/id_rsync" ${SOURCEDIR} ${DESTDIR} 2>&1 | tee -a ${LOGFILE}
~~~
