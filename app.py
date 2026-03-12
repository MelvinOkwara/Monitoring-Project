from flask import Flask, Response
import prometheus_client
from prometheus_client import Counter, Histogram
import time
import random

app = Flask(__name__)

# Metrics definitions
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP Request Latency', ['endpoint'])

@app.route('/')
def hello():
    start_time = time.time()
    
    # SIMULATE THE "BROKEN" PART: 
    # 20% of the time, make it slow (Latency) or fail (Errors)
    roll = random.random()
    if roll < 0.1:
        time.sleep(3) # Very slow!
    elif roll < 0.2:
        REQUEST_COUNT.labels(method='GET', endpoint='/', http_status='500').inc()
        return "Internal Server Error", 500

    REQUEST_COUNT.labels(method='GET', endpoint='/', http_status='200').inc()
    REQUEST_LATENCY.labels(endpoint='/').observe(time.time() - start_time)
    return "Hello! I am being monitored."

@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)