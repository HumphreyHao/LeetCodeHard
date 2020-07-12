# RocketMQ

- 看你用过RocketMQ,介绍一下吧

主要分为生产者,消费者,主题,消息,消息队列,标记,broker经纪人,名称服务器,offset.

生产者: 将消息发送到brokers中.RMQ提供了同步,异步,单向,三种消息发送模式.
生产组: 生产者的一个集合,原始生产者崩溃,另一个生产者替代
    如何选择消息队列?
    首先，要澄清一个误会。这里的选择消息队列发送消息，并不是真的往某个队列发送消息。RocketMQ的消息只存在一个叫CommitLog的逻辑文件中，对应于磁盘上的多个文件。消息队列的概念，仅仅是消息消费的时候才会用到。因为所有消息都是存放在一个CommitLog中的，这意味着不同的Topic的消息是先来后到的顺序插入到CommitLog中。如果Consumer要消费某个Topic下的消息，去CommitLog里面去一个个查询势必非常缓慢，是完全不可取的。为了解决某Topic下消息查询的问题（当然不仅仅是解决这一个问题，还包括消费进度等），RocketMQ在原有的CommitLog的基础之上，为每一个Topic新建了一个ConsumerQueue的文件（同样对应于磁盘上的多个文件，也就是我们口中的消息队列），它保存了某个topic下的消息在CommitLog里偏移位置。这样消费某个Topic的消息，就可以直接读取该ConsumerQueue文件，拿到消息在CommitLog中的偏移位置，然后去CommitLog里面寻找消息实体即可。

消费者: 从brokers中拉取消息,并且将消息传递给业务系统.
有两种消费者:

    拉取DefaultMQPullConsumer: 主动从brokers拉取消息.读取中的大部分功能由使用者自主控制.

    推送DefaultMQPushConsumer: 系统控制读取操作,收到消息后自动调用传入的处理方法.需要传入三个参数,一是这个Consumer的GroupName，二是NameServer的地址和端口号，三是Topic的名称+要的tag。

同时有两种消费模式:

    Clustering(集群模式):在集群消费模式下，每条消息只需要投递到订阅这个topic的Consumer Group下的一个实例即可。RocketMQ采用主动拉取的方式拉取并消费消息，在拉取的时候需要明确指定拉取哪一条message queue。所以算法上都是一个queue只分给一个consumer实例，一个consumer实例可以允许同时分到不同的queue。但是如果consumer实例的数量比message queue的总数量还多的话，多出来的consumer实例将无法分到queue，也就无法消费到消息，也就无法起到分摊负载的作用了。所以需要控制让queue的总数量大于等于consumer的数量。

    Broadcasting广播模式:同一个ConsumerGroup里的每个Consumer都能消费到所订阅Topic的全部消息，也就是一个消息会被多次分发，被多个Consumer消费。在实现上，其中一个不同就是在consumer分配queue的时候，会所有consumer都分到所有的queue。

消息类型:

    无序消息:生成和消费消息是顺序未知
    有序消息: 取决于topic到底有几个queue
        全局有序: 只设定一个queue,但是慢
        局部有序: 多个queue,按照orderid进行消息投递和消费.
    延时消息: 在msg中设定延时即可

Topic: 是消息的逻辑分类,如下图可以展示topic,broker,queue三者之间的关系

