import tkinter as tk
from tkinter import ttk
import mysql.connector
import face_recognition
import cv2
import numpy as np
import pickle
import threading

class DetectCriminals:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Criminal Details")

        self.tree = ttk.Treeview(self.root, columns=("Name", "Type", "Description"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Description", text="Description")
        self.tree.column("Name", width=150)
        self.tree.column("Type", width=100)
        self.tree.column("Description", width=200)
        self.tree.pack(expand=True, fill="both")

        self.known_face_encodings = []
        self.known_face_names = []

        with open("ref_name.pkl", "rb") as f:
            ref_dict = pickle.load(f)

        with open("ref_embed.pkl", "rb") as f:
            embed_dict = pickle.load(f)

        for ref_id, embed_list in embed_dict.items():
            for embed in embed_list:
                self.known_face_encodings.append(embed)
                self.known_face_names.append(ref_id)

    def update_treeview(self, name):
        try:
            connection = mysql.connector.connect(host='localhost', database='criminal', user='root', password='root')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT name, type, description FROM crmdetails where id={}".format(int(name)))
                rows = cursor.fetchall()
                for row in rows:
                    self.tree.insert("", "end", values=row)
        except mysql.connector.Error as error:
            print("Error while connecting to MySQL", error)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def face_detection_thread(self):
        video_capture = cv2.VideoCapture(0)

        while True:
            ret, frame = video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = 0
                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]
                face_names.append(name)

            self.tree.delete(*self.tree.get_children())  # Clear previous entries
            for name in face_names:
                self.update_treeview(name)
            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                    # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                                  #updating in database

                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    # Draw a label with a name below the face
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, str(name), (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            font = cv2.FONT_HERSHEY_DUPLEX
            # cv2.putText(frame, last_rec[0], (6,20), font, 1.0, (0,0 ,0), 1)

            # Display the resulting imagecv2.putText(frame, ref_dictt[name], (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

    def start_detection(self):
        threading.Thread(target=self.face_detection_thread, daemon=True).start()
        self.root.mainloop()

