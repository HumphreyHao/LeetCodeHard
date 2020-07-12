# JAVA基础

## Java中的泛型有哪些应用?为什么要使用泛型.
在没有使用泛型的情况下，如果要实现参数“任意化”，通常会定义成Object类型来接受，然后强制类型转换使用；而强制类型转换有明显的缺点，就是必须要知道实际参数的具体类型的情况才可以进行转换，同时在强制转换的过程中，编译器不会报错提示的，只有在运行阶段才会出现异常，一定程度上存在安全隐患。
主要是用于定义公共类,比如hashmap的源码中,集合类的源码中.泛型可以用到容器，方法，接口，内部类，抽象类

## Java中的反射有哪些应用?
生成各种代理类,动态代理,调用不同的连接器等等.
JDBC数据库的连接:加载数据库驱动程序,根据地址用户和密码连接,使用connection接口接收连接.
xml的配置加载bean就是根据字符串获取class实例,动态配置实例属性.

## 内存泄漏是怎么回事?
生命周期长引用了生命周期短的实例.

## final关键字
当用final修饰一个类时，表明这个类不能被继承
修饰一个函数,不能被重写.
对于一个final变量，如果是基本数据类型的变量，则其数值一旦在初始化之后便不能更改；
如果是引用类型的变量，则在对其初始化之后便不能再让其指向另一个对象。


## 设计模式了解哪些
https://www.jianshu.com/p/bdf65e4afbb0
简单工厂模式:根据不同的条件,返回不同的对象.
工厂模式:不同的工厂类实现同一个工厂接口,返回不同的产品.
抽象工厂模式:应对产品族,当一个产品族中的多个对象被设计成一起工作时，它能保证客户端始终只使用同一个产品族中的对象。
装饰者模式:动态的给某对象添加一些额外的功能
代理模式:封装被代理对象,并且限制外界对被代理对象的访问
模板方法模式:定义一个操作的算法骨架,并且将一些步骤延迟到子类中
外观模式:为系统向外界提供一个统一的接口
适配器模式:类似于三足插头,提供统一的接口标准,比如一个类可能有10个私有方法,但是对外只有3个接口方法.
桥接模式:把原本要耦合的上下层抽象出来,上层和下层使用组合的方式连接,这样一来就只需要set方法即可切换不同的子类,类似于切换桥的方向.
建造者模式:把builder单独抽象出来,可以使用lombok的builder方法.
观察者模式:定义了一种1对多的依赖关系,当Observable状态改变时通知所有Observer
单例模式:保证本类只有一个实例,并且提供一个访问他的全局控制点
命令模式:封装一系列命令,通过重写命令可以实现指定命令集的运行.

### 如何实现多线程安全的单例模式:

直接放一个代码
```
private static volatile SettingsDbHelper sInst = null;
public static SettingsDbHelper getInstance(Context context) {  
    SettingsDbHelper inst = sInst;  // <<< 在这里创建临时变量
    if (inst == null) {
        synchronized (SettingsDbHelper.class) {
            inst = sInst;
            if (inst == null) {
                inst = new SettingsDbHelper(context);
                sInst = inst;
            }
        }
    }
    return inst;  // <<< 注意这里返回的是临时变量
}
```
这样一来,除了第一次访问,其他的访问单例都只会访问一次sInst变量

再加一个延迟初始化的方式:
```
class Foo {  
    private static class HelperHolder {
       public static final Helper helper = new Helper();
    }

    public static Helper getHelper() {
        return HelperHolder.helper;
    }
}
```

这个方法也可以保证延迟初始化,并且多线程安全.

或者更加粗暴一些:
```
public enum Foo {  
    INSTANCE;
}
```

## 设计原则了解哪些
1,单一职责原则:每个类只执行一个功能
2,里氏替换原则:父类出现的地方替换为子类必须可以出现
3,依赖倒置原则:类不应该从具体类派生出来,实现类之间没有依赖关系
4,接口隔离原则:类尽量实现接口
5,迪米特法则:一个对象应该对其他对象有最少的了解
6,开闭原则:软件实体应该对扩展开放,对修改关闭.

## 谈谈垃圾回收
见另外一个博客:深入理解JAVA虚拟机

## 创建对象的方式
1,使用new关键字,调用任意的构造函数
2,使用反射
```
//创建方法1
User user = (User)Class.forName("根路径.User").newInstance();　
//创建方法2（用这个最好）
User user = User.class.newInstance();

Constructor<User> constructor = User.class.getConstructor();
User user = constructor.newInstance();
```

