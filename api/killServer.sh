for i in $(ps -ef | grep "/home/pi/edt-bot-iut/api/*.py" | tr -s " " | cut -d " " -f2)
do
	echo $i
	kill  -9 $i
done
