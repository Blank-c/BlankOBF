# BlankOBF (Version 2)

**BlankOBF** is a tool designed to obfuscate Python programs, making them more challenging to understand for casual user. Please note that while obfuscation can deter casual users, determined individuals can still reverse engineer the code with effort. It's essential to understand that obfuscation does not provide security but rather adds a layer of complexity.

## Features
- **Python Obfuscation:** BlankOBF utilizes techniques to obscure Python code, making it less readable to human eyes.
- **Customization:** Offers various options to customize the obfuscation process, such as recursive obfuscation and inclusion of imports.
- **Command-line Interface:** Convenient command-line interface for easy integration into your development workflow.

## Usage
### From command line:
```bash
python BlankOBFv2.py [-h] --input PATH [--output PATH] [--recursive N] [--include_imports]
```
- **-h, --help:** Show the help message and exit.
- **--input PATH:** Specify the input file to be obfuscated.
- **--output PATH:** Optional flag to specify the output filename for the obfuscated code.
- **--recursive N:** Optional flag to specify the depth of recursive obfuscation (default is 1).
- **--include_imports:** Optional flag to include imports in the obfuscated file.

### From code:
```python
from BlankOBFv2 import BlankOBFv2

# Your Python code to obfuscate
code_to_obfuscate = """
def hello_world():
    print("Hello, world!")

hello_world()
"""

# Instantiate BlankOBFv2 with your code
obfuscator = BlankOBFv2(code=code_to_obfuscate, include_imports=False, recursion=1)

# Obfuscate the code
obfuscated_code = obfuscator.obfuscate()

# Print or use the obfuscated code as needed
print(obfuscated_code)

```

## Note
Keep in mind that while obfuscation can add a layer of complexity to your code, it's not a substitute for proper security measures. Always implement robust security practices to protect your intellectual property and sensitive data.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
