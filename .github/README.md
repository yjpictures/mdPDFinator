# Markdown to PDF Converter CLI

![GitHub Actions Badge](https://github.com/yjpictures/mdPDFinator/actions/workflows/release-binaries.yml/badge.svg?branch=stable)

Convert your Markdown files to PDF from the command line with ease. This cross-platform command-line tool supports Linux, macOS, and Windows.



## Features

- Convert Markdown files to PDF.
- Cross-platform support (Linux, macOS, Windows).
- Customizable output file names and styles.
- Option for custom new page characters.
- Fast and efficient conversion.
- Command-line interface for easy automation.



## Installation

### Install [weasyprint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation):
1. Windows - [Download](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/latest) the installer and install with default options
1. Ubuntu - `apt install weasyprint`
1. macOS - `brew install weasyprint`



### Install mdPDFinator

1. [Download](https://github.com/yjpictures/mdPDFinator/releases/latest) the latest version from the releases for your OS type
1. Rename the binary file to `mdPDFinator` (`mdPDFinator.exe` for Windows)
1. Windows binary is already an execuatable but for Linux or macOS you need to run `chmod 775 mdPDFinator` to make the binary execuatable.



## Usage

To convert a Markdown file to PDF, use the following command:

```bash
./mdPDFinator input.md
```

Replace input.md with the path to your Markdown file. You can customize the output style and format using various options (see [Options](#options)).



## Options

`-o`, `--output_file_path <file>`: Default: 'output.pdf'. Path to the output PDF file (it will not create a folder for you, make sure directory already exists).

`-n`, `--new_page_char <char>`: Default: '---'. Character for new page break.

`-s`, `--style_file_path <style>`: Path to the CSS file.

`-h`, `--help`: Display usage information.



## Examples

Basic conversion:

```bash
./mdPDFinator input.md
```

Using a custom output:
```bash
./mdPDFinator input.md -o custom_output.pdf
```

Using a custom output and style:
```bash
./mdPDFinator input.md -o custom_output.pdf -s my-style.css
```

Using a custom new line char:
```bash
./mdPDFinator input.md -n -+-+-+-
```



## Troubleshooting

### weasyprint errors

If weasyprint is not installed on your system you might see the following error, try to go through the mentioned links in the error to resolve the issues.

```
WeasyPrint could not import some external libraries. Please carefully follow the installation steps before reporting an issue:
https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation
https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#troubleshooting 
```

### CLI `--` errors

We utilize Google's Python Fire CLI tool in our project. If your input includes the double hyphen `--`, you may encounter difficulties when attempting to ensure the tool functions correctly.

Read more about it here:
- https://google.github.io/python-fire/guide/#using-fire-flags
- https://google.github.io/python-fire/using-cli/#-separator-changing-the-separator

You could even use the [interactive mode](https://google.github.io/python-fire/using-cli/#-interactive-interactive-mode) to enter such outputs.



## Limitations

The mdPDFinator is a versatile tool designed to convert Markdown files to PDF on various platforms. However, there are certain limitations and compatibility considerations that users should be aware of:

### 1. Supported Operating Systems

The Markdown to PDF Converter CLI is officially supported on the following operating systems:
- Ubuntu 20.04 and above
- Windows 2019 and above
- macOS 11 and above

While the application is expected to work on other Linux distributions and macOS versions, as well as Windows versions not listed above, we do not provide official support for these platforms. Users on unsupported platforms may experience compatibility issues, and we recommend using one of the officially supported systems for the best experience.

### 2. Unverified Compatibility

The Markdown to PDF Converter CLI might work on other operating systems or versions that are not officially listed in the supported operating systems section. However, we have not tested the application on all possible configurations, so we cannot guarantee full compatibility or functionality. Users on non-standard platforms should be aware that they might encounter issues related to system dependencies or libraries that we have not accounted for in our testing.

### 3. Limited Official Support

As an open-source project, the level of support we can provide is limited. While we aim to address issues and feature requests as they are reported, response times and issue resolutions may vary. We encourage users to contribute to the project by reporting issues and submitting pull requests to improve compatibility on different platforms.

### 4. Continuous Improvement

We are actively working to expand the list of officially supported platforms and improve compatibility across different operating systems and versions. Users are encouraged to check for updates and releases that may include expanded compatibility.

Please be aware of these limitations and compatibility considerations when using the Markdown to PDF Converter CLI on your specific platform. If you encounter issues or have suggestions for improving compatibility, please feel free to reach out or contribute to the project's development. Your feedback is valuable to us and the broader community of users.



## Developing

This python project has been setup poetry.

### First time dev setup

This will create and activate the virtual environment - `poetry shell`

This will install all development dependencies - `poetry install`

```bash
poetry shell
poetry install
```

### Running the project

If you are in the poetry shell use `python mdPDFinator.py`

Otherwise, use `poetry run python mdPDFinator.py`

```bash
python mdPDFinator.py
```

### How to add packages

```bash
poetry add <package>
poetry add <package> --group prod
```

### How to remove packages

```bash
poetry remove <package>
```



## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](https://github.com/yjpictures/mdPDFinator/blob/beta/LICENSE) file for details.
