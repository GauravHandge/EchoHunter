# EchoHunter
A sonar-based system that hunts and classifies rocks and mines from sonar signals.

# Sonar Rock vs Mine Prediction

This project uses a **Logistic Regression** model to predict whether a sonar signal corresponds to a rock or a mine. The dataset contains sonar readings, with the target variable being either "R" for rock or "M" for mine.

The project uses **Streamlit** for a web-based user interface, allowing users to input sonar data and get predictions on whether the signal represents a rock or a mine.

---

## Requirements

Make sure you have Python 3.6+ installed. The following libraries are required to run this project:

- `numpy`
- `pandas`
- `scikit-learn`
- `streamlit`

---

## Installation

1. **Clone or Download the Repository**:
   - You can clone the repository using `git` or simply download the project files.
   
   ```bash
   git clone https://github.com/yourusername/sonar-rock-vs-mine.git


**Run the Streamlit App:**

Navigate to the project directory and run the following command in your terminal:

streamlit run sonar_prediction.py
