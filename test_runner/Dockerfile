FROM python:3.6-slim
MAINTAINER charlesplachno@outlook.com
COPY . /test-center
WORKDIR /test-center
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null