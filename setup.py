import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tradingview_ta',
    version='3.1.6',
    description="A python module to get TradingView's technical analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/deathlyface/python-tradingview-ta',
    author='deathlyface',
    author_email='bri4nong@gmail.com',
    packages=['tradingview_ta'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'requests',
    ],
    python_requires='>=3.5')
