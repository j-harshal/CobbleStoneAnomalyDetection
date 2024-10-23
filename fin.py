import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Function to simulate the data stream with regular patterns and anomalies
def data_stream_simulation(stream_length=1000):
    data = []
    for i in range(stream_length):
        # Seasonal pattern (sine-like wave)
        seasonal_value = 10 * (i % 100) / 100
        # Random noise
        noise = random.uniform(-5, 5)
        # Combined value
        value = seasonal_value + noise
        data.append(value)

    # Injecting anomalies for testing
    data[200] = 20  # Positive anomaly
    data[600] = -20  # Negative anomaly
    return data


# Function to calculate the mean of a list of numbers
def calculate_mean(window):
    return sum(window) / len(window)


# Function to calculate the standard deviation from scratch
def calculate_std_dev(window, mean):
    variance = sum((x - mean) ** 2 for x in window) / len(window)
    return variance ** 0.5


# Real-time anomaly detection function
def anomaly_detection(data_stream, window_size=50):
    anomalies = []
    for i in range(len(data_stream)):
        if i < window_size:
            continue  # Skip until we have enough data for a window

        window = data_stream[i - window_size:i]
        mean = calculate_mean(window)
        std_dev = calculate_std_dev(window, mean)
        value = data_stream[i]

        # Detect anomalies if value is greater than 3 times standard deviation
        if abs(value - mean) > 3 * std_dev:
            anomalies.append(i)  # Store the index of the anomaly

    return anomalies


# Function to write the input data stream to a file
def write_data_to_file(data_stream, filename="input_data.txt"):
    with open(filename, "w") as file:
        for index, value in enumerate(data_stream):
            file.write(f"{index}, {value:.4f}\n")


# Function to write output with anomalies marked
def write_output_with_anomalies(data_stream, anomalies, filename="output_data.txt"):
    with open(filename, "w") as file:
        for index, value in enumerate(data_stream):
            if index in anomalies:
                file.write(f"{index}, {value:.4f} *\n")  # Mark anomaly with '*'
            else:
                file.write(f"{index}, {value:.4f}\n")


# Function to write the indices of detected anomalies to a file
def write_anomalies_to_file(anomalies, filename="anomalies.txt"):
    with open(filename, "w") as file:
        for anomaly in anomalies:
            file.write(f"Anomaly detected at index: {anomaly}\n")


# Animation function to visualize the data stream and anomalies
def animate(i):
    ax.clear()
    ax.plot(data_stream[:i], label='Data Stream')
    if i > window_size:
        # Calculate the window, mean, and standard deviation
        window = data_stream[i - window_size:i]
        mean = calculate_mean(window)
        std_dev = calculate_std_dev(window, mean)
        # Plot the mean and the threshold for anomalies
        ax.axhline(y=mean, color='green', linestyle='--', label='Mean')
        ax.axhline(y=mean + 3 * std_dev, color='red', linestyle='--', label='Anomaly Threshold (+3σ)')
        ax.axhline(y=mean - 3 * std_dev, color='red', linestyle='--', label='Anomaly Threshold (-3σ)')
        # Mark the anomalies detected so far
        for anomaly in anomalies:
            if anomaly <= i:
                ax.plot(anomaly, data_stream[anomaly], 'ro', label='Anomaly')

    ax.legend()
    ax.set_title(f"Data Stream Visualization (t={i})")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")


if __name__ == "__main__":
    # Simulate the data stream
    data_stream = data_stream_simulation()

    # Write the input data stream to file
    write_data_to_file(data_stream)

    # Detect anomalies
    window_size = 50
    anomalies = anomaly_detection(data_stream, window_size)

    # Write the output with anomalies marked
    write_output_with_anomalies(data_stream, anomalies)

    # Write the anomaly indices to a file
    write_anomalies_to_file(anomalies)

    # Optionally print the list of anomaly indices
    print("Detected anomalies at the following indices:", anomalies)

    # Set up the plot for animation
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, animate, frames=len(data_stream), interval=10)

    # Show the animation
    plt.show()
