
#__version__ = '.'.join(map(str, version_info))
version_info = [0,0,0,'final',0]
version_info_js = [0,0,0,'final',0]
_specifier_ = {'alpha': 'a', 'beta': 'b', 'candidate': 'rc', 'final': ''}
__version__ = '%s.%s.%s%s'%(version_info[0], version_info[1], version_info[2],
  '' if version_info[3]=='final' else _specifier_[version_info[3]]+str(version_info[4]))

__version_js__ = '%s.%s.%s%s'%(version_info_js[0], version_info_js[1], version_info_js[2],
  '' if version_info[3]=='final' else '-%s.%s' % (version_info_js[3], str(version_info_js[4])))

__version_tuple__    = (0, 4, 0)
__version__ = '0.4.0'
__version_tuple_js__ = (0, 4, 0)
__version_js__ = '0.4.0'
__version_threejs__ = '0.85' # kept for embedding in offline mode, we don't care about the patch version since it should be compatible