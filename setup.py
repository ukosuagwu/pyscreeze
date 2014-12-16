from setuptools import setup


setup(
    name='PyScreeze',
    version='0.1.4',
    url='https://github.com/asweigart/pyscreeze',
    author='Al Sweigart',
    author_email='al@inventwithpython.com',
    description='A simple, cross-platform screenshot module for Python 2 and 3.',
    license='BSD',
    packages=['pyscreeze'],
    test_suite='tests',
    install_requires=['Pillow'],
    keywords="screenshot screen screencap capture scrot screencapture image",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)