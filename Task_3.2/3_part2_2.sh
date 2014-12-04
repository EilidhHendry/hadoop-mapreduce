#!/bin/bash
echo "Assignment 2 - Question 3 - Part 2"
echo "Log analysis"
IN="/user/s0925284/exc2/output/task_3_part2.out"
OUT="/user/s0925284/exc2/output/task_3_part2_2.out"
MAP="task3mapper_part2_2.py"
RED="task3reducer_part2_2.py"
OUTFILE="Question_3_part2_2"
NUMR=1

hadoop dfs -rmr $OUT

RUN="hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D mapred.text.key.comparator.options=-nr -D mapred.reduce.tasks=$NUMR -input $IN -output $OUT -mapper $MAP -file $MAP -reducer $RED -file $RED"
$RUN
rm -r $OUTFILE
hadoop dfs -copyToLocal $OUT $OUTFILE
echo "Script complete, see output Directory."
