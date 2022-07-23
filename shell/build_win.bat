call conda create -n niconicron python=3.8 -y
call conda activate niconicron
call pip install yt-dlp pyinstaller loguru
call pyinstaller main.spec --noconfirm
