'''Open a file in the Pythonista text editor, or vi
if not on iPad. Only works with file extensions that
Pythonista recognizes.
'''

import os

HAS_EDITOR = False

try:
    import editor
    import console
    HAS_EDITOR = True
except:
    pass

from ... tools.toolbox import bash

def main(self, line):
    args = bash(line)
    
    if len(args) == 1:
        if HAS_EDITOR:
            print 'Opening {0} in Pythonista editor.'.format(args[0])
            editor.open_file(os.path.join(os.getcwd(), args[0]))
            console.hide_output()
        else:
            import platform
            if platform.system() == 'Linux':
                os.system('vi {0}'.format(args[0]))
            else:
                print 'Unsupported platform'
    else:
        print 'Usage: editor <filename>'
