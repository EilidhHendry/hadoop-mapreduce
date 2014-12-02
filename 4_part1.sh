#!/bin/bash
echo "Assignment 2 - Question 4 - Part 1"
echo "Querying Stack Overflow"
IN="/user/s1250553/ex2/task2/stackLarge.txt"
OUT="/user/s0925284/exc2/output/task_4_part1.out"
MAP="task4mapper_part1.py"
RED="task4reducer_part1.py"
OUTFILE="Question_4_part1"
NUMR=1

hadoop dfs -rmr $OUT

RUN="hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -D mapred.reduce.tasks=$NUMR -input $IN -output $OUT -mapper $MAP -file $MAP -reducer $RED -file $RED"
$RUN
rm -r $OUTFILE
hadoop dfs -copyToLocal $OUT $OUTFILE
echo "Script complete, see output Directory."
