import importlib
import sys

print('Trying importlib.import_module("cv2")')
cv = importlib.import_module('cv2')
print('cv module file:', getattr(cv, '__file__', 'missing'))
print('Has CascadeClassifier in cv?:', 'CascadeClassifier' in dir(cv))

try:
    print('\nTrying import cv2.cv2...')
    cv2native = importlib.import_module('cv2.cv2')
    print('cv2.cv2 file:', getattr(cv2native, '__file__', 'missing'))
    print('Has CascadeClassifier in cv2native?:', 'CascadeClassifier' in dir(cv2native))
    sample = [n for n in dir(cv2native) if 'Cascade' in n or n.startswith('Video')][:40]
    print('Sample attrs in native module:', sample)
except Exception as e:
    print('import cv2.cv2 failed:', e)

print('\nsys.modules keys for cv2*:', [k for k in sys.modules.keys() if k.startswith('cv2')])
