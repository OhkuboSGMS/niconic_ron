conda create -n niconicron python=3.8
conda activate niconicron
pip install yt-dlp pyinstaller

pyinstaller main.spec
