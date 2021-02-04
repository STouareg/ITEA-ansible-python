#!/bin/bash
pid_file='/home/admturyk/lesson5-ansible/script.pid'
if [ ! -s "$pid_file" ] || ! kill -0 $(cat $pid_file) > /dev/null 2>&1; then
  echo $$ > "$pid_file"
  exec /usr/bin/python3.8 /home/admturyk/lesson5-ansible/bot.py
fi
