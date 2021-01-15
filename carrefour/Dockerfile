FROM python:3.6
COPY . /carrefour
WORKDIR /carrefour
RUN pip install -r requirements.txt
ENTRYPOINT [ "scrapy" ]
CMD [ "crawl carrefour" ]