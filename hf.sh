#!/bin/sh
# To run the file: chmod +x hf.sh && ./hf.sh [repo-name]


python -m pip install huggingface_hub tensorboard tqdm torchinfo
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
apt-get install git-lfs

# git clone https://huggingface.co/harryph/[repo-name]
git clone https://huggingface.co/harryph/$1
cd $1


git config user.email "phamharrytdn@gmail.com"
git config user.name "Harry"

git remote set-url origin https://harryph:[access-token]@huggingface.co/harryph/$1
git pull origin
git lfs install

