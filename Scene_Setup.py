import maya.cmds as cmds
import maya.OpenMayaUI as mui
import shiboken2

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

def maya_window():
    from maya.OpenMayaUI import MQtUtil
    import shiboken2
    return shiboken2.wrapInstance(int(MQtUtil.mainWindow()), QMainWindow)

# Set the start and end frames    
def set_playback_options(start_frame, end_frame):
    cmds.playbackOptions(minTime=start_frame, maxTime=end_frame, animationStartTime=start_frame, animationEndTime=end_frame)

#create camera
def set_camera():
    camera = cmds.camera(centerOfInterest=5, focalLength=150, overscan=1, aspectRatio=1.78, filmFit=3, displayFilmGate=True)
    
#transform keys in step mode
def set_step_mode():
    tangent_type = "step"
    cmds.keyTangent(ott=tangent_type)
    
#render settings
def set_render_settings():
    width = 1920
    height = 1080

    # Set the render resolution in the render settings
    cmds.setAttr("defaultResolution.width", width)
    cmds.setAttr("defaultResolution.height", height)

    # Set the device aspect ratio to match the resolution
    aspect_ratio = float(width) / float(height)
    cmds.setAttr("defaultResolution.deviceAspectRatio", aspect_ratio)
                   
#playback settings
def set_playback_speed_and_fps():
    # Set the playback speed
    cmds.playbackOptions(playbackSpeed=1, maxPlaybackSpeed=1)
    cmds.currentUnit(time='film')
 

#playblast settings
def set_playblast():
    # Set the playblast format
    cmds.playblast(fmt="qt",compression="H.264", p=100, orn=1, v=1, wh=[1920,1080])
 
# We create a simple window with a QWidget
window = QMainWindow()
window.setWindowTitle('Set Scene')

central = QWidget()
window.setCentralWidget(central)

vertical = QVBoxLayout()
central.setLayout(vertical)

# Create a vertical line with text
layout = QVBoxLayout()
line_label_1 = QLabel("Setup animation playback 150 frames")
line_1 = QFrame()
line_1.setFrameShape(QFrame.HLine)
vertical.addWidget(line_label_1)

# Set a background color to highlight the line
line_label_1.setStyleSheet("background-color: dark gray")

button1 = QPushButton('Playback 150')
vertical.addWidget(button1)

layout = QVBoxLayout()
line_label_2 = QLabel("Setup camera Focal Length, Film Aspect ratio and Display Film Gate")
line_2 = QFrame()
line_2.setFrameShape(QFrame.HLine)
vertical.addWidget(line_label_2)

# Set a background color to highlight the line
line_label_2.setStyleSheet("background-color: dark gray")

button2 = QPushButton('Setup Camera')
vertical.addWidget(button2)

layout = QVBoxLayout()
line_label_3 = QLabel("Transform keys into Step mode")
line_3 = QFrame()
line_3.setFrameShape(QFrame.HLine)
vertical.addWidget(line_label_3)

# Set a background color to highlight the line
line_label_3.setStyleSheet("background-color: dark gray")

button3 = QPushButton('Step MODE')
vertical.addWidget(button3)

layout = QVBoxLayout()
line_label_4 = QLabel("Setup Image size 1920*1080 and Device aspect ratio 1.778")
line_4 = QFrame()
line_4.setFrameShape(QFrame.HLine)
vertical.addWidget(line_label_4)

# Set a background color to highlight the line
line_label_4.setStyleSheet("background-color: dark gray")

button4 = QPushButton('Render Settings')
vertical.addWidget(button4)

layout = QVBoxLayout()
line_label_5 = QLabel("Setup Framerate and playback speed in Preferences")
line_5 = QFrame()
line_5.setFrameShape(QFrame.HLine)
vertical.addWidget(line_label_5)

# Set a background color to highlight the line
line_label_5.setStyleSheet("background-color: dark gray")

button5 = QPushButton('Framerate 24fps')
vertical.addWidget(button5)

layout = QVBoxLayout()
line_label_6 = QLabel("Run 1920*1080 .mov playblast. REMEMBER to click on the right viewport and save the video in the right folder!!!")
line_6 = QFrame()
line_6.setFrameShape(QFrame.HLine)
vertical.addWidget(line_label_6)

# Set a background color to highlight the line
line_label_6.setStyleSheet("background-color: dark gray")

button6 = QPushButton('Playblast an Animation')
vertical.addWidget(button6)

window.resize(500, 500)

#connect logic & UI
button1.clicked.connect(lambda:set_playback_options(1, 150))
button2.clicked.connect(set_camera)
button3.clicked.connect(set_step_mode)
button4.clicked.connect(set_render_settings)
button5.clicked.connect(set_playback_speed_and_fps)
button6.clicked.connect(set_playblast)
window.show()


