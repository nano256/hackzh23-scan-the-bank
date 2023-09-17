#!/bin/bash
START=$(($(date +%s%N)/1000000))
python crawler.py
STOP=$(($(date +%s%N)/1000000))
echo "Crawler run time (ms)"
echo "$((STOP-START))"