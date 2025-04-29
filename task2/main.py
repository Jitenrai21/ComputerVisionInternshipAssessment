import cv2
import pandas as pd

# Loading the color names CSV (you can download a standard color list CSV)
# standard color list CSV downloaded from https://github.com/codebrainz/color-names/blob/master/output/colors.csv
csv_path = 'colors.csv'
colors_df = pd.read_csv(csv_path)
# giving column headers
colors_df.columns = ['name_id', 'color_name', 'hex', 'R', 'G', 'B']

# global variables
clicked = False
r = g = b = xpos = ypos = 0
color_name = ""

# Function to get the closest color name
def get_color_name(R, G, B):
    minimum = float('inf') #positive infinity as a floating-point
    cname = ""
    # Iterate through each color in the CSV
    for i in range(len(colors_df)):
        r_, g_, b_ = int(colors_df.loc[i, 'R']), int(colors_df.loc[i, 'G']), int(colors_df.loc[i, 'B'])
        d = abs(R - r_) + abs(G - g_) + abs(B - b_)
        if d < minimum:
            minimum = d
            cname = colors_df.iloc[i, 1]  # Column 1 has the actual color name
    return cname

# Mouse callback function
def draw_function(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked, color_name
    if event == cv2.EVENT_LBUTTONDOWN: # Left mouse button click
        clicked = True
        xpos, ypos = x, y
        b, g, r = frame[y, x]
        b, g, r = int(b), int(g), int(r)
        color_name = get_color_name(r, g, b)

# Open webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow('Webcam Feed')

#OpenCV's setMouseCallback() function for mouse events.
cv2.setMouseCallback('Webcam Feed', draw_function)

# Main loop to continuously capture webcam frames
while True:
    ret, frame = cap.read() # Read a frame from the webcam
    if not ret:
        break # If frame read fails, exit loop

    if clicked:
        # Display rectangle and text
        cv2.rectangle(frame, (20, 20), (600, 60), (b, g, r), -1)
        text = f'{color_name} R={r} G={g} B={b}'
        cv2.putText(frame, text, (30, 50), 2, 0.8, (255, 255, 255) if r + g + b < 400 else (0, 0, 0), 2)

    cv2.imshow('Webcam Feed', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
