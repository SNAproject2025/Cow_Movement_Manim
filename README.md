# Cow Movement Visualization using Manim

## Overview
This project visualizes the movement of multiple cows in a barn using **Manim**, a mathematical animation engine. It takes cow position data from a JSON file and generates an animated visualization.

## Features
- Reads time-stamped cow position data from `TimeStampCowCoordinates.json`
- Normalizes coordinates to fit Manim's coordinate system
- Displays the movement of cows in a barn environment
- Generates smooth animations with labels for each cow

---

## Setup Instructions

### 1. Install Python
Ensure you have **Python 3.8+** installed. If not, download it from [Python.org](https://www.python.org/downloads/).

Verify installation:
```sh
python --version
```

### 2. Install an IDE (Recommended: PyCharm or VS Code)
- **[PyCharm](https://www.jetbrains.com/pycharm/)**
- **[VS Code](https://code.visualstudio.com/)**

### 3. Clone the Repository
```sh
git clone https://github.com/SNAproject2025/Cow_Movement_Manim.git  
cd Cow_Movement_Manim
```

### 4. Create a Virtual Environment (Recommended)
```sh
python -m venv venv  
source venv/bin/activate  # On macOS/Linux  
venv\Scripts\activate  # On Windows
```

### 5. Install Dependencies
```sh
pip install -r requirements.txt
```

---

## Running the Visualization
To generate and preview the animation:
```sh
manim -pql Cow_Movement_Manim.py CowsMovement
```

- `-pql`: Preview the animation in low quality
- `CowsMovement`: Name of the scene class in the script

### Example Output
A window will pop up displaying the animated movement of cows.

---

## Project Structure
```sh
Cow_Movement_Manim/  
│── Cow_Movement_Manim.py   # Main animation script  
│── TimeStampCowCoordinates.json   # JSON file containing cow positions  
│── requirements.txt   # Dependencies  
│── README.md   # Project documentation  
```

---

## Troubleshooting

### 1. `ModuleNotFoundError: No module named 'manim'`
- Ensure you installed Manim using `pip install manim`.
- Try running `python -m pip install --upgrade pip` before reinstalling.

### 2. `manim: command not found`
- Restart your terminal or ensure the virtual environment is activated.

### 3. The animation is lagging
- Try running in lower quality:
 ```sh
  manim -ql Cow_Movement_Manim.py CowsMovement
 ```

---

## Contributing
Feel free to fork this repository, improve the visualization, and submit a pull request!

---

## License
This project is licensed under the MIT License.
