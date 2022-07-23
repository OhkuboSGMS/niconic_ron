conda create -n niconicron python=3.6 -y
conda activate niconicron
pip install yt-dlp pyinstaller loguru

pyinstaller main.spec --noconfirm

#mv dist\niconicron ~/bin

