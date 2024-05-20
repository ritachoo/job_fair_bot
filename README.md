# job_fair_bot
job fair bot

## start bot with infinity loop (ubuntu)

### create .env file and add TOKEN and CHAT_ID
```commandline
touch .env
```

### ensure that your system is updated and the required packages installed
```commandline
sudo apt update && sudo apt upgrade -y
```

### install python v3.10
```commandline
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10
```

### install process manager 'pm2'
```commandline
sudo apt install nodejs && sudo apt install npm
npm install pm2 -g
```

### start job fair bot
```commandline
pm2 start job_fair_form.py --interpreter=python3
```

### show all process 'pm2'
```commandline
pm2 list
```

### stop job fair bot
```commandline
pm2 stop job_fair_form
```

### stop all process 'pm2'
```commandline
pm2 stop
```

### show monitoring for process 'pm2' (for debug)
```commandline
pm2 monit
```
