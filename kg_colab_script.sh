# Script to download dataset from Kaggle to Google Colab
# Have to upload kaggle.json manually to current directory
#!/bin/bash
pip install -q kaggle
mkdir ~/.kaggle
cp kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
kaggle datasets download -d $1
mkdir dataset
IFS='/' read -ra ADDR <<< "$1"
for ((i=0; i<${#ADDR[@]}; i++ ));
do
  if [ $i -eq 1 ]
  then
    unzip "${ADDR[$i]}.zip" -d dataset
  fi
done
