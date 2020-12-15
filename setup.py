#!/usr/bin/env python

"""
setup.py file for Verovio
"""

from glob import glob
import os
import platform
from setuptools import setup, Extension
from setuptools.command.sdist import sdist as _sdist
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel


# There is no task common to both sdist and bdist_wheel, so we override both commands to
# generate the git version header file
class sdist(_sdist):
    def run(self):
        # generate the git commit include file
        os.system("cd tools; ./get_git_commit.sh")
        _sdist.run(self)


class bdist_wheel(_bdist_wheel):
    def run(self):
        # generate the git commit include file
        os.system("cd tools; ./get_git_commit.sh")
        _bdist_wheel.run(self)


EXTRA_COMPILE_ARGS = ['-DPYTHON_BINDING']
if platform.system() != 'Windows':
    EXTRA_COMPILE_ARGS += ['-std=c++17',
                           '-Wno-write-strings', '-Wno-overloaded-virtual']
else:
    EXTRA_COMPILE_ARGS += ['-DNO_PAE_SUPPORT']

verovio_module = Extension('verovio._verovio',
                           sources=glob('./src/*.cpp') + glob('./src/hum/*.cpp') +
                           [
                               './src/json/jsonxx.cc',
                               './src/pugi/pugixml.cpp',
                               './src/midi/Binasc.cpp',
                               './src/midi/MidiEvent.cpp',
                               './src/midi/MidiEventList.cpp',
                               './src/midi/MidiFile.cpp',
                               './src/midi/MidiMessage.cpp',
                               './libmei/attconverter.cpp',
                               './libmei/atts_analytical.cpp',
                               './libmei/atts_cmn.cpp',
                               './libmei/atts_cmnornaments.cpp',
                               './libmei/atts_critapp.cpp',
                               './libmei/atts_gestural.cpp',
                               './libmei/atts_externalsymbols.cpp',
                               './libmei/atts_facsimile.cpp',
                               './libmei/atts_mei.cpp',
                               './libmei/atts_mensural.cpp',
                               './libmei/atts_midi.cpp',
                               './libmei/atts_neumes.cpp',
                               './libmei/atts_pagebased.cpp',
                               './libmei/atts_shared.cpp',
                               './libmei/atts_visual.cpp',
                               './bindings/python/verovio.i'],
                           swig_opts=['-c++', '-outdir', 'verovio'],
                           include_dirs=['/usr/local/include',
                                         './include',
                                         './include/vrv',
                                         './include/json',
                                         './include/midi',
                                         './include/hum',
                                         './include/pugi',
                                         './include/utf8',
                                         './include/win32',
                                         './libmei'],
                           extra_compile_args=EXTRA_COMPILE_ARGS
                           )

setup(name='verovio',
      cmdclass={'sdist': sdist, 'bdist_wheel': bdist_wheel},
      version='3.1.0-dev',
      url="www.verovio.org",
      description="""A library and toolkit for engraving MEI music notation into SVG""",
      ext_modules=[verovio_module],
      packages=['verovio',
                'verovio.data',
                'verovio.data.Bravura',
                'verovio.data.Gootville',
                'verovio.data.Leipzig',
                'verovio.data.Petaluma',
                'verovio.data.text'],
      package_dir={'verovio.data': 'data'},
      package_data={
          'verovio.data': [f for f in os.listdir('./data') if f.endswith(".xml")],
          'verovio.data.Bravura': os.listdir('./data/Bravura'),
          'verovio.data.Gootville': os.listdir('./data/Gootville'),
          'verovio.data.Leipzig': os.listdir('./data/Leipzig'),
          'verovio.data.Petaluma': os.listdir('./data/Petaluma'),
          'verovio.data.text': os.listdir('./data/text'),
      }
      )
