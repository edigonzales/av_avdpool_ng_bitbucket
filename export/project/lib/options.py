# -*- coding: utf-8 -*-

from argparse import ArgumentParser

class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        usage = 'bin/export'
        self.parser = ArgumentParser(usage=usage)
        self.parser.add_argument('-x',
                                '--example',
#                                 required=True, 
                                default='example-value',
                                dest='example',
                                help='An example option')

        self.parser.add_argument('-t',
                                '--targetdir',
                                action = 'store',
                                type = str, 
                                default ='/tmp/',
                                dest ='targetdir',
                                help = 'Directory to move the finished tiles to.')

        self.parser.add_argument('-r',
                                '--dpi',
                                action = 'store',
                                type = int, 
                                default = 508, 
                                dest ='dpi',
                                help = 'Resolution (dpi) to generate the tiles at. Default: 508.')

        self.parser.add_argument('-s',
                                '--scale',
                                action = 'store',
                                type = int, 
                                default = 5000,
                                dest ='scale',
                                help = 'Scale of the map. Default: 5000 (for 1:5000).')

        self.parser.add_argument('-c',
                                '--colortype',
                                action = 'store',
                                type = str, 
                                default = 'sw',
                                dest ='colortype',
                                choices = ['sw', 'f'],
                                help = 'Color (f) or black/white (sw) map. Default: sw.')

        self.parser.add_argument('--noclip',
                                action = 'store_false',
                                default = True,
                                dest ='clip',
                                help = "Don't clip the output to a geometry which is specified in the script settings.")

        self.parser.add_argument('-l',
                                '--layer',
                                action = 'store',
                                type = str, 
                                default = 's',
                                dest ='mode',
                                choices = ['s', 'l', 'b'],
                                help = 'Generate just the situation (s), the real estate (Liegenschaften, l), or both (b). Default: s.')

        self.parser.add_argument('--tile',
                                action = 'store',
                                type = str, 
                                default = "",
                                dest ='restrict_tile',
                                help = 'Only create the tile with the specified name, even if there are more tiles in the tile index than just this one. This tile must be listed in the tile index file.')

        self.parser.add_argument('-o',
                                '--overlap',
                                action = 'store',
                                type = str, 
                                default = '100.0 50.0',
                                dest ='overlap',
                                help = "Overlap (meters) in x and y direction to use for improved creation of the label layer (e.g. '0 0'). Default: '100.0 50.0'.")

        self.parser.add_argument('--canton',
                                action = 'store',
                                type = str, 
                                default = '11',
                                dest ='canton',
                                choices = ['11'],
                                help = 'Number of canton. Default: 11.')

        self.parser.add_argument('--preprocess',
                                action = 'store_true',
                                default = False,
                                dest ='preprocess',
                                help = "Don't preprocess cadastral data.")

        self.parser.add_argument('--all',
                                action = 'store_true',
                                default = False,
                                dest ='all',
                                help = "Export all communities.")


    def parse(self, args=None):
        return self.parser.parse_args(args)
