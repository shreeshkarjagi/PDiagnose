# PDiagnose 

A Python-based application that provides a user-friendly interface for Parkinson's Disease detection through spiral drawing analysis, inspired by [Robin T. White's research work](https://github.com/robintwhite/parkinsons-sketch).

## Features

- **Simple GUI Interface**: Built with Tkinter for easy image upload and analysis
- **Real-time Processing**: Immediate results after image upload
- **Training Data Collection**: Optional user feedback system to improve model accuracy
- **Image Processing Pipeline**: Uses OpenCV and scikit-image for feature extraction
- **Machine Learning Model**: Random Forest classifier for prediction

## Technical Implementation

### Core Components

```
PDiagnose/
├── Interface.py          # GUI and main application logic
├── parkinson_model.py    # ML model and feature extraction
├── process_data.py      # Data preprocessing utilities
├── process_images.py    # Image processing functions
└── drawings/           
    └── spiral/          
        ├── training/    
        └── testing/     
```

### Dependencies
- opencv-python
- scikit-image
- scikit-learn
- xgboost
- numpy
- pillow
- imutils
- tkinter

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python Interface.py
```

2. Draw a spiral pattern according to the guide shown
3. Use "Select Image" to upload your drawing
4. View analysis results
5. Optionally contribute to model training by confirming diagnosis status

## Features

The GUI application provides:
- Visual guide for spiral drawing
- Real-time image analysis
- Prediction results display
- Optional feedback collection
- Training data management

## Note
This is a proof-of-concept implementation based on research by [Robin T. White](https://github.com/robintwhite/parkinsons-sketch). Not for medical diagnosis.

## License
MIT License
