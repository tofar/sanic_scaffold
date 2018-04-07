FROM python:3.6
LABEL maintainer="yun_tofar@qq.com"
LABEL version="1.0"
LABEL description="python sanic scaffold"

COPY ./src /app

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

CMD python -m sanic main.app --host=0.0.0.0 --port=3031 --workers=4