# FPick

[![Release](https://github.com/coding-beagle/fpick/actions/workflows/release.yml/badge.svg)](https://github.com/coding-beagle/fpick/actions/workflows/release.yml)

FPick is a simple utility that allows users to access their OS file dialog from the CLI.

This is particularly useful for image / video browsing with scripts.

## Example usage

Running a python script that takes an image or video file as an output:

```
python some_script.py `fpick`
```

For those unfamiliar with terminal use (I.E. the primary target for this tool): 

```
# either way works
echo `fpick`  # the backticks are command substitution: the output of 'fpick' is passed as the argument to 'echo'
echo $(fpick) # more modern syntax for command substitution
```

![](./readme_resources/first_demo.gif)

Use the '-d' or '--directory' flags to return directories only:

![](./readme_resources/directory_demo.gif)

Use the '-f' or '--file_extension' flags to filter by file extension:

![](./readme_resources/filefilter_demo.gif)

## To create a release build:

```
git tag v0.1.0 && git push origin v0.1.0
```

Any tag starting with v and numerical version number should work (?)