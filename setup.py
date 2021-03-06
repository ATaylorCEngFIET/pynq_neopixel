from setuptools import setup, find_packages
#import neo_pynq
from distutils.dir_util import copy_tree
import os
import shutil

# global variables
board = os.environ['BOARD']
repo_board_folder = f'boards/{board}/neo_pixel'
board_notebooks_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']
hw_data_files = []
ovl_dest = 'neo_pixel'


# check whether board is supported
def check_env():
    if not os.path.isdir(repo_board_folder):
        raise ValueError("Board {} is not supported.".format(board))
    if not os.path.isdir(board_notebooks_dir):
        raise ValueError("Directory {} does not exist.".format(board_notebooks_dir))


# copy overlays to python package
def copy_overlays():
    src_ol_dir = os.path.join(repo_board_folder, 'bitstream')
    dst_ol_dir = os.path.join(ovl_dest, 'bitstream')
    copy_tree(src_ol_dir, dst_ol_dir)
    hw_data_files.extend([os.path.join("..", dst_ol_dir, f) for f in os.listdir(dst_ol_dir)])


# copy notebooks to jupyter home
def copy_notebooks():
    src_nb_dir = os.path.join(repo_board_folder, 'notebook')
    dst_nb_dir = os.path.join(board_notebooks_dir, 'neo_pixel')
    if os.path.exists(dst_nb_dir):
        shutil.rmtree(dst_nb_dir)
    copy_tree(src_nb_dir, dst_nb_dir)


check_env()
copy_overlays()
copy_notebooks()

setup(
	name= "neo_pixel",
	version= "1.1",
	url= 'https://github.com/ATaylorCEngFIET/pynq_neopixel.git',
	license = 'Apache Software License',
	author= "Adam Taylor",
	author_email= "adam@adiuvoengineering.com",
	packages= find_packages(),
	package_data= {
	 '': hw_data_files,
	},
	description= "Neo Pixel Driver for PYN1 Z2",
)
