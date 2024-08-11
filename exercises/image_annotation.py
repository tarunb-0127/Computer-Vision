import cv2

# Load the original image
original_image = cv2.imread('tesla.jpg')

# Make a copy for annotation
annotated_image = original_image.copy()

# Add text annotation to the annotated image
text = "Object"
position = (50, 50)  # Coordinates for text placement
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (0, 255, 0)  # Text color in BGR
thickness = 2
cv2.putText(annotated_image, text, position, font, font_scale, color, thickness)

# Concatenate the original and annotated images horizontally
combined_image = cv2.hconcat([original_image, annotated_image])

# Display the combined image
cv2.imshow('Original vs Annotated Image', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
