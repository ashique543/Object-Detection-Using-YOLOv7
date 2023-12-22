# yolov7-object-tracking

### Steps to run Code
- Clone the repository.
```
git clone 
```
- Goto the cloned folder.
```
cd yolov7-object-tracking
```
- Create a virtual envirnoment (Recommended, If you dont want to disturb python packages)
```
### For Linux Users
python3 -m venv yolov7objtracking
source yolov7objtracking/bin/activate

### For Window Users
python3 -m venv yolov7objtracking
cd yolov7objtracking
cd Scripts
activate
cd ..
cd ..
```
- Upgrade pip with mentioned command below.
```
pip install --upgrade pip
```
- Install requirements with mentioned command below.
```
pip install -r requirements.txt
```
- Run the code with mentioned command below (by default, pretrained [yolov7](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt) weights will be automatically downloaded into the working directory if they don't already exist).
```
# for detection only
python detect.py --weights yolov7.pt --source "your video.mp4"

#if you want to change source file
python detect_and_track.py --weights yolov7.pt --source "your video.mp4"

#for WebCam
python detect_and_track.py --weights yolov7.pt --source 0

#for External Camera
python detect_and_track.py --weights yolov7.pt --source 1

#For LiveStream (Ip Stream URL Format i.e "rtsp://username:pass@ipaddress:portno/video/video.amp")
python detect_and_track.py --source "your IP Camera Stream URL" --device 0

#for specific class (person)
python detect_and_track.py --weights yolov7.pt --source "your video.mp4" --classes 0

#for colored tracks 
python detect_and_track.py --weights yolov7.pt --source "your video.mp4" --colored-trk

#for saving tracks centroid, track id and bbox coordinates
python detect_and_track.py --weights yolov7.pt --source "your video.mp4" --save-txt --save-bbox-dim
```

- Output file will be created in the ```working-dir/runs/detect/obj-tracking``` with original filename

- To check if the objects of a particular videos are moving 
```python moving_still.py``` 
Then you will be asked to enter the directories folder
Output will be given as a csv file with the name ```video-name.csv``` with original filename


### Results
<table>
  <tr>
    <td>YOLOv7 Detection Only</td>
    <td>YOLOv7 Object Tracking with ID</td>
    <td>YOLOv7 Object Tracking with ID and Label </td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/62513924/196107891-bb8124de-99c6-4039-b556-2ade403bd985.png"></td>
    <td><img src="https://user-images.githubusercontent.com/62513924/185798283-0455ce49-4359-4e52-8d69-fd30dd61c5b4.png"></td>
     <td><img src="https://user-images.githubusercontent.com/62513924/191241661-ed5b87eb-5c8c-49bc-8301-531ee86f3b38.png"></td>
  </tr>
 </table>

