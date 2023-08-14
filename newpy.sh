#!/bin/bash

FILE_NAME=$1
echo "#!/usr/bin/python" >> $FILE_NAME
sudo chmod +x $FILE_NAME
exit 0