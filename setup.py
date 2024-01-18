from setuptools import setup

if __name__ == '__main__':
    long_description = open('README.md').read()
    setup(
        name='pgn2fixture',
        version='1.0.4',
        description='A very simple PGN to Django fixture converter.',
        author='Josias Alvarado',
        author_email='josiasjag@gmail.com',
        url='https://josias-alvarado.me',
        packages=[
            'pgn2fixture',
            ],
        license='MIT',
        long_description=long_description,
        long_description_content_type='text/markdown',
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Operating System :: OS Independent',
            'Topic :: Software Development',
            'Topic :: Games/Entertainment :: Board Games',
            'Intended Audience :: Developers',
            'Development Status :: 3 - Alpha',
            ],
        )
