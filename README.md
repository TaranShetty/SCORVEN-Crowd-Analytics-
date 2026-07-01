# 🚀 SCORVEN – Smart Crowd Observation and Response Vehicle

An AI-powered crowd detection and analytics system built using **YOLO**, **Streamlit**, **OpenCV**, and **Plotly** for real-time crowd monitoring, people counting, and density analysis.


## 📖 Overview

SCORVEN (Smart Crowd Observation and Response Vehicle) is an intelligent computer vision application that detects and counts people in real time using a custom-trained YOLO model. The system provides an interactive Streamlit dashboard for monitoring crowd density, visualizing analytics, and supporting surveillance and public safety applications.

## ✨ Features

- 👥 Real-time crowd detection
- 🎥 Webcam support
- 📂 Video upload support
- 📊 Live crowd count
- 📈 Crowd trend analysis
- 🟢 Low / 🟠 Moderate / 🔴 High density classification
- 🥧 Interactive density distribution chart
- ⚡ Interactive Streamlit dashboard
- 💻 CPU compatible


## 🛠️ Technologies Used

- Python
- Streamlit
- YOLO (Ultralytics)
- OpenCV
- NumPy
- Pandas
- Plotly

---

## 📂 Project Structure

```text
SCORVEN-Crowd-Analytics/
│── README.md
│── requirements.txt
│
└── Dash Board/
    │── Dashboard.py
    └── model/
```

## 📥 Model Download

The trained YOLO model (`best.pt`) is **not included** in this repository because it exceeds GitHub's file size limit.

### Download the model

1. Open the **Releases** section of this repository.
2. Download **best.pt** from the latest release.
3. Create a folder named **model** inside the **Dash Board** directory (if it doesn't already exist).
4. Place the downloaded file as shown below:

```text
Dash Board/
└── model/
    └── best.pt
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/SCORVEN-Crowd-Analytics.git
```

Navigate to the project folder:

```bash
cd SCORVEN-Crowd-Analytics
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Navigate to the dashboard folder:

```bash
cd "Dash Board"
```

Run the application:

```bash
streamlit run Dashboard.py
```

The Streamlit dashboard will open automatically in your default web browser.


## 📊 Dashboard Features

- Real-time people detection
- Live crowd counting
- Peak, average, and minimum crowd statistics
- Crowd density classification
- Interactive trend visualization
- Density distribution analytics
- Webcam and uploaded video support


## 🎯 Applications

- Smart Cities
- Public Safety
- Railway Stations
- Airports
- Shopping Malls
- Stadiums
- Event Management
- Traffic Monitoring
- Disaster Response


## 📦 Requirements

```
streamlit
opencv-python
pandas
numpy
ultralytics
plotly
```


## 🔮 Future Improvements

- Multi-camera support
- Heatmap generation
- Automatic crowd alerts
- Person tracking
- Cloud deployment
- Database integration
- GPU acceleration



## 👨‍💻 Authors

**Taran Shetty**,
**Mayank Upadhyay**

B.Tech – Artificial Intelligence & Machine Learning

Thakur College of Engineering and Technology (TCET)




## 📄 License

This project is intended for educational and research purposes.


⭐ If you found this project useful, please consider starring the repository.
