import cv2

# to load image
image = cv2.imread('image.jpg')

# to check if image is loaded
if image is None:
    raise FileNotFoundError("Image file not found. Please check the path.")

# to convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('output_grayscale.jpg', gray_image)

# applying Gaussian Blur
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
cv2.imwrite('output_blurred.jpg', blurred_image)

# detecting edges using Canny
edges = cv2.Canny(blurred_image, 50, 150)
cv2.imwrite('output_edges.jpg', edges)

print("All operations completed and outputs saved.")