🎨 Color Detection and Image Processing Project
Overview
This project consists of two Python scripts designed for image processing and color detection. 
The first script processes static images, converting them to grayscale, applying Gaussian blur, and detecting edges. 
The second script utilizes a webcam feed to identify and display the color of clicked pixels. 
Built with OpenCV and pandas, this project aims to streamline color identification and image analysis. 🚀

✨ Features
🖼️ Image Processing: Convert images to grayscale, apply blur, and detect edges.
🗂️ Result Saving: Save processed images with different filters applied.
📷 Webcam Color Detection: Click on any pixel to identify its color and view RGB values.

🛠️ Prerequisites
🐍 Python 3.8+
🌐 A modern web browser (for viewing results if applicable)
📄 Required libraries listed in requirements.txt

⚙️ Installation
Clone the Repository 📂:
bash:
git clone https://github.com/your-username/color-detection.git
cd color-detection

Create a Virtual Environment (optional but recommended) 🧪:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies 📦:
pip install -r requirements.txt

The requirements.txt should include:
opencv-python==4.10.0.84
numpy==1.26.4
pandas==2.2.2

🚀 Usage
Run the Image Processing Script 🖼️:
cd task1
python main.py
This processes the specified image file and saves the results.

Run the Color Detection Application 📷:
cd task2
python main.py
This opens a webcam feed for color detection.


📂 Project Structure

ComputerVisionInternshipAssessment/
├── task1              
    ├── main.py          # Static image processing script 🖼️
    ├── image.jpg        # Static image
    ├── output_blurred.jpg    
    ├── output_edges.jpg
    └── output_grayscale.jpg
├── task2             
    ├── main.py          # Webcam color detection application 🎨
    ├── colors.csv
    └── Webcam Feed      # Project demo video
├── task3             
    ├── CVInternshipAssessmentReport.pdf 
├── requirements.txt     # Project dependencies 📋
└── README.md            # The Readme.md file 📖

📸 Example Use Case
The project is designed to handle standard images:

![image](https://github.com/user-attachments/assets/92203071-f78a-4a2b-8830-948cadbd7d7f)

![output_edges](https://github.com/user-attachments/assets/95a52a61-f98b-4adb-898c-4761b4432097)

🤝 Contributing
I welcome contributions! To get started:

🍴 Fork the repository.
🌿 Create a feature branch (e.g., git checkout -b feature/your-feature).
💾 Commit your changes (e.g., git commit -m "Add your feature").
🚀 Push to the branch (e.g., git push origin feature/your-feature).
📬 Open a pull request.
Please ensure your code follows PEP 8 guidelines and includes relevant tests.

🙏 Acknowledgments
Built with OpenCV and pandas. 🎉

📧 Contact
For questions or feedback, please contact me at [info@jitenrai.com.np]. ✉️
