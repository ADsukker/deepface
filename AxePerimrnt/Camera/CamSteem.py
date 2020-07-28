"""
Example to introduce how to read a camera connected to your computer
"""

# Import the required packages
import cv2
import argparse
capture_Agnt = cv2.VideoCapture(0)

class CameraCV():
    """ All OpenCV features related to Cam"""
    _CameraIndex = 0
    # Get some properties of VideoCapture (frame width, frame height and frames per second (fps)):
     
     
    _frame_width = 640
    _frame_height = 480
    _fps = 30

    def __init__(self,CameraIndex = 0,*frame_width, frame_hight, FramePerSec ):
        _CameraIndex = CameraIndex
        _frame_width = frame_width
        _frame_height = frame_hight
        _fps = FramePerSec
        
    
    def Cam_Config(self, *args, **kwargs):
        # We first create the ArgumentParser object
        # The created object 'parser' will have the necessary information
        # to parse the command-line arguments into data types.
        
        parser = argparse.ArgumentParser()
        
        # We add 'index_camera' argument using add_argument() including a help.
        parser.add_argument("index_camera", help="index of the camera to read from", type=int)
        args = parser.parse_args()
        capture_Agnt = cv2.VideoCapture()

        # We create a VideoCapture object to read from the camera (pass 0):
        #ADS> capture = cv2.VideoCapture(args.index_camera)
        
    try:
        # Print these values:
        print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(_frame_width))
        print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(_frame_height))
        print("CAP_PROP_FPS : '{}'".format(_fps))
        capture_Agnt.open()
    
            
        #  pass
    except Exception as e:
        print("Error: Parsing provided Camera Arguments.\n Bodey: ['{}'].".format(e))
        pass

    else:
        
        print("Camera configuration completed.\n Bodey: [Frame[Hight = {}, Width = {}, FPS = {}  ]."
        .format(_frame_height,_frame_width, _fps))
        pass
     
    print(capture_Agnt.isOpened)
    Print("####### Process Started #######")
    Print(' Please press q to terminate')
    while capture_Agnt.isOpened():
      
        # Capture frame-by-frame from the camera
        ret, frame = capture_Agnt.read()

        if ret is True:
            # Display the captured frame:
            cv2.imshow('Input frame from the camera', frame)

            # Convert the frame captured from the camera to grayscale:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the grayscale frame:
            cv2.imshow('Grayscale input camera', gray_frame)
    
            # Press q on keyboard to exit the program
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        # Break the loop
        else:
            break
    
    # Release everything:
    capture_Agnt.release()
    cv2.destroyAllWindows()
    Print("####### TERMINATED #######")
    
pass

 
 

 