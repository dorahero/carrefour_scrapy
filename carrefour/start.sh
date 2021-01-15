#!/bin/bash
export DOCKER_HOST="tcp://172.16.16.139:2375"
docker run --rm dorahero2727/carrefour_scrapy:v3 crawl carrefour 
