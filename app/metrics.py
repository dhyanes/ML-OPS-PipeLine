from prometheus_client import Counter, Histogram

# Request count
REQUEST_COUNT = Counter(
    "prediction_requests_total",
    "Total number of prediction requests"
)

# Latency
REQUEST_LATENCY = Histogram(
    "prediction_latency_seconds",
    "Latency of prediction requests"
)