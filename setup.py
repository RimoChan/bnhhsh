import setuptools


setuptools.setup(
    name='bnhhsh',
    version='1.2.2',
    author='RimoChan',
    author_email='the@librian.net',
    description='bnhhsh',
    url='https://github.com/RimoChan/bnhhsh',
    packages=['bnhhsh'],
    package_data={
        'bnhhsh': ['data/色情词库.json', 'data/色情词库_数据增强.json', 'data/莉沫词库.json', 'data/常用汉字.json', 'data/现代汉语常用词表.json'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pypinyin>=0.42.0',
    ],
    python_requires='>=3.8',
)
