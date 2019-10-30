from pynput.mouse import Button, Controller
from pynput.keyboard import KeyCode, Key
from pynput import keyboard
from PIL import ImageGrab
import argparse, time, cv2
import numpy as np

get_coordinates=Key.space
quit=KeyCode(char='q')

black, white = 0, 255
delay=0.0000001
tmp='tmp.png'

def paint(i, j, m):
	m.position=(i, j)
	m.press(Button.left)
	m.release(Button.left)
	time.sleep(delay)
	
def on_press(key):
	global new_image_start
	
	# Print pointer position if the spacebar is pressed
	if(key==get_coordinates):
		new_image_start=mouse_c.position
		keyboard_listener.stop()
	
	# Exit the program if the 'q' key is pressed
	elif(key==quit):
		exit()

def get_dist(a, b):
	return np.sqrt(abs(a[0]-b[0])**2 + abs(a[1]-b[1])**2)
	
# Main function
global new_image_start

# Structure responsible for the coordination of the parameters of the program
parser=argparse.ArgumentParser(description='Redraws an image from the clipboard to the https://skribbl.io/ canvas')

args=parser.parse_args()

# Read image from clipboard
print('[+] Reading image from clipboard and converting it to grayscale... ', end='')
try:
	im=ImageGrab.grabclipboard()
	im.save(tmp, 'PNG')
	src=cv2.imread(tmp, cv2.IMREAD_GRAYSCALE)
	print('ok.')
	print('[!] Image is %d x %d pixels.' % (src.shape[0], src.shape[1]))
except:
	print('error.')
	print('[!] Image not found on clipboard')
	exit()

# Set threshold and max value
thresh=128
max_value=255

# Basic threshold example
print('[+] Generating the thresholded image... ', end='', flush=True)
th, dst = cv2.threshold(src, thresh, max_value, cv2.THRESH_BINARY)
print('ok.')

# Controller to the mouse
print('[!] Hover the cursor over the position that you wish to redraw the image and press the spacebar.')
mouse_c=Controller()

# Read pointer position
with keyboard.Listener(on_press=on_press) as keyboard_listener:
	keyboard_listener.join()

bpx=[]
aux=np.where(dst==black)

for i in range(len(aux[0])):
	bpx.append([aux[1][i], aux[0][i]])
	
# Redraw the image
o=bpx[0]
print('[+] Redrawing the image... ', end='', flush=True)
paint(o[0]+new_image_start[0], o[1]+new_image_start[1], mouse_c)
bpx.remove(o)

j=0
print(len(bpx))
while(len(bpx)>0):
	# This factor must vary according to the number of black pixels to be painted
	if(j%5==0):
		or_dist, un_dist = [], []
		
		for i in bpx:
			or_dist.append(get_dist(o, i))
			un_dist.append(get_dist(o, i))

		or_dist.sort()
	j+=1
	
	o=bpx[un_dist.index(or_dist[0])]
	paint(o[0]+new_image_start[0], o[1]+new_image_start[1], mouse_c)
	
	bpx.remove(o)
	un_dist.remove(un_dist[un_dist.index(or_dist[0])])
	or_dist.remove(or_dist[0])

print('ok.')