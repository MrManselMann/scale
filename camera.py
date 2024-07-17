import cv2
from graph import f
import audio as aud
lower = (100, 100, 100)
upper = (120, 255, 255)
cap = cv2.VideoCapture(0)
cY = 0
cX = 0
averageB = 0
counter = 0
counter2 = 0
numsB = 0
start = 0
movement = 0
movement1 = 0
movement2 = 0
units = {"pounds": False, "kilograms": True, "kilos": True, "kg": True, "kilo": True, "gram": True, "grams": True, "keys": True, "kgs": True}
unit_input = input("What unit would you like it to be in, Pounds or Kilograms: ").lower()
is_kilograms = units.get(unit_input)
print("kilograms = " + str(is_kilograms))
while True:
    ret, frame = cap.read()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsvImage, lower, upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(max_contour)

        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

        if counter == 0:
            aud.play_audio(r"C:\Users\jijoe.joseph\scale\numbers\placeObject.wav")
        
        movement1 = cX
        movement = movement1 - movement2
        movement2 = cX
        
        if counter >= 100 and movement == 0:
            averageB += cY
            numsB += 1
            counter2 += 1
    if cY - 20>= start:
        counter += 1
    if counter2 == 100:
        break
    key = cv2.waitKey(1) & 0xFF
    k = cv2.waitKey(33)
    if k==27: 
        break  
    if k==32: 
        counter += 50 
cap.release()
cv2.destroyAllWindows()
if numsB > 0:
    averageB /= numsB
prediction = f(averageB)
if is_kilograms:
    prediction *= 0.453592
print("height = " + str(averageB))    
prediction = round(float(prediction), 2)
print("prediction = " + str(prediction))
aud.say_num(prediction)
if is_kilograms:
    aud.play_audio(r"C:\Users\jijoe.joseph\scale\numbers\kilograms.wav")
else:
    aud.play_audio(r"C:\Users\jijoe.joseph\scale\numbers\pounds.wav")
