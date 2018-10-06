#!/usr/bin/env bash

# cat $1|awk '{print "0,",$1}'
cat $1|awk '{ print "0,", $1}'
# for line in $(cat < "$1")
# do
#     d="$(echo $line|rev|cut -c 2-|rev)"
#     echo "0,$d"
# done

# while read p; do
#     # c=$(( ( RANDOM % 2048 )  + 1 ))
#     d="$(echo $p|rev|cut -c 2-|rev)"
#     echo "0,${d}"
# done <$1