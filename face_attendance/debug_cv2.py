import cv2
import sys
import inspect

print('cv2 file:', getattr(cv2, '__file__', 'missing'))
print('has CascadeClassifier:', 'CascadeClassifier' in dir(cv2))
print('cv2 version:', getattr(cv2, '__version__', 'unknown'))
print('\nFirst 10 entries in sys.path:')
for p in sys.path[:10]:
    print(p)

# show if there is a local cv2 module
try:
    import importlib.util
    spec = importlib.util.find_spec('cv2')
    print('\nimportlib spec for cv2:')
    print(spec)
except Exception as e:
    print('spec error:', e)

print('\nDir cv2 (sample):', [n for n in dir(cv2) if 'Cascade' in n or n.startswith('Video')][:40])
