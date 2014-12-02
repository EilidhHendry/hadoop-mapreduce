#!/bin/bash
echo "Assignment 2 - Question 3"
echo "Log analysis"
IN="/user/s1250553/ex2/task2/logsLarge.txt"
OUT="/user/s0925284/exc2/output/task_3_part1.out"
MAP="task3mapper_part1.py"
RED="task3reducer_part1.py"
OUTFILE="Question_3"
NUMR=10

hadoop dfs -rmr $OUT

RUN="hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -D mapred.reduce.tasks=$NUMR -input $IN -output $OUT -mapper $MAP -file $MAP -reducer $RED -file $RED -file terms.txt"
$RUN
rm -r $OUTFILE
hadoop dfs -copyToLocal $OUT $OUTFILE
echo "Script complete, see output Directory."
