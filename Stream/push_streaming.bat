:while
ffmpeg -re -f concat -safe 0 -i ./Stream/listA -s 400x400 -vcodec copy -acodec aac -b:a 192k -f flv "rtmp://111.231.234.217/live/livestream"
goto while