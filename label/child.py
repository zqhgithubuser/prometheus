from prometheus_client import Summary

LATENCY = Summary(
    "http_requests_latency_seconds", "HTTP request latency.", labelnames=["path"]
)

# 创建子对象
foo = LATENCY.labels("/foo")


@foo.time()
def foo_handler(params):
    pass
