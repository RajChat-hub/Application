# RCXProj

![RCXProj Logo](https://via.placeholder.com/150)  <!-- Replace with your logo or relevant image -->

**RCXProj** is a project management tool designed to simplify the build process for C++ projects. It mimics the functionality of Visual Studio's Vcxproj files while providing a command-line interface for ease of use. With RCXProj, you can easily compile, build, and manage your projects in a structured and efficient manner.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Building a Project](#building-a-project)
  - [Running a Project](#running-a-project)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Easy Compilation**: Compile C++ source files effortlessly using a simple command-line interface.
- **Directory Management**: Automatically creates necessary directories (`bin` and `build`) for your project outputs.
- **Project Structure**: Organizes project files in a clear and concise manner, making it easier to navigate.
- **Test Support**: Built-in support for unit testing to ensure your code functions correctly.
- **Customizable Templates**: Use default templates for creating new RCXProj files.

---

## Installation

To install RCXProj, you need Python and pip installed on your system. Then, you can clone the repository and install the package:

```bash
git clone https://github.com/yourusername/rcxproj.git
cd rcxproj
pip install .

Alternatively, you can install it directly from PyPI:

bash
pip install rcxproj

Usage
Building a Project
To build a project, navigate to your project directory and run the following command:

bash
rcx build --file project.rcxproj

This command will compile your sources and generate the output files in the specified directories.

Running a Project
Once your project is built, you can run the output executable from the bin directory:

bash
./bin/main.out

On Windows, use:

bash
.\bin\main.out

Project Structure
Here’s an overview of the RCXProj project structure:

/rcxproj-system/
├── rcxproj/
│   ├── __init__.py
│   ├── parser.py
│   ├── builder.py
│   ├── cli.py
│   ├── utils.py
│   └── templates/
│       └── default.rcxproj
├── src/
│   ├── main.cpp
│   ├── utils.cpp
│   └── utils.h
├── project.rcxproj
├── build/
├── bin/
├── tests/
│   ├── test_parser.py
│   ├── test_builder.py
│   └── test_cli.py
├── README.md
├── requirements.txt
└── setup.py

Contributing
We welcome contributions! To contribute to RCXProj, please follow these steps:

Fork the repository.
Create a new branch for your feature or fix.
Make your changes and commit them.
Push your branch and open a pull request.
For more details, please refer to our CONTRIBUTING.md.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For questions or support, please contact:

Rajdeep Chatterjee
Email: rc9775295@gmail.com
GitHub Profile: https://github.com/RajChat-hub
