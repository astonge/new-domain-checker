#!/usr/bin/env bash

#https://whoisds.com//whois-database/newly-registered-domains/2018-10-01.zip/nrd

today="$(date -v -1d +"%Y-%m-%d")"
curl "https://whoisds.com//whois-database/newly-registered-domains/$today.zip/nrd" -o $today.zip
