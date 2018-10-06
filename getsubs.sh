#!/usr/bin/env bash

while read domain; do
	docker run -t amass-docker -v -passive -d $domain
done <test.txt
