# 整理50个hadoop相关的面试题
    https://blog.csdn.net/WYpersist/article/details/80262066

## 列出Hadoop集群的Hadoop守护进程和相关的角色。
Namenode：它运行上Master节点上，负责存储的文件和目录所有元数据。它管理文件的块信息，以及块在集群中分布的信息。
Datanode：它是一个存储实际数据的Slave节点。它定时向Namenode发送本节点上块的信息。
Secondary Namenode：它会定期通过Editlog合并NameNode的变化，从而它r的日志不会过大。它可以在NameNode的故障的情况下做为副本使用。
JobTracker：这是运行在Namenode上，负责提交和跟踪MapReduce Job的守护程序。它会向Tasktracker分配的任务。
TaskTracker：这是Datanode上运行的守护进程。它在Slave节点上负责具体任务的运行。
ResourceManager的（Hadoop的2.X）：它负责YARN上运行的资源和调度。

NodeManager（Hadoop的2.X）：它可以运行在Slave节点，并负责启动应用程序的容器，监测他们的资源使用情况（CPU，内存，磁盘，网络），并报告这些到ResourceManager。

JobHistoryServer（Hadoop的2.X）：它维护有关的MapReduce工作中的应用终止后的信息。

## 什么是主动和被动的namenodes
在Hadoop的2.x中，我们有两个Namenodes-主动“Namenode” 被动“Namenode”。主动“Namenode”是在集群中运行的Namenode。被动“的Namenode”是一个备用“的Namenode”，里面有主动“的Namenode”的数据。当主动“Namenode”失败，则被动“Namenode”集群中替换主动“Namenode”。因此，集群是从来不会没有“Namenode”，所以它永远不会失败。

## 怎样才能删除或Hadoop集群添加节点？
修改所有机器的hosts文件和/home/hadoop/hadoop/conf下slaves文件，切换到hosts文件在文件的后面添加新节点的ip和机器名：192.168.56.204 slaves，再切换到hadoop用户，在slaves文件后面添加slave4

## 当两个客户端尝试访问对HDFS相同的文件，会发生什么？
HDFS只支持独占写入。

当第一个客户端连接“Namenode”打开文件进行写入时，“Namenode”授予租约的客户端创建这个文件。当第二个客户端试图打开同一个文件写入时，“Namenode”会注意到该文件的租约已经授予给另一个客户端，并拒绝第二个客户端打开请求.

## 为什么我们有时会得到一个“文件只能被复制到0节点，而不是1”的错误？
这是因为“的Namenode”没有任何可用的DataNodes。

## 如何在HDFS定义“block”？Hadoop1和2中Hadoop块大小是多少？是否可以改变？
“块”是可被读取或写入的数据的最小量。 HDFS中的文件被分解成块大小的块，它们被存储作为独立的单元。
Hadoop的1默认块大小：64 MB
Hadoop的2默认块大小：128 MB
是，块可以被配置。该dfs.block.size参数可在HDFS-site.xml文件被用来设置一个块的大小。

## 你如何在Hadoop中定义“rack awareness”？
它是在“Namenode”上确定块放置方式，以尽量减少在同一机架内“DataNodes”之间的网络流量的方式。比方说，我们考虑复制因子3（默认），该策略是“数据的每个块，两个副本将在一个机架中，第三个副本存在于不同的机架”。这条规则被称为“副本放置策略”。

## 为什么Hadoop适用于大型数据集的应用程序，而不是具有大量的小文件的应用程序？
相较于在多个分布数据量小的文件 ，HDFS更适合在一个文件中具有大量的数据集。这是因为“Namenode”是非常昂贵的，高性能的系统中，它是不慎重的占据“Namenode”通过了为多个小文件生成的元数据的不必要量的空间。因此，当在一个单独文件中的大量的数据，“Namenode”将占据更少的空间。因此，为获得最佳的性能，HDFS支持大数据集，而不是多个小文件。

## 什么是传统的关系型数据库和Hadoop之间的基本区别？
传统的RDBMS是用于交易系统报告和存档数据，而Hadoop是存储和处理的分布式文件系统的海量数据的方法。当你想寻求大数据的一个记录RDBMS将是有益的。因此，当你在一次存储很大的文件并随后进行分析，Hadoop将是有益的。

## 解释HDFS索引过程
Hadoop的有它自己的索引数据的方式。取决于块大小，HDFS将继续存储数据的最后部分。它还会告诉你数据的下一部分的位置。

## 什么是“speculative running”在Hadoop中
如果一个节点出现运行一个任务较慢，主节点可以冗余另一个节点上执行同一任务的另一实例。这里，它第一个完成任务的将被接受，而另一个被杀死。这个过程被称为“speculative running”。

## 为什么在HDFS，“读”是并行的，但“写”不是？
使用的MapReduce程序，该文件可以通过分割成块被读取。不过，写入时MapReduce并行 不能适用。

## 如果您在尝试访问HDFS或者其相应的文件得到一个“连接被拒绝Java异常'的错误会发生什么？
这可能意味着“Namenode”不工作了。“Namenode”可能是在“安全模式”或“Namenode”的IP地址可能改变了。

## “zookeeper”在Hadoop集群中的作用？
“zookeeper”的目的是集群管理。 “zookeeper”将帮助你实现的Hadoop节点之间的协调。 也有助于：
管理跨节点配置
实现可靠的消息传递
实现冗余服务
同步流程执行

# MapReduce相关

## 什么是“MapReduce的”？
它是一个框架或用于通过使用分布式编程的计算机的集群处理大型数据集的编程模型。

## 什么是运行“MapReduce的”程序的语法？
Hadoop jar file.jar / input_path / output_path

## 为什么我们不能在一个映射器进行“聚合”（加法）的原因是什么？我们为什么需要这个了“reduce”？
因为排序不在“mapper”中发生。排序仅在reducer侧发生。在“mapper”的方法初始化取决于每个输入。在“聚合”时，我们将失去以前的实例的值。对于每一行，一个新的“mapper”将得到初始化。对于每一行，input split再次被分为“mapper”。因此，我们不能跟踪前一行的值。

## Hadoop中“RecordReader”的目的是什么？
在“InputSplit”定义工作片，但并没有描述如何访问它。的“RecordReader”级从其源加载数据，并将其转换成适合于“mapper”读的（键，值）对。“RecordReader”实例是由“输入格式”中定义。

## 什么是一个“MapReduce的分区”？
“MapReduce的分区”可以确保同一个key的所有值去到同一个“reducer”，从而允许“reducer”对应的map输出的平均分布。它通过确定哪个“reducer”是负责该特定键从而把map输出重定向给reducer。

# Hive相关
## “hive”存储表中的数据的默认位置是？
HDFS：//NameNode/用户/hive/warehouse

## 解释在Hadoop中“Sqoop”。
“Sqoop”是用于一个RDBMS并在Hadoop HDFS之间传送数据的一种工具。使用“Sqoop”，数据可以从一个RDBMS（如MySQL或Oracle）插入HDFS以及从HDFS文件RDBMS出口数据传输。