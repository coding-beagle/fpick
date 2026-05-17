# FPick

FPick is a simple utility that allows users to access their OS file dialog from the CLI.

This is particularly useful for image / video browsing with scripts.

## Example usage

Running a python script that takes an image or video file as an output:

```
python some_script.py `fpick`
```

![](./readme_resources/first_demo.gif)

Use the '-d' or '--directory' flags to return directories only:

![](./readme_resources/directory_demo.gif)

Use the '-f' or '--file_extension' flags to filter by file extension:

![](./readme_resources/filefilter_demo.gif)