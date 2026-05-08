


pwd
    2  ls
    3  df -h
    4  python
    5  sudo apt install python
    6  sudo apt install python3
    7  python3
    8  pip install numpypython3
    9  pip install numpy
   10  sudo apt install python3-pip
   11  pip
   12  sudo apt update
   13  sudo apt install python3-pip
   14  history



 lsb_release -d
 1921  cat /etc/upstream-release/lsb-release
 1922  scw
 1923  curl -L https://github.com/scaleway/scaleway-cli/releases/latest/download/scw-linux-amd64.tar.gz | tar xz -C /usr/local/bin
 1924  curl -L https://github.com/scaleway/scaleway-cli/releases/latest/download/scw-linux-amd64.tar.gz
 1925  wget https://github.com/scaleway/scaleway-cli/releases/latest/download/scw-linux-amd64.tar.gz
 1926  curl -s https://raw.githubusercontent.com/scaleway/scaleway-cli/master/scripts/get.sh
 1927  curl -s https://raw.githubusercontent.com/scaleway/scaleway-cli/master/scripts/get.sh | sh
 1928  scw --help
 1929  scw login
 1930  ssh root@2001:bc8:711:3a6f:dc00:1ff:fe02:e2eb
 1931  make add_to_env
 1932  scw instance
 1933  scw instance server --help
 1934  scw instance server list
 1935  scw instance server console
 1936  cp /mnt/NUC/perso/keys/id_ed25519_essai_scaleway* ~/.ssh
 1937  ls ~/.ssh
 1938  scw instance server console 8b7ac85f-738b-4741-ac03-60b150e99417 fr-par-1
 1939  scw instance server
 1940  scw instance server ssh
 1941  scw instance server ssh 8b7ac85f-738b-4741-ac03-60b150e99417 username=root port=22 zone=fr-par-1
 1942  ping 2001:bc8:711:3a6f:dc00:1ff:fe02:e2eb
 1943  #scp readme.md
 1944  scp readme.md root@2001:bc8:711:3a6f:dc00:1ff:fe02:e2eb:/data
 1945  scp readme.md root@"2001:bc8:711:3a6f:dc00:1ff:fe02:e2eb":/data
 1946  scp readme.md root@"[2001:bc8:711:3a6f:dc00:1ff:fe02:e2eb]":/data

# ssh key

<Laboite><Monbled><Monchien>_IV


à rentrer quand je ssh vers la machine

git clone https://github.com/louis-chevallier/scaleway.git


file transfer :
	ftp ftp.byethost7.com
name = b7_41867395
pw = ( dans firefox / passwd : byethost )

one line command :
	wget ftp://b7_41867395:yZtudpf9jrZHQ@ftp.byethost7.com/htdocs/test.wav
        curl -T test.wav -u "b7_41867395:yZtudpf9jrZHQ" ftp://ftp.byethost7.com/htdocs
        ftp ftp://b7_41867395:yZtudpf9jrZHQ@ftp.byethost7.com <<< "dir htdocs"
cd htdocs
put test.mp3


#pas utilisé
enabling google drive api ( for uploading with python )
https://d35mpxyw7m7k7g.cloudfront.net/bigdata_1/Get+Authentication+for+Google+Service+API+.pdf




install anaconda :
        curl -O https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Linux-x86_64.sh
        bash Anaconda3-2025.12-2-Linux-x86_64.sh
        cd anaconda3/bin
        ./pip install uv
        ./pip install utillc soundfile 
        ./uv venv tts
        source tts/bin/activate
        ./uv pip install -U vllm

        ./uv pip install vllm-omni --upgrade  # make sure to have >= 0.18.0
        
        python3 -c "import mistral_common; print(mistral_common.__version__)" # should print >= 1.10.0
        # ca écrit 1.11.2 chez moi
        
        sudo apt install ffmpeg
        sudo apt install calibre curl

        ebook-convert libre.epub livre.txt

dans une fenetre :
	vllm serve mistralai/Voxtral-4B-TTS-2603 --omni

dans une autre
         python client.py
         


lsblk


 lsblk
   28  fdisk -l
   29  df -h
   30  mkdir /mnt/block1
   31  mkfs.ext4 /dev/vda
   32  h
   33  history
   34  df -h
   35  fdisk -l
   36  df -h
   37  lsblk
   38  df -h .
   39  lsblk
   40  fdisk -l
   41  #mount /dev/vda /mnt/block1
   42  mkdir /mnt/local_vda
   43  mount /dev/vda /mnt/local_vda
   44  df -h
   45  touch /mnt/local_vda
   46  touch /mnt/local_vda/x
   47  ls /mnt/local_vda/
   48  history

louis-Latitude-7400|Wed Apr  1 11:42:07 AM CEST 2026|/home/louis/dev/scaleway|louis[121270]:scp readme.md root@"2001:bc8:711:3a6f:dc00:1ff:fe02:e2eb":/data  

louis-Latitude-7400|Wed Apr  1 11:40:47 AM CEST 2026|/home/louis/dev/scaleway|louis[137765]:ssh -i ~/.ssh/scaleway root@2001:bc8:711:3a6f:dc00:1ff:fe02:e2eb

louis-Latitude-7400|Wed Apr  1 10:38:12 AM CEST 2026|/home/louis/dev/scaleway|louis[121270]:curl -s https://raw.githubusercontent.com/scaleway/scaleway-cli/master/scripts/get.sh | sh
