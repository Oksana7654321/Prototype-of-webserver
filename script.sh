for i in `seq 1 15`: 
	do
		curl localhost:8080 &
done
wait