from setuptools import setup, find_packages

setup(
    name='circuits',
    version='1.0.0',
    author="Samuel Marks, Can Rager, Eric J Michaud, Yonatan Belinkov, David Bau, Aaron Mueller wrapped by Daniel Karl I. Weidele",
    author_email="daniel.karl@ibm.com",
    description="Python Module for Feature Circuits",
    url="https://github.com/saprmarks/feature-circuits",
    python_requires='>=3.10',
    packages=["circuits"],
    install_requires=[
        "circuitsvis>=1.43.2",
        "datasets>=2.18.0",
        "einops>=0.7.0",
        "graphviz>=0.20.1",
        "matplotlib>=3.8.3",
        "nnsight==0.2.15",
        "numpy>=1.26.4",
        "pandas>=2.2.1",
        "plotly>=5.18.0",
        "torch>=2.1.2",
        "torchtyping>=0.1.4",
        "tqdm>=4.66.1",
        "zstandard>=0.22.0",
        "numpy<2.0",
        "dictionary_learning"
    ]
)
