import cv2

image1 = cv2.imread("Additional stuff/images/eyes.jpg")

grey = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(grey, 5)
edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9,9 )
#this defines the threshold values of the blue. we dont wantit to be fully blur, so we use mean blur to know the middle for the blur intensity, whilst the adaptive aspect will adapt to the image. Thresh Binary is a property of adaptive threshold. we use Binary because we are using the greyscaled version for the trade, which can be read in 1s and 0s.

coloured = cv2.bilateralFilter(edges, 9, 250, 250)
#bilaterial filter will add colour back to the image. 9 is the width and height of the threshold, and the two 250 is the width and height of the image
final = cv2.bitwise_and(coloured, coloured, mask = edges)
#this will add the two images together to give this the cartoon look

cv2.imshow("cartoon effect", final)

cv2.waitKey(0)
#it will hold the window until the user presses a key
cv2.destroyAllWindows()
#it will destroy all windows