![](https://upload-images.jianshu.io/upload_images/6302559-5693e4bec15216b5.png?imageMogr2/auto-orient/strip|imageView2/2/w/837/format/webp)
实际上保存的消息不是真正的消息数据,而是指向commit log的消息索引.
Topic创建的时候可以用集群模式去创建（这样集群里面每个broker的queue的数量相同），也可以用单个broker模式去创建（这样每个broker的queue数量可以不一致）。
使用命令行创建topic, mqadmin通知broker创建topic和对应的queue信息,broker转发通知namesrv保存topic和broker的原信息，同时在本地持久化一份topic配置。
不同的topic，message queue都是写到相同的CommitLog 文件，也就是说CommitLog完全的顺序写

offset:RocketMQ在存储消息时会为每个Topic下的每个Queue生成一个消息的索引文件，每个Queue都对应一个Offset记录当前Queue中消息条数。

broker:真正存储消息的地方,有很多个queue.
每个Broker与Name Server集群中的所有节点建立长连接，定时注册Topic信息到所有Name Server。
由于消息分布在各个Broker上，一旦某个Broker宕机，则该Broker上的消息读写都会受到影响。
所以RocketMQ提供了Master/Slave的结构，Salve定时从Master同步数据，如果Master宕机，则Slave提供消费服务，但是不能写入消息，此过程对应用透明，由RocketMQ内部解决。
消费者得到Master宕机通知后，转向Slave消费，但是Slave不能保证Master的消息100%都同步过来了，因此会有少量的消息丢失。但是消息最终不会丢的，一旦Master恢复，未同步过去的消息会被消费掉。

- 都有哪些组件?

主要分为生产者,消费者,主题,消息,消息队列,标记,broker经纪人,名称服务器,offset.

- 有哪几种消费者?
拉取,推送.

- 是怎么消费的?
拉取,推送,取决于自己的设定.

- 和Kafka最大的区别是什么?
存储形式: Kafka采用partition，每个topic的每个partition对应一个文件。顺序写入，定时刷盘。但一旦单个broker的partition过多，则顺序写将退化为随机写，Page Cache脏页过多，频繁触发缺页中断，性能大幅下降; RocketMQ采用CommitLog+ConsumeQueue，单个broker所有topic在CommitLog中顺序写，Page Cache只需保持最新的页面即可。同时每个topic下的每个queue都有一个对应的ConsumeQueue文件作为索引。ConsumeQueue占用Page Cache极少，刷盘影响较小。

```
介绍一下Kafka的刷盘策略
首先我们先来了解一下kafka日志的结构：每个topic的partition对应一个broker上一个目录，目录中的文件以日志的大小（log.segment.bytes）和时间（log.roll.hours）来roll。我们看到的kafka v0.10.2的日志文件包括三个部分，分别是xxxxxxxxxxxxxxxxxxxx.index、xxxxxxxxxxxxxxxxxxxx.log和xxxxxxxxxxxxxxxxxxxx.timeindex，其中xxxxxxxxxxxxxxxxxxxx代表的是offset，20位，从0开始。Kafka没有采用uuid的形式，为每个message分配一个message.id，而是通过offset来标记message，offset并不是消息在文件中的物理编号，而是一个逻辑编号，通过追加方式，每次加1。那通过offset如何查找消息的呢？
```

刷盘策略: 
同步刷盘是在每条消息都确认落盘了之后才向发送者返回响应；而异步刷盘中，只要消息保存到Broker的内存就向发送者返回响应，Broker会有专门的线程对内存中的消息进行批量存储。所以异步刷盘的策略下，当机器突然掉电时，Broker内存中的消息因无法刷到磁盘导致丢失;RMQ支持同步和异步刷盘,但是KAFKA只支持异步.
其次是支持的队列数: Kafka单机超过64个队列/分区，消息发送性能降低严重；RocketMQ 单机支持最高5万个队列，性能稳定
消息顺序性: Kafka 某些配置下，支持消息顺序，但是一台Broker宕机后，就会产生消息乱序；RocketMQ支持严格的消息顺序，在顺序消息场景下，一台Broker宕机后，发送消息会失败，但是不会乱序；
消息查询机制: Kafka不支持消息查询,RocketMQ支持根据Message Id查询消息，也支持根据消息内容查询消息.
具体的原理是什么?

- 如何刷盘/存磁盘的?
异步刷盘: Broker的一种持久化策略，消息写入pagecache后，直接返回。由异步线程负责将pagecache写入硬盘。
同步刷盘:Broker的一种持久化策略，消息写入pagecache后，由同步线程将pagecache写入硬盘后，再返回。

- 是用在哪和哪之间通讯?
用于发送订单和处理订单,用于数据库和redis之间
