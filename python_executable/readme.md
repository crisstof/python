Programme de multiplication:
Le but est de créer un exécutable avec dépendance.
installer l'outil de création d'exécutable:
PyInstaller: pip install pyinstaller
cx_Freeze: pip install cx_Freezer

Préparer votre environnement virtuel pour isoler les dépendances de votre projet.
python -m venv nom_de_votre_environnement
nom_de_votre_environnement\Scripts\activate   #windows
source nom_de_votre_environnement/bin/activate   Linux/macOS

Installer toutes les dépendances dans cet environnement.
Installer pyinstaller par exemple:
pip install pyinstaller

Créez un fichier de configuration (si nécessaire)
pour cx_Freezer créez un fichier setup.py qui spécifie les paramètres de compilation et les scripts à inclure.
avec PyInstaller
pyinstaller --onefile votre_script.py
ou
avec cx_Freezer
python setup.py.build

Tester l'exécutable généré pour assurer qu'il fonctionne correctment sur différentes platformes.

pour les fichiers externes (images, base de données ...) utilisez l'option
include_files dans votre configuration
Surveillez la taille de l'exécutable.
L'xécutable est autonome qui peut être distribué et exécuté sur des systèmes n'ayant pas Python installé.

-------------------------------------------------------------------------------
Dans PyInstaller, le dossier "build" sert principalement de zone de travail temporaire pendant le processus de création de l'exécutable. Voici ses fonctions principales :

Stockage des fichiers intermédiaires : PyInstaller y écrit des fichiers de logs et de travail nécessaires à la compilation.

Analyse du code : C'est dans ce dossier que PyInstaller effectue l'analyse de votre script et de ses dépendances.

Préparation des ressources : Les modules Python et autres ressources nécessaires y sont rassemblés avant d'être intégrés à l'exécutable final1.

Compilation : Les fichiers Python sont compilés en bytecode dans ce dossier.

Le dossier "build" n'est pas destiné à être distribué avec votre application finale. L'exécutable et les fichiers nécessaires à la distribution se trouveront dans le dossier "dist" une fois le processus terminé.
-------------------------------------------------------------------------------
Collecting pefile!=2024.8.26,>=2022.5.30
  Downloading pefile-2023.2.7-py3-none-any.whl (71 kB)
     |██████████████                  | 30 kB 1.9 MB/s eta 0:00:0     |██████████████████              | 40 kB 2.6 MB/s eta 0:00:0     |███████████████████████         | 51 kB 3.2 MB/s eta 0:00:0     |███████████████████████████▌    | 61 kB 3.8 MB/s eta 0:00:0     |████████████████████████████████| 71 kB 4.5 MB/s eta 0:00:0     |████████████████████████████████| 71 kB 5.1 MB/s
Installing collected packages: packaging, pywin32-ctypes, pyinstaller-hooks-contrib, pefile, altgraph, pyinstaller
Successfully installed altgraph-0.17.4 packaging-24.2 pefile-2023.2.7 pyinstaller-6.12.0 pyinstaller-hooks-contrib-2025.1 pywin32-ctypes-0.2.3

--------problème------
dans notre environnement venv nous avons perdu pip donc on ne peut installer pygame.
réinstaller pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

pip --version

python -m pip install pygame


toujours le problème
Remove-Item -r ~* -Force
python -m pip install --upgrade pip

résolution
 pip install pygame --upgrade
 python.exe -m pip install --upgrade pip