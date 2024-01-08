# Image Optimization Script with Pillow

## Overview

Welcome to the Image Optimization Script with Pillow! This Python script is designed to streamline the process of resizing and compressing images using the powerful Pillow library. Whether you're a digital nomad or a web developer, this tool simplifies the optimization of your image assets, ensuring a balance between quality and performance.

## Features

1. **Configuration Flexibility**: The script employs a JSON configuration file (`config.json`) to store and manage input and output folder paths. This offers flexibility and ease of customization, ensuring a smooth user experience.

2. **Dependency Management**: The script utilizes the Pillow library for image processing. To install the required dependencies, run the following command:
```bash
pip install Pillow
```

3. **User-Friendly Interaction**: The script guides users through a series of prompts, allowing them to specify input and output paths, image dimensions for resizing, and the desired compression percentage. This ensures an interactive and user-friendly workflow.

4. **Quality Control**: Users can fine-tune the quality of image compression by adjusting the quality parameter, providing a balance between file size and visual fidelity. This feature is particularly useful when optimizing images for web applications.

5. **Backup Considerations**: A gentle reminder: the script modifies images in the specified input folder by creating an optimized version in a subfolder named `img-optimize`. It is advisable to maintain a backup of original images, especially if irreversible changes are a concern.

## Getting Started

### Installation

Ensure that you have Python installed on your system. (https://www.python.org/downloads/) Install the required dependencies by running:
```bash
pip install Pillow
```

### Execution

Run the script using the following command:
```bash
python compress_images.py
```


### Follow the Prompts

The script will prompt you to provide necessary information, including input and output paths, resizing options, and compression quality. Follow the prompts for a customized image optimization experience.

## Contributors

- Benjamin - [GitHub]([https://github.com/benjamin](https://github.com/Ben695))

## License

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to the open-source community and contributors to the Pillow library, making image processing in Python accessible and efficient.

Feel free to explore and enhance the capabilities of this script according to your needs. Happy optimizing!

