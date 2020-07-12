# linux服务器部分

## 怎么查看日志?如果只想看日志的最底端,用什么命令?如果想在日志里检索关键词,用什么命令?
使用tail -f test.log,查看最底端正在改变的文件.

head是查看前多少行日志.

cat是查看关键字的日志.

cat -n test.log |grep "debug"得到关键字行号
grep是查看关键字

tac和cat是相反的,cat可以显示整个文件.
cat可以合并文件.cat file1 file2 > file

cat -n test.log |grep "debug" |more     分页打印,空格翻页
cat -n test.log |grep "debug"  >debug.txt 拉下来查询

## 如何查看cpu使用情况?如果查看硬盘使用情况?
top命令查看cpu使用情况
df -h查看硬盘使用情况