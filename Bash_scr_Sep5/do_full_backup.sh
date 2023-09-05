#!/bin/sh

echo "starting"

mkdir backups

cd ./backups

n=2
m=$(ls -1 | wc -l)

if [ "$m"  -gt "$n" ];
then
	ls -t | tail -n +3 | xargs rm
	tar -czvf $(date "+%m-%d-%y-%T").tar.gz ../src/*
else
	tar -czvf $(date "+%m-%d-%y-%T").tar.gz ../src/*
fi
