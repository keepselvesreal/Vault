from flask import Flask, Response
import redis

# ts: 로깅 설정 추가
import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)


# ts: Redis 연결 확인 함수
def check_redis_connection():
    try:
        if r.ping():
            logger.info("Redis 연결 성공")
    except redis.ConnectionError:
        logger.error("Redis 연결 실패", exc_info=True)
        sys.exit(1)

# ts: Redis 연결 확인
check_redis_connection()


@app.route('/metrics')
def metrics():
    thumbs_down_count = int(r.get('thumbs_down_count') or 0)
    thumbs_up_count = int(r.get('thumbs_up_count') or 0)

    prometheus_data = (
        f'thumbs_down_count {thumbs_down_count}\n'
        f'thumbs_up_count {thumbs_up_count}\n'
    )

    return Response(prometheus_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)