import multiprocessing

bind = "0.0.0.0:9999"
workers = multiprocessing.cpu_count()
accesslog = "/tmp/bloom.access.log"
wsgi_app  = "app:app"

logconfig = "logging.conf"
