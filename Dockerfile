FROM python:3
WORKDIR /app
COPY . /app
RUN pip install -r requirenments
EXPOSE 5000
CMD  python ./views.py
