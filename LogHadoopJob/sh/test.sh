echo 'start'
yesterday=`date -d yesterday +%Y%m%d`
echo 'done' > /home/client/analyze_data/$yesterday
echo 'end'
if [ ! $1 ]; then
	echo 'done'
fi
