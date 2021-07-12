import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tradingview_ta',
    version='3.2.6',
    description="Unofficial TradingView technical analysis API wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/brian-the-dev/python-tradingview-ta',
    author='deathlyface',
    author_email='brian@brianthe.dev',
    packages=['tradingview_ta'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'requests',
    ],
    python_requires='>=3.5',
    project_urls={
        'Demo': 'https://tradingview.brianthe.dev',
        'Documentation': 'https://python-tradingview-ta.readthedocs.io',
        'Source': 'https://github.com/brian-the-dev/python-tradingview-ta',
    },
)
