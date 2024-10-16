# DeepColorizer 🎨

**DeepColorizer** is an AI-powered application that colorizes black and white images using deep learning techniques. By leveraging a pre-trained model implemented with OpenCV and Caffe, the project predicts and adds appropriate colors to grayscale images, allowing users to transform historical or black-and-white photos into vibrant, colorized versions.

## Table of Contents
- Project Overview
- Features
- Technologies Used
- Setup Instructions
- Usage
- Model and Dataset
- Screenshots
- Contributing

## Project Overview 📁
The goal of this project is to automate the process of colorizing black and white images using convolutional neural networks (CNNs). The application allows users to upload grayscale images, process them using a pre-trained model, and download the colorized versions.

## Features ⭐
- Upload and process black and white images.
- Automatically colorize images using a deep learning model.
- Simple web interface built with Flask.
- Efficient image processing with OpenCV.

## Technologies Used 🛠️
- **Python**
- **Flask**: Web framework for building the application interface.
- **OpenCV**: For image processing and conversion between color spaces.
- **Caffe**: Pre-trained model for image colorization.
- **NumPy**: For efficient numerical operations on images.
- **cv2.dnn**: OpenCV's DNN module to load the pre-trained model.

## Setup Instructions 🚀

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mahihubb/DeepColorizer.git
   cd DeepColorizer
   ```

2. **Install Dependencies**:
   Install the required libraries using `pip`:
   ```bash
   pip install Flask opencv-python-headless numpy
   ```

3. **Download the Pre-trained Model**:
   Download the model file `colorization_release_v2.caffemodel` from [this link](https://www.dropbox.com/s/dx0qvhhp5hbcx7z/colorization_release_v2.caffemodel?dl=1) and save it in the `models/` directory.

4. **Run the Application**:
   After setting up the environment and downloading the model, run the Flask app:
   ```bash
   python app.py
   ```

5. **Access the Application**:
   Visit `http://127.0.0.1:5000/` in your browser to use the web interface.

## Usage 🖼️
1. Upload a black and white image (e.g., `.jpg` or `.png` format).
2. The image will be processed using the deep learning model.
3. Download the colorized version of the image from the results page.

## Model and Dataset 📊
This project uses a **pre-trained model** for image colorization, which was trained on a large dataset of images. The model predicts the color channels (`a` and `b` from the LAB color space) for grayscale images. The model used is based on research in the field of automatic image colorization using CNNs.

## Screenshots 📸
![home (2)](https://github.com/user-attachments/assets/0c88aab7-d4c6-48f3-860f-e9fdbba01716)

![example1 (2)](https://github.com/user-attachments/assets/18307b5a-0c51-40ef-818a-212efe71a661)

![Screenshot (75)](https://github.com/user-attachments/assets/e43cc491-39aa-485e-b557-2c11746847a0)

![Screenshot (76)](https://github.com/user-attachments/assets/d35fa4aa-b4ba-4479-af2c-666975cb1de2)



## Contributing 🤝
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

