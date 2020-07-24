# files_mover
file move automation : when it' s running in background, move automatically the files from Downloads into their respectiv directory like Picture/Video/Music/Document.

It's very usefull when you're working on a project and you have to download bunch on files, it much more easier to classify them.

## Prerequisite
No prerequisite.

## Error handling
No error found for the moment...

You can modify the time to update the Download folder if you don't want it to be each second.

## Use
python3 pathTOfile/files_mover.py

## Tip
you can directly run this program in background without doing nothing :

First solution (the one that I use) : edit the ~/.bashrc file in linux and write to the end of the file : python3 pathTOfile/files_mover.py &

Second solution (I didn't manage to do it) : create a windows service following these explanations :

http://thepythoncorner.com/dev/how-to-create-a-windows-service-in-python/

https://www.youtube.com/watch?v=R090APfdu58

## For futher
You can directly modify the python file to make it correspond the way that you prefer with the type of file you want and the directory you want.
