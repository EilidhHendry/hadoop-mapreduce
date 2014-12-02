#!/bin/bash
echo "Assignment 2 - Question 1"
echo "Inverse Index of Document Frequency"
IN="/user/s0925284/exc2/output/task_1_part_1.out"
OUT="/user/s0925284/exc2/output/task_2.out"
MAP="task1mapper_part2.py"
RED="task1reducer_part2.py"
OUTFILE="Question_1"
NUMR=1

hadoop dfs -rmr $OUT

RUN="hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -D mapred.reduce.tasks=$NUMR -input $IN -output $OUT -mapper $MAP -file $MAP -reducer $RED -file $RED"
$RUN
rm -r $OUTFILE
hadoop dfs -copyToLocal $OUT $OUTFILE
echo "Script complete, see output Directory."
