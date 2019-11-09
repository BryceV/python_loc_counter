# python-loc-counter

The python-loc-counter module was built to count various LOC metrics:
- source_loc (Everything thats not a comment or blank line)
- single_comment_loc (Comments with the pound key)
- single_docstring_loc (Docstrings with single quotes)
- double_docstring_loc (Docstrings with double quotes)
- total_comments_loc (single_comment_loc + single_docstring_loc + double_docstring_loc)
- blank_loc (Any whitespace designated only with string.whitespace)
- total_line_count (Typical line count)

This uses extensive regex to try to cover weird edge cases, like comments in the middle of a src line (I recommend a quick review about how comments are decidely handled in tests/randomFile.txt). This is written entirely in python with no dependencies outside the standard library. Made to be used as a library.

### Installation
This package is locted on [github](https://github.com/BryceV/python_loc_counter) and [pypi](https://pypi.org/project/python-loc-counter/). If you have pip installed the easiest way to install is:

```sh
$ pip install python-loc-counter
```

### Example Usage

```sh
from python_loc_counter import LOCCounter

def main():
    counter = LOCCounter(<file_name>)
    loc_data = counter.getLOC()
    print(loc_data)
```

This will print a dictionary that might look something like:
```sh
{
    total_src_loc:1757
    total_single_comments_loc:75
    total_single_docstrings_loc:0
    total_double_docstrings_loc:179
    total_blank_loc:516
    total_comments_loc:254
    total_line_count:2530
}
```

### Development
See a feature or found a bug? Feel free to make suggestions or (better yet) contributions for future iterations!
   
### Example Projects
- Originally this module was built for: https://github.com/bcdasilv/code-style-mining/tree/python_analysis.
