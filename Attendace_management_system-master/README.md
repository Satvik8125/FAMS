# Face Recognition Based Attendance Management System

A robust and automated attendance management system that uses facial recognition technology to mark attendance efficiently. Built with Python, OpenCV, and Tkinter, this application eliminates the need for manual roll calls and provides a secure, digital way to track student attendance.

## 🚀 Features

*   **Automated Face Recognition**: Uses the LBPH (Local Binary Patterns Histograms) algorithm to recognize registered faces.
*   **Easy Registration**: Simple interface to capture and store student face data for training.
*   **Real-time Attendance**: Marks attendance instantly upon face recognition.
*   **Manual Entry**: Fallback option to manually fill attendance if needed.
*   **CSV Export**: Automatically generates daily attendance reports in CSV format.
*   **Database Integration**: Supports MySQL database for storing attendance records (requires setup).
*   **User-Friendly GUI**: Clean and intuitive interface built with Tkinter.

## 🛠️ Tech Stack

*   **Language**: Python 3.x
*   **Interface**: Tkinter
*   **Computer Vision**: OpenCV (`cv2`)
*   **Data Handling**: Pandas, NumPy, CSV
*   **Image Processing**: Pillow (`PIL`)
*   **Database**: PyMySQL

## 📋 Prerequisites

Ensure you have Python installed. You can install the required dependencies using pip:

```bash
pip install opencv-python numpy pandas Pillow pymysql
```

*Note: Tkinter is usually included with Python distributions.*

## ⚙️ Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone <your-repo-url>
    cd Attendace_management_system-master
    ```

2.  **Database Configuration (Optional)**
    *   The system can interface with a MySQL database (e.g., using WampServer or XAMPP). 
    *   Default database configurations are set to `localhost` with user `root` and no password.
    *   You can modify the database connection details in `AMS_Run.py` if you wish to use this feature.

3.  **Run the Application**
    ```bash
    python AMS_Run.py
    ```

## 📖 How to Use

1.  **Register a New Student**:
    *   Enter the **Enrollment Number** and **Name** in the provided fields.
    *   Click on **"Take Images"**. The webcam will open and capture 70 sample images of the student's face.
    *   These images are saved in the `TrainingImage` folder.

2.  **Train the Model**:
    *   After capturing images, click on **"Train Images"**.
    *   The system will process the images and train the internal model.
    *   A notification will appear when training is successful.

3.  **Mark Attendance**:
    *   Click on **"Automatic Attendance"**.
    *   Enter the **Subject Name** when prompted.
    *   The webcam will open. As it recognizes faces, it will mark attendance in real-time.
    *   Press `q` or wait for the timer to close the window.
    *   Attendance is saved as a CSV file in the `Attendance` folder.

4.  **View Records**:
    *   You can view the generated CSV files in the `Attendance` directory to see the logs.

## 📸 Screenshots

### Home Screen
<img src="Screenshot (43).png" width="400">
*Home Screen Interface*

### Face Recognition in Action
<img src="Screenshot (41).png" width="400">
*Face Recognition Active*

### Attendance Filled
<img src="Screenshot (42).png" width="400">
*Attendance Logs*

## 📄 License

This project is open-source and available for educational and personal use.
Copyright (c) 2026 Satvik Sharma.