3,实现Cloneable接口并且实现定义的clone方法

4,使用反序列化读出一个对象

## 类初始化和加载的顺序
父类的静态变量>子类静态变量>父类的变量>子类变量

## 垃圾回收只回收堆中对象吗?
基本上是的,大部分对象都存在堆内存中

## 如何保证不同线程之间隔离,同一线程共享
 ThreadLocal不是用于解决多线程共享资源的问题，因为每个线程都会备份ThreadLocal变量的副本，相当于对线程自身局部变量的操作，所以不存在资源同步的问题。ThreadLocal主要解决变量需要在线程内方法之间传递但在不同线程间隔离的问题。
每个访问 ThreadLocal 变量的线程都有自己的一个“本地”实例副本

## 引用顺序
强引用:绝不会被回收
软引用:内存空间不足就会被回收
弱引用:一旦被发现就被回收
虚引用:被回收的时候会发一个消息

## 说一下内存泄漏的场景
应用程序不再使用对象，但是垃圾回收器无法删除它们，因为它们已被引用。
class stack{    Object data[1000];    int top = -1;    public void push(Object o){        top++;        data[top] = o;    }    public Object pop(Object o){        top--;        return data[top+1];    }}

## 如何防止基础类被破坏
双亲委派模型。
具体实现：
![](https://user-gold-cdn.xitu.io/2018/7/4/16465fe65c8f85b4?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

一个类在加载时会优先让父类加载器去加载，如果不行再使用自定义加载器加载。

## 动态加载
动态加载是使用反射实现的，而静态加载是使用new关键字，在编译期实现的。


## 手写一下快排的代码
快速排序是挖坑填数+分治来实现的
快速排序的基本思想:
1．先从数列中取出一个数作为基准数。

2．分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。

3．再对左右区间重复第二步，直到各区间只有一个数。

挖坑法实现:
```
public static void pothlingSort(int[] arrays , int low , int high){
    if(low < high){
        //求每次分治的分割线
		int divideIndex = getDivideIndex(arrays,low,high);
        //再递归分别对分割的俩个子数组进行递归排序
		pothlingSort(arrays,low,divideIndex -1);
		pothlingSort(arrays,divideIndex + 1, high);
    }
}

private static int getDivideIndex(int[] arrays, int low, int high) {
    // 将数组最左端arrays[0]作为默认的基准值,将最左端的值放至基准值的坑内。
    // 此时arrays[0]没有值了，需要从最右端找到一个比基准值小的数填至[0]这个坑。
    // 再从左到右找到一个比基准值大的数填到刚才的坑。循环进行直到low=high
    // 将基准值填至刚才的low位置。再进行分治

    int baseValue = arrays[low];
    arrays[low] =0 ; //挖个坑

    while(low <high){
        //从右往左,找第一个比坑数小的数字
        while(low < high && arrays[high] >= baseValue){
				high--;
			}
        
        arrays[low] = arrays[high] ;
		arrays[high] = 0 ;

        //从左往右,找第一个比坑大的数字
        while(low < high && arrays[low] <= baseValue){
				low++;
			}
			arrays[high] = arrays[low] ;
			arrays[low] = 0 ;
    }

    if(low == high){
			arrays[low] = baseValue;
		}
		
		return low;
    //最后坑填完了,返回坑,或者不返回
}
```

## java的跨平台性如何理解
JVM会把.java文件翻译成.class字节码文件,然后虚拟机识别平台,对应不同的平台转换为机器码.
注意不同平台下需要安装不同版本的JVM.

## String，StringBuilder，StringBuffer的区别，哪个是线程安全的
String是不可变的常量.
StringBuffer是字符串变量（线程安全）,使用synchronized关键字来进行操作.
StringBuilder是字符串变量(线程不安全)但是快

## ArrayList，LinkedList的区别，适用场景，线程安全，如果要实现线程安全怎么办
1. ArrayList是实现了基于动态数组的数据结构，而LinkedList是基于链表的数据结构；
2. 对于随机访问get和set，ArrayList要优于LinkedList，因为LinkedList要移动指针；

都是线程不安全的,如果要安全可以用两种方法:
1. List<String> list = Collections.synchronizedList(new LinkedList<String>());
也就是使用Collections.synchronizedList这个方法包装一下
2. 或者用ConcurrentLinkedQueue代替linkedList
如果是要用Array的话,要使用CopyOnWriteArrayList,每次做更新操作都会做一次数组拷贝

## TreeMap的线程安全问题
线程不安全,也是同上两种方式:
Collections.synchronizedSortedSet/Collections.synchronizedSortedMap方法包装一下
ConcurrentSkipListMap/ConcurrentSkipListSet

## 讲讲动态代理
静态代理:就是单纯的封装一层,类似装饰者模式,拓展一些功能.
缺点:写死的类,会有很多的代理类和重复代码.

动态代理:使用反射来动态的获取不同的目标类,并且生成代理类
代理对象不需要实现接口,但是目标对象一定要实现接口,否则不能用动态代理
static Object newProxyInstance(ClassLoader loader, Class<?>[] interfaces,InvocationHandler h )使用这一行来实现代理
示例代码:
```
/**
 * 创建动态代理对象
 * 动态代理不需要实现接口,但是需要指定接口类型
 */
public class ProxyFactory{

    //维护一个目标对象
    private Object target;
    public ProxyFactory(Object target){
        this.target=target;
    }

   //给目标对象生成代理对象
    public Object getProxyInstance(){
        return Proxy.newProxyInstance(
                target.getClass().getClassLoader(),
                target.getClass().getInterfaces(),
                new InvocationHandler() {
                    @Override
                    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
                        System.out.println("开始事务2");
                        //运用反射执行目标对象方法
                        Object returnValue = method.invoke(target, args);
                        System.out.println("提交事务2");
                        return returnValue;
                    }
                }
        );
    }

}
```
如果目标对象只是一个单独的对象,并未实现接口,这时候就要用到子类代理.
Cglib代理,也叫作子类代理,它是在内存中构建一个子类对象从而实现对目标对象功能的扩展.
Cglib是一个强大的高性能的代码生成包,它可以在运行期扩展java类与实现java接口.它广泛的被许多AOP的框架使用,例如Spring AOP和synaop,为他们提供方法的interception(拦截)

如果方法为private,static则无法进行代理.

在spring AOP中往往使用代理模式来进行切面编程

## 介绍NIO
NIO=Non-blocking I/O.是同步非阻塞的I/O模型
不同的IO模型:
![](https://awps-assets.meituan.net/mit-x/blog-images-bundle-2016/77752ed5.jpg)
NIO一个重要的特点是：socket主要的读、写、注册和接收函数，在等待就绪阶段都是非阻塞的，真正的I/O操作是同步阻塞的（消耗CPU但性能非常高）

## 红黑树
红黑树:二叉平衡搜索树
二叉排序树的性能取决于二叉树的层数,最好的情况是logn,完全二叉排序树,最差的情况是On,全部有序.

红黑树是在二叉查找树的基础上额外添加了一个标记,和一些规则.
红黑树保证了一种平衡，插入、删除、查找的最坏时间复杂度都为 O(logn)。

### 黑色高度
从根节点到叶节点的路径上黑色节点的个数，叫做树的黑色高度。

一些规则:
每个节点要么是红色，要么是黑色；
根节点永远是黑色的；
所有的叶节点都是是黑色的（注意这里说叶子节点其实是上图中的 NIL 节点）；
每个红色节点的两个子节点一定都是黑色；
从任一节点到其子树中每个叶子节点的路径都包含相同数量的黑色节点；

性质 4 的意思是：从每个根到节点的路径上不会有两个连续的红色节点，但黑色节点是可以连续的。

### 左旋和右旋
![](https://user-gold-cdn.xitu.io/2016/11/29/45e6629fc939b2140fa30b885a0db6bf?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

### 红黑树的平衡插入
红黑树的插入主要分两步：

首先和二叉查找树的插入一样，查找、插入
然后调整结构，保证满足红黑树状态
对结点进行重新着色
以及对树进行相关的旋转操作

前面说了，插入一个节点后要担心违反特征 4 和 5，数学里最常用的一个解题技巧就是把多个未知数化解成一个未知数。我们这里采用同样的技巧，把插入的节点直接染成红色，这样就不会影响特征 5，只要专心调整满足特征 4 就好了。这样比同时满足 4、5 要简单一些。

染成红色后，我们只要关心父节点是否为红，如果是红的，就要把父节点进行变化，让父节点变成黑色，或者换一个黑色节点当父亲，这些操作的同时不能影响 不同路径上的黑色节点数一致的规则。