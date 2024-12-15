# Text Reverser

**Text Reverser** is a simple command-line utility that takes a string as input and reverses it character by character. This package is created for educational purposes and demonstrates packaging with Conda and setuptools.

## Installation

To install this package, use `conda-build` and install it locally:

```bash
conda-build .
conda install --use-local text_reverser
```

## Usage

Once installed, you can use the `text-reverser` command to reverse input text.

### Example:

**Input**:
```bash
text-reverser "Iain Amos is a Queen"
```

**Output**:
```
neeuQ a si somA niaI
```

## Requirements

- Python >= 3.6
- Conda (for building and installing)

## Author

Created by **Iain Amos Melchizedek**  
Email: [iainamos@outlook.com](mailto:iainamos@outlook.com)  
GitHub: [IainAmosMelchizedek](https://github.com/IainAmosMelchizedek)

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

### Educational Purpose

This project is designed to help learners understand how to:
1. Create a Python script.
2. Package it with Conda.
3. Use `setuptools` for Python package management.
