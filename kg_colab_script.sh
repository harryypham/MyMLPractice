# Script to download dataset from Kaggle to Google Colab
pip install -q kaggle
echo "from google.colab import files 
files.upload()" >> script_upload_file.py
python script_upload_file.py
mkdir ~/.kaggle
cp kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
kaggle datasets download -d $1
mkdir dataset
unzip "$1.zip" -d dataset
