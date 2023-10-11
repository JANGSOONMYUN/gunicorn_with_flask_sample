# Gunicorn
```
gunicorn -w 1 --bind 0.0.0.0:8000 server:app &
gunicorn -w 4 --bind 0.0.0.0:8000 server:app &

gunicorn -w 1 --bind 192.168.0.10:8000 server:app --log-file gunicorn.log & 
gunicorn -w 4 --bind 192.168.0.10:8000 server:app --log-file gunicorn.log & 
```

# Flask for Test
```
export FLASK_APP=server.py
flask run --host=192.168.0.10 --port=8000 
```

# Close gunicorn process
```
ps -ef | grep gunicorn
pgrep -f "gunicorn"
kill [pid]
```

# Close all
```
pkill -f "gunicorn"
```