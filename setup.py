from setuptools import setup, find_packages

setup(
    # Set the package name
    name='EmotionDetection',
    
    version='0.1.0',
    
    # Use find_packages() to automatically detect directories 
    # that contain an __init__.py file (like EmotionDetection/)
    packages=find_packages(),
    
    # List the required external libraries
    install_requires=[
        'requests',
    ],
    
    description='A package for detecting emotions in text using a network service.',
    # ... (other metadata like author, license, etc., remains the same)
)