import os
import csv
import random

def read_object_info(frame_path):
    # Read object information from the TXT file
    object_info = []
    with open(frame_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            object_id = int(parts[0])
            x1, y1, x2, y2 = map(float, parts[1:])
            average_x =(x1 + x2) / 2
            average_y =(y1 + y2) / 2
            #print(average_x,average_y)
            object_info.append((object_id, average_x, average_y))
    return object_info

def classify_objects(frames_folder):
    # List all frame files in the folder
    frame_files = sorted([f for f in os.listdir(frames_folder) if f.endswith('.txt')])

    # Collect all object IDs in the video
    all_object_ids = set()

    csv_file_name = ''
    for a in frame_files[0]:
        if (a!='_'):
            csv_file_name = csv_file_name+a
        else:
            break
    csv_file_name = csv_file_name+'.csv'
    # Initialize CSV writer
    with open(csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['ObjectID', 'Status'])

        # Process each frame
        for frame_file in frame_files:
            frame_path = os.path.join(frames_folder, frame_file)
            current_objects = read_object_info(frame_path)

            # Collect all object IDs
            all_object_ids.update(obj[0] for obj in current_objects)

        # Compare objects across frames
        # if (frame_file[len(frame_file) - 5:] == '1.txt'):
            
        
        previous_objects = None
        for object_id in sorted(all_object_ids):
            # Initialize status for each object
            # object_status = {'ObjectID': object_id, 'Status': 'Still'}

            # Find the object in the previous frame
            previous_obj = next((obj for obj in previous_objects if obj[0] == object_id), None) if previous_objects else None

            # Find the object in the current frame
            current_obj = next((obj for obj in current_objects if obj[0] == object_id), None)

            # Compare average IDs
            if previous_obj and current_obj and (previous_obj[1], previous_obj[2]) == (current_obj[1], current_obj[2]):
                x = 'Still'
            else:
                x = 'Moving'

            object_status = {'ObjectID': object_id, 'Status': x}
            # object_status['Status'] = 'Moving'

            # Write results to CSV only once for the entire video
            if frame_file == frame_files[-1]:
                csv_writer.writerow([object_id,x])

            previous_objects = current_objects

if __name__ == '__main__':
    # Replace 'frames_folder' with the path to your frame TXT files folder
    str = input("Enter the path where coordinates are saved - ")
    frames_folder = str

    # Classify objects and save results to CSV
    classify_objects(frames_folder)

    print("Results saved as csv file")
