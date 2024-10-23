# Efficient Data Stream Anomaly Detection

## Project Description
This project is designed to detect anomalies in a continuous data stream of floating-point numbers, which simulates real-time sequences such as financial transactions or system metrics. The goal is to identify unusual patterns, like significant deviations from the norm, and provide real-time detection of anomalies.

## Code Overview

### Data Stream Simulation
The function `data_stream_simulation()` generates a synthetic data stream that includes regular seasonal patterns, random noise, and injected anomalies.

### Anomaly Detection
Anomalies are detected by calculating the mean and standard deviation over a sliding window of data points. Any point that deviates from the mean by more than three times the standard deviation is flagged as an anomaly.

### File Handling
Three files are generated:
- `input_data.txt`: Contains the generated data stream.
- `output_data.txt`: Marks anomalies in the data stream with an asterisk (`*`).
- `anomalies.txt`: Lists the indices of detected anomalies.

### Visualization
The `animate()` function plots the real-time data stream along with the detected anomalies and anomaly thresholds. The data stream is animated using Matplotlib’s `FuncAnimation`.

## Files
- **`input_data.txt`**: The simulated data stream.
- **`output_data.txt`**: The data stream with anomalies marked.
- **`anomalies.txt`**: Contains the indices of detected anomalies.

## How to Run
Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Algorithm Explanation
The chosen algorithm for anomaly detection is based on calculating the **mean** and **standard deviation** over a sliding window of recent data points. Anomalies are detected when a point deviates from the mean by more than three times the standard deviation (3σ rule). This method is effective because it adapts to seasonal patterns and noise by recalculating the mean and standard deviation in real-time, allowing it to detect significant deviations quickly.

### Why This Algorithm?
- **Effectiveness**: The simplicity of the algorithm makes it fast and suitable for real-time anomaly detection, especially in streaming scenarios. It also naturally adapts to data with seasonal fluctuations by continuously updating its window.
- **Limitations**: While effective for many use cases, it may struggle with more complex, non-linear patterns of anomalies. However, it's lightweight and optimized for continuous data streams.

## Error Handling and Data Validation
The script includes basic error handling and data validation:
- **Boundary Checks**: It ensures the sliding window only starts once enough data points are available.
- **Handling Empty Data**: Functions like `calculate_mean()` and `calculate_std_dev()` validate input to avoid errors such as division by zero.
- **File Operations**: Writing data to files is wrapped in `try-except` blocks to handle file I/O issues gracefully.

## External Libraries
The project limits the use of external libraries to ensure lightweight and efficient execution. The only external library used is:
- `matplotlib` for visualization and animation.

If additional libraries are needed, include them in a `requirements.txt` file.


