# Criminal-face-identification-system
Criminal Face Identification System

Overview

The Criminal Face Identification System is designed to assist law enforcement agencies in identifying criminals using facial recognition technology. The system achieves high accuracy through the use of MTCNN (Multi-task Cascaded Convolutional Networks) for facial detection and FaceNet for feature extraction and identification.

The project aims to enhance security and improve real-time identification of individuals in video feeds or photographs, making it an efficient tool for criminal identification.

Features

Real-Time Identification: Identifies individuals based on stored facial data in real-time.
High Accuracy: Achieved 98% accuracy in criminal identification using deep learning models.
Facial Detection: Utilizes MTCNN for robust face detection in images and videos.
Face Recognition: Employs FaceNet to extract unique facial features for matching.
Database Integration: Stores criminal records and associated facial data for easy retrieval.
Video Input Processing: Capable of identifying faces from live video inputs or stored video files.
Technologies Used

Python: Main programming language for developing the system.
OpenCV: Used for image and video processing tasks.
Keras/TensorFlow: Frameworks used for implementing deep learning models for face recognition.
MTCNN: Used for detecting faces in images and videos.
FaceNet: Used for extracting facial features and performing recognition.
MySQL: Database used to store criminal records and facial data.
Installation

Requirements
Python 3.6+
TensorFlow 2.0+
Keras 2.3+
OpenCV 4.0+
MySQL (for database integration)
Steps to Run the System
Clone the repository:
git clone https://github.com/isha962/criminal-face-identification.git
Install required dependencies:
pip install -r requirements.txt
Set up your MySQL database with the necessary tables for storing criminal records and facial data.
Run the system:
python face_identification.py
You can provide a video feed or a stored image to test the system's identification capabilities.
Usage

Once the system is set up and running, simply input a video stream or image file to test the identification process. The system will process the input, detect faces, and compare them with stored records to identify potential matches.

Contributing

Feel free to fork the repository and submit pull requests for any improvements or additional features. If you encounter any bugs or issues, please open an issue in the repository.
