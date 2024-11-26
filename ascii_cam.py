import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

# Gray scale levels
gscale1 = "$#@)*^($^&#@#%22BECKDAVIDBECK22]**^%$$^(*&*(^%&^%)BUILT_BY_BECK^(*)&(*^%^^*&%%*&^&*)*&"
gscale2 = "@%#*+=-:. "

def get_average_l(image):
    """Given a grayscale image, return the average luminance."""
    im = np.array(image)
    return np.average(im)

def convert_frame_to_ascii(frame, cols=120, scale=0.75, more_levels=False):
    """
    Convert a video frame to ASCII art.
    """
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Get dimensions
    height, width = gray.shape
    tile_width = width / cols
    tile_height = tile_width / scale
    rows = int(height / tile_height)

    # Ensure rows and cols fit the image dimensions
    if cols > width or rows > height:
        raise ValueError("Image too small for specified cols!")

    # Prepare ASCII image
    ascii_art = []
    for row in range(rows):
        y1 = int(row * tile_height)
        y2 = int((row + 1) * tile_height)
        if row == rows - 1:
            y2 = height

        line = ""
        for col in range(cols):
            x1 = int(col * tile_width)
            x2 = int((col + 1) * tile_width)
            if col == cols - 1:
                x2 = width

            # Crop image tile and compute average luminance
            tile = gray[y1:y2, x1:x2]
            avg_luminance = int(np.mean(tile))

            # Choose gray scale value
            if more_levels:
                gsval = gscale1[int((avg_luminance * 69) / 255)]
            else:
                gsval = gscale2[int((avg_luminance * 9) / 255)]

            line += gsval
        ascii_art.append(line)

    return "\n".join(ascii_art)

class ASCIICameraApp:
    def __init__(self, root, cols=120, scale=0.55, more_levels=False):
        self.root = root
        self.cols = cols
        self.scale = scale
        self.more_levels = more_levels

        # Initialize camera
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Could not access the camera.")
            self.root.destroy()
            return

        # Create a text widget for ASCII output
        self.text_widget = tk.Text(
            root, font=("Courier", 5), bg="black", fg="white", spacing3=0
        )
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        # Start updating frames
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            try:
                # Convert the frame to ASCII
                ascii_art = convert_frame_to_ascii(frame, cols=self.cols, scale=self.scale, more_levels=self.more_levels)
                # Display in the text widget
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, ascii_art)
            except Exception as e:
                print(f"Error processing frame: {e}")

        # Schedule the next frame update
        self.root.after(33, self.update_frame)  # ~30 FPS

    def on_close(self):
        self.cap.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("High-Quality ASCII Camera")
    app = ASCIICameraApp(root, cols=120, scale=0.55, more_levels=True)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
