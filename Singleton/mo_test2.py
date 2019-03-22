# from module import singleton 

import module
singleton = module.singleton

singleton.x = 2
print(__name__, singleton, singleton.x)
