import bluetooth
import RPi.GPIO as GPIO   #calling for header file which helps in using GPIOs of PI
BULB=21
GPIO.setmode(GPIO.BCM)    #programming the GPIO by BCM pin numbers. (like PIN40 as GPIO21)
GPIO.setwarnings(False)
GPIO.setup(BULB,GPIO.OUT)  #initialize GPIO21 (Relay connected at this pin) as an output Pin
GPIO.output(BULB,0)
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 1
server_socket.bind(("",port))
server_socket.listen(1);
client_socket,address = server_socket.accept();
print ("Accepted connection from ",address);
while (1):
data = client_socket.recv(1024);
print ("Received: %s", %data);
if (data == "0"):  #if '0' is sent from the Android App, turn OFF the CFL bulb
print ("AC light OFF");
GPIO.output(BULB,0)
if (data == "1"):  #if '1' is sent from the Android App, turn OFF the CFL bulb
print("AC light ON")
GPIO.output(BULB,1)
if (data == "q"):
print ("Quit")
break
client_socket.close()
server_socket.close()