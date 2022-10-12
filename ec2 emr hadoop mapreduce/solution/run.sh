#!/bin/bash
i=1

chmod 744 mapper.py
chmod 744 reducer.py
chmod 744 driver.py

while :
do
	hadoop jar ./hadoop-streaming-3.1.4.jar \
	-D mapred.reduce.tasks=1 \
	-D mapred.text.key.partitioner.options=-k1 \
	-file ./mapper.py \
	-mapper ./mapper.py \
	-file ./reducer.py \
	-reducer ./reducer.py \
	-file ./M.txt ./N.txt ./X.txt \
	-input ./M.txt ./N.txt ./X.txt \
	-output /mapreduce-output$i \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner


	
	rm -f output1.txt
	hadoop fs -copyToLocal /mapreduce-output$i/part-00000 output1.txt

	python driver.py

	if [ $?  ==  0 ]
	then
		rm output1.txt
		hadoop fs -copyToLocal /mapreduce-output$i/part-00000 output1.txt
		break
	else
		rm output1.txt
		hadoop fs -copyToLocal /mapreduce-output$i/part-00000 output1.txt
	fi
	i=$((i+1))
done

