from setuptools import setup, find_packages

setup(
    name="stock_sentiment_prediction",
    version="0.1.0",
    author="vivesh kumar singh",
    author_email="viveshsingh8797@gmail.com",
    description="A package for predicting stock market movement using subreddit sentiment analysis",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],  # This should be empty if you use requirements.txt
)