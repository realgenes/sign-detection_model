# Hand Detection and Sign Language Recognition

A real-time hand detection and sign language recognition system that can identify hand gestures for letters A-L using computer vision and machine learning.

## Features

- **Real-time Hand Detection**: Uses MediaPipe-based hand tracking to detect hands in live video
- **Data Collection**: Automated system to collect training images for different hand gestures
- **Sign Language Recognition**: Trained model to recognize hand signs for letters A through L
- **Live Prediction**: Real-time classification of hand gestures with visual feedback

## Project Structure

```
HandDetection/
├── dataCollection.py    # Script to collect training data
├── test.py             # Main application for real-time recognition
├── model/
│   ├── keras_model.h5  # Trained neural network model
│   └── labels.txt      # Class labels (A-L)
├── Data/               # Training data organized by letter
│   ├── A/
│   ├── B/
│   ├── C/
│   └── ... (through L)
└── README.md
```

## Requirements

- Python 3.7+
- OpenCV
- CVZone
- NumPy
- TensorFlow/Keras
- Webcam

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/HandDetection.git
cd HandDetection
```

2. Install required packages:
```bash
pip install opencv-python
pip install cvzone
pip install numpy
pip install tensorflow
```

## Usage

### Data Collection

To collect training data for a specific letter:

1. Open `dataCollection.py`
2. Change the `folder` variable to the desired letter (e.g., `"Data/A"` for letter A)
3. Run the script:
```bash
python dataCollection.py
```
4. Position your hand in the camera view showing the desired letter sign
5. Press 's' to save images
6. Collect multiple images (recommended: 100+ per letter)

### Real-time Recognition

To run the hand sign recognition:

```bash
python test.py
```

- Position your hand in front of the camera
- The system will detect your hand and predict the letter
- The predicted letter will be displayed on the screen

## How It Works

### Data Collection Process
1. **Hand Detection**: Uses CVZone's HandDetector to locate hands in the camera feed
2. **Image Preprocessing**: 
   - Crops the hand region with offset for better detection
   - Resizes to 300x300 pixels
   - Centers the hand image on a white background
   - Maintains aspect ratio to prevent distortion
3. **Data Storage**: Saves preprocessed images with timestamps

### Recognition Process
1. **Real-time Detection**: Continuously captures frames from webcam
2. **Hand Preprocessing**: Same preprocessing as data collection
3. **Classification**: Uses trained Keras model to predict the letter
4. **Visual Feedback**: Displays the predicted letter on the video feed

## Model Information

- **Architecture**: CNN (Convolutional Neural Network)
- **Input Size**: 300x300x3 (RGB images)
- **Classes**: 12 (Letters A through L)
- **Framework**: TensorFlow/Keras

## Controls

- **Data Collection Mode**: Press 's' to save an image
- **Exit**: Press any key to close the application

## Tips for Better Recognition

1. **Lighting**: Ensure good lighting conditions
2. **Background**: Use a plain background for better hand detection
3. **Hand Position**: Keep your hand clearly visible and well-positioned
4. **Consistency**: Maintain consistent hand poses during data collection
5. **Distance**: Keep a consistent distance from the camera

## Future Improvements

- [ ] Extend to full alphabet (A-Z)
- [ ] Add number recognition (0-9)
- [ ] Implement word and sentence recognition
- [ ] Add voice feedback
- [ ] Improve model accuracy with data augmentation
- [ ] Add gesture-to-text functionality

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- CVZone library for simplified computer vision operations
- MediaPipe for hand tracking technology
- OpenCV for computer vision functionality

## Contact

If you have any questions or suggestions, feel free to open an issue or contact me.

---

**Note**: This project is designed for educational purposes and basic sign language recognition. For production use, consider collecting more diverse training data and implementing additional error handling.
