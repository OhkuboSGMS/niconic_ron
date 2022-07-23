conda create -n niconicron python=3.6.6  -y
source activate niconicron
pip install yt-dlp pyinstaller loguru

pyinstaller main.spec --noconfirm

mv dist ~/bin/

