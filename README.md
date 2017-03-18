# scrapy_celery

Asynchronous, multi-process and Distributed crawler customer base on scrapy core and celery task;
for initialization,  put the folder [spider_service] in the root folder of the scrapy project;
for using, execute "celery -A task worker -c 4 -l info" in the folder with "task.py", the service can notify the spider and load it automatically;
Then send task info to the queue on the redis, the crawler will begin to crawl;

异步的，多进程并发，分布式的，基于celery开发的scrapy任务调度服务插件；
将“spider_service”文件夹放在scrapy项目的根目录以初始化该插件；
在task.py目录执行 "celery -A task worker -c 4 -l info" 启动监听服务（爬虫不会启动）；
在redis的任务队列里传入爬去的种子任务，scrapy项目下的爬虫就会在插件的识别下自动启动；

特性：
资源消耗在并发量相同下，相比scrapy_redis略小；
任务设置参数动态可变；
下载器性能充分利用cpu和内存优势；
配有并发锁，并发负载可控；

--------------------------------------------------------------------------------------
Warning：
it only fit linux；
Windows 下不兼容；
