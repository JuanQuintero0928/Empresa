start chrome.exe https://www.youtube.com/watch?v=F2kAQymIyMc
mkdir "Abrir"
cd Abrir
touch Readme.txt
touch ver.txt
mkdir "Foto"
cd Foto
powershell Invoke-WebRequest -OutFile img1.jpg http://drive.google.com/u/3/uc?id=1_l73d2jTNa8x6b4_3OFdbycrMKlJtIov&export=download
powershell Invoke-WebRequest -OutFile img2.jpg https://drive.google.com/u/3/uc?id=1tEEBgdiCYisdtVoG4NGvhXR5a76C87MN&export=download
cd..
echo ¡Te Amooo Muchisimooooo! > Readme.txt
echo Abre la carpeta que se te creo! > ver.txt
start notepad ver.txt

