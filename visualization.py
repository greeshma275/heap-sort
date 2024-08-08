import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# Function to generate a list of integers
def generate_list(size):
    return list(range(size))

# Heapify function for top-down approach
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Bottom-Up Heapify
def bottom_up_heapify(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# Time the heap sort algorithms
def time_heap_sort(size):
    arr = generate_list(size)
    
    # Top-Down Heap Sort
    arr_td = arr.copy()
    start_td = time.time()
    bottom_up_heapify(arr_td)
    end_td = time.time()
    top_down_time = end_td - start_td
    
    # Bottom-Up Heap Sort
    arr_bu = arr.copy()
    start_bu = time.time()
    heapify(arr_bu, size, 0)
    end_bu = time.time()
    bottom_up_time = end_bu - start_bu
    
    return top_down_time, bottom_up_time

# Streamlit UI
st.title('Heap Sort Time Complexity Visualization')

# User input for range of sizes
min_size = st.slider('Select the minimum number of elements:', min_value=1000, max_value=9000, value=1000)
max_size = st.slider('Select the maximum number of elements:', min_value=min_size+1000, max_value=10000, value=10000)

# Generate time complexity data
sizes = np.arange(min_size, max_size + 1, 1000)
top_down_times = []
bottom_up_times = []

for size in sizes:
    td_time, bu_time = time_heap_sort(size)
    top_down_times.append(td_time)
    bottom_up_times.append(bu_time)

# Plotting the results
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(sizes, top_down_times, label='Top-Down Heap Sort', color='blue', marker='o')
ax.plot(sizes, bottom_up_times, label='Bottom-Up Heap Sort', color='red', marker='o')

ax.set_title('Time Complexity of Heap Sort (Top-Down vs. Bottom-Up)')
ax.set_xlabel('Number of Elements')
ax.set_ylabel('Time (seconds)')
ax.legend()
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# Function to generate a list of integers
def generate_list(size):
    return list(range(size))

# Heapify function for top-down approach
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Bottom-Up Heapify
def bottom_up_heapify(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# Time the heap sort algorithms
def time_heap_sort(size):
    arr = generate_list(size)
    
    # Top-Down Heap Sort
    arr_td = arr.copy()
    start_td = time.time()
    bottom_up_heapify(arr_td)
    end_td = time.time()
    top_down_time = end_td - start_td
    
    # Bottom-Up Heap Sort
    arr_bu = arr.copy()
    start_bu = time.time()
    heapify(arr_bu, size, 0)
    end_bu = time.time()
    bottom_up_time = end_bu - start_bu
    
    return top_down_time, bottom_up_time

# Streamlit UI
st.title('Heap Sort Time Complexity Visualization')

# User input for range of sizes
min_size = st.slider('Select the minimum number of elements:', min_value=1000, max_value=9000, value=1000)
max_size = st.slider('Select the maximum number of elements:', min_value=min_size+1000, max_value=10000, value=10000)

# Generate time complexity data
sizes = np.arange(min_size, max_size + 1, 1000)
top_down_times = []
bottom_up_times = []

for size in sizes:
    td_time, bu_time = time_heap_sort(size)
    top_down_times.append(td_time)
    bottom_up_times.append(bu_time)

# Plotting the results
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(sizes, top_down_times, label='Top-Down Heap Sort', color='blue', marker='o')
ax.plot(sizes, bottom_up_times, label='Bottom-Up Heap Sort', color='red', marker='o')

ax.set_title('Time Complexity of Heap Sort (Top-Down vs. Bottom-Up)')
ax.set_xlabel('Number of Elements')
ax.set_ylabel('Time (seconds)')
ax.legend()
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)
