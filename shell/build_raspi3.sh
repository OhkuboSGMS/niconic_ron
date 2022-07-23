conda create -n niconicron  -y
source activate niconicron
pip install yt-dlp pyinstaller loguru

pyinstaller main.spec --noconfirm

mv dist ~/bin/

