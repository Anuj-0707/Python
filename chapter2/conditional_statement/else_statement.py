light = input("Enter the colour of light : ")
light=light.capitalize()
if(light=="Red"):
    print("stop")
elif(light=="Green"):
    print("Go")
elif(light=="Yellow"):
    print("Wait") # spacing in python is called indentation
else:
    print("Light is not working")