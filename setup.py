from setuptools import setup, find_pakages
import pynq_proj

setup(
	name = "neo_pynq",
	version = neo_pynq.__version__,
	url = 'https://github.com/ATaylorCEngFIET/pynq_neopixel',
	license = 'Apache Software License',
	author = "Adam Taylor",
	author_email = "adam@adiuvoengineering.com",
	packages = ['neo'],
	package_data = {
	 '' : ['*.bit','*.tcl'],
	},
	description = "Neo Pixel Driver for PYN1 Z2",

