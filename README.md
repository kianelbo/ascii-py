# ASCIIpy
Simple ASCII art generator from image files
<p align="center">
  <img src="sample.jpg" width="60%" height="60%">
</p>

## How to Use
```python3
from asciipy.ascii_art import AsciiArt

pic = AsciiArt(image_path).to_image(color=True)
pic.save("out.jpg")
```

Or run the program as module:
```bash
[python -m] asciipy --input "sample.jpg"
```

| Switch        | Description          |
|:------------- |:--------------------:|
| --input       | input file           |
| --color       | color/greyscale      |
| --resolution  | output resolution    |
| --txt         | print as text        |
| --output 	    | output file name     |
