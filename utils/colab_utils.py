#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/02_production_colab.ipynb
import os
REQUIREMENTS_PIP = """pip install azure-cognitiveservices-search-imagesearch
pip install git+https://github.com/fastai/fastai2
pip install git+https://github.com/fastai/fastcore
pip install nbdev"""

SETUP_WARNING="""    NOTE: For debugging and visualizing stdout, please run:
    from colab_utils import *
    !{REQUIREMENTS_PIP}
    !{GIT_CLONE_REPOSITORY}
    %cd {FASTAI_NB_PATH}
"""

GIT_CLONE_REPOSITORY = 'git clone https://github.com/fastai/course-v4/'

FASTAI_NB_PATH = "course-v4/nbs/"
def install_requirements():
    print("Installing requirements...")
    os.system(REQUIREMENTS_PIP)
    print("Done!")

def clone_repository():
    print("Cloning FastAI Repository...")
    os.system(GIT_CLONE_REPOSITORY)
    print("Done!")

def open_nb_folder():
    print(f"Opening folder {FASTAI_NB_PATH} with nbs and utils files...")
    os.chdir(FASTAI_NB_PATH)
    print("Done!")

def setup_fastai_colab():
    print(SETUP_WARNING)
    install_requirements()
    clone_repository()
    open_nb_folder()
