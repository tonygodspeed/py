#!/bin/sh

echo 'start'
echo `date +%H:%M:%S`
yesterday=`date -d yesterday +%Y%m%d`
ten_days_age=`date -d '10 days ago' +%Y%m%d`
an_date=$yesterday

py_path=/home/client/code/py
raw_path=/home/client/raw_data/$an_date/top
mkdir home/client/raw_data/$an_date
an_path=/home/client/analyze_data/$an_date
mkdir home/client/analyze_data/$an_date
echo $py_path

output_path=/user/client/analyze_data/$an_date/top
echo $an_data
hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.6.0.jar \
	-input /data/log/client/real/$an_date/*.play_music.gz \
	-file $py_path/mapper.py \
	-file $py_path/dispatcher.py \
	-file $py_path/common_util.py \
	-file $py_path/common_def.py \
	-file $py_path/reducer.py \
	-file $py_path/MR_RECOM_SHOW.py \
	-file $py_path/MR_RECOM_RUN.py \
	-file $py_path/MR_RECOM_START.py \
	-file $py_path/MR_INSTALL.py \
	-file $py_path/MR_ERROR_LOG.py \
	-file $py_path/MR_DataRepairDES.py \
	-file $py_path/MR_AppStart.py \
	-file $py_path/MR_REGDLL.py \
	-file $py_path/MR_CL_START.py \
	-file $py_path/MR_COMMON_START.py \
	-file $py_path/MR_DISP_START.py \
	-file $py_path/MR_INSTALL_REG_TOOLS.py \
	-file $py_path/MR_DISP_KSLIVE.py \
	-file $py_path/MR_KSLIVE.py \
	-file $py_path/MR_DRTASKMGR.py \
	-file $py_path/MR_CRASHREPORT.py \
	-file $py_path/MR_PLAY_MUSIC.py \
	-mapper mapper.py \
	-reducer reducer.py \
	-output $output_path \
	-cmdenv "condition=word_count"
#hadoop fs -text $output_path/part-* >> $raw_path/analyze_data.$an_date
echo `date +%H:%M:%S`
echo $raw_path
mkdir $raw_path
hadoop fs -get $output_path/part-* $raw_path/
echo 'get finish'
mkdir $an_path
tar zcvf $an_path/$an_date.top.tar.gz $raw_path/
echo `date +%H:%M:%S`
echo 'done' > $an_path
hadoop fs -rm -r /user/client/analyze_data/$ten_days_age/top
