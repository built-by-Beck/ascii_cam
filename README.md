# ASCII Camera

A real-time ASCII art generator built with Python, OpenCV, and Tkinter. This project captures live video from your webcam, processes it, and displays it as ASCII art in an interactive, resizable GUI.

This project combines creativity with technical skills, transforming a simple webcam feed into dynamic ASCII art using all characters from the alphabet and symbols. It’s an impressive showcase of Python programming, computer vision, and GUI design.

Here is what the program outputs: 

ABCD@@EFG@@HIJKLMNOPQRST@@@@UVWXY@ 
@@Z%%%%####@@@@@@@####@@@@@@#####@
@@ABCD@@@@@#############@@@@@@#### 
@@FGHIJKLMNOPQ@@@@@@@@@@@@####@@@@ 
@@RSTUVWXY@@@@@@##############@@@@


Imagine this updating in real time from your webcam feed!

## How It Works

1. **Frame Capture**: OpenCV captures video frames from your webcam.
2. **Grayscale Conversion**: Converts each frame into grayscale.
3. **ASCII Mapping**: Maps pixel intensity values to characters from the ASCII set (`ABCDEFGHIJKLMNOPQRSTUVWXYZ@%#*+=-:. `).
4. **Dynamic Rendering**: Displays the ASCII art in a resizable Tkinter GUI.

## Requirements

Make sure you have the following installed:

- **Python 3.8+**
- Required Python libraries:
  ```bash
  pip install opencv-python numpy pillow

**Clone the repository:**

```bash
git clone https://github.com/yourusername/ascii-camera.git
```

```bash
cd ascii-camera
```
- 
**Run the program:**

```bash
python ascii_camera.py
```

Resize or maximize the window to adjust the ASCII art resolution dynamically.
To exit, close the window or press Ctrl+C.

**Skills Demonstrated**

Python Programming: Efficient use of OpenCV, Tkinter, and Numpy libraries.
Real-Time Processing: Implementation of a smooth, live video-to-ASCII pipeline.
GUI Development: Responsive design with dynamic resizing and font scaling.
Performance Optimization: Real-time rendering with minimal computational overhead.

**Why This Project Matters**
This project bridges art and technology, providing a creative way to display live video. 


It demonstrates:

1. Advanced knowledge of Python libraries.
2. The ability to handle real-time data processing.
3. An understanding of graphical user interface design.

**Contributions**
Contributions are welcome! Fork this repository and submit a pull request with your improvements or bug fixes.


**License**
This project is licensed under the MIT License. See the LICENSE file for details.















