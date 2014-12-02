#!/bin/bash
echo "Assignment 2 - Question 2"
echo "TFIDF"
IN="/user/s0925284/exc2/output/task_1.out"
OUT="/user/s0925284/exc2/output/task_2.out"
MAP="task2mapper.py"
RED="task2reducer.py"
OUTFILE="Question_2"
NUMR=1

hadoop dfs -rmr $OUT

RUN="hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -D mapred.reduce.tasks=$NUMR -input $IN -output $OUT -mapper $MAP -file $MAP -reducer $RED -file $RED -file terms.txt"
$RUN
rm -r $OUTFILE
hadoop dfs -copyToLocal $OUT $OUTFILE
echo "Script complete, see output Directory."
