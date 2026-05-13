SHELL := /usr/bin/bash

key=d8b6abd8-2556-41d8-854c-ce611e58110b


# key /mnt/NUC/perso/keys/id_ed25519_essai_scaleway
# name = key_04_Avril


# api key 	SCWSKG7PAEV6Q9N66MQ3
# secret key 	4488a994-ef1d-4546-8752-65149e80b62b


start :
	python client.py


add_to_env :
	scw init -p newprofile \
  access-key=SCWSKG7PAEV6Q9N66MQ3\
  secret-key=4488a994-ef1d-4546-8752-65149e80b62b\
  organization-id=56e7bc20-f6cb-4f5c-9fc4-6182bde51f04\
  project-id=d8b6abd8-2556-41d8-854c-ce611e58110b


cp :
	rcp /mnt/NUC/www/book/linfortune.txt root@ 1946  root@"[2001:bc8:711:3a6f:dc00:1ff:fe02:e2eb]":/data

conda :
	curl -O https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Linux-x86_64.sh
	bash Anaconda3-2025.12-2-Linux-x86_64.sh -b -p ./anaconda

install : conda
	cd anaconda; make -f ../makefile install2
	ebook-convert huc_l_empire_chinois.epub livre.txt

install2 :
	sudo apt install -y ffmpeg
	sudo apt install -y calibre curl

	bin/pip install uv
	bin/uv venv tts
	source tts/bin/activate; make -f ../makefile install3

install3 :
	bin/uv pip install utillc soundfile 
	bin/uv pip install -U vllm
	bin/uv pip install vllm-omni --upgrade  # make sure to have >= 0.18.0
	bin/python3 -c "import mistral_common; print(mistral_common.__version__)" # should print >= 1.10.0
        # ca écrit 1.11.2 chez moi


clone :
	git clone https://github.com/louis-chevallier/scaleway.git


push :
	git commit -a -m xxx
	git push

serve :
	vllm serve mistralai/Voxtral-4B-TTS-2603 --omni

start :
	ebook-convert huc_l_empire_chinois.epub livre.txt
