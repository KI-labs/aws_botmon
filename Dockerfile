FROM python:alpine3.7
COPY . /app
WORKDIR /app
ENV SLACK_TOKEN
ENV APP_ENV production
ENV SLACK_CHANNEL aws_monitor
ENV FLASK_APP /app/monitor_main.py
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "monitor_main.py" ]