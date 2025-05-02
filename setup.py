from distutils.core import setup

from hackwifi.config import Configuration

setup(
    name='hackwifi',
    version=Configuration.version,
    author='localexpert',
    author_email='localexpert000@gmail.com',
    url='https://github.com/localexpert000/hackwifi',
    packages=[
        'hackwifi',
        'hackwifi/attack',
        'hackwifi/model',
        'hackwifi/tools',
        'hackwifi/util',
    ],
    data_files=[
        ('share/dict', ['wordlist-top4800-probable.txt'])
    ],
    entry_points={
        'console_scripts': [
            'hackwifi = hackwifi.hackwifi:entry_point'
        ]
    },
    license='GNU GPLv2',
    scripts=['bin/hackwifi'],
    description='Wireless Network Auditor for Linux',
    #long_description=open('README.md').read(),
    long_description='''Wireless Network Auditor for Linux.

    Cracks WEP, WPA, and WPS encrypted networks.

    Depends on Aircrack-ng Suite, Tshark (from Wireshark), and various other external tools.''',
    classifiers = [
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ]
)
