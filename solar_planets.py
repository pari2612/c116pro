import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(img,
             "Sun",
             (125,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255),
            )

cv2.putText(img,
             "Mercury",
             (130,150),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255),
            )

cv2.putText(img,
             "Venus",
             (200,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255),
            )

cv2.putText(img,
             "Earth",
             (250,150),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255),
            )

cv2.putText(img,
             "Mars",
             (380,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255),
            )

cv2.putText(img,
             "Jupiter",
             (460,50),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255),
            )


cv2.putText(img,
             "Saturn",
             (750,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255),
            )

cv2.putText(img,
             "Uranus",
             (900,150),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255),
            )

cv2.putText(img,
             "Neptune",
             (1050,300),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255),
            )
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.imwrite("Solar_system_with_name.jpg",img)
 