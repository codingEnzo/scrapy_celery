broker_url = "redis://158f0830c2.iask.in:12700/2"
result_backend = "redis://158f0830c2.iask.in:12700/3"
include = ['spider_service.services.spider_service',]
task_default_queue = 'celery_spider_queue'