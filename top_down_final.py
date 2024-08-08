import streamlit as st
import numpy as np
import graphviz
import time

def sift_up(arr, i, steps, sorted_indices):
    parent = (i - 1) // 2
    while i > 0 and arr[parent] < arr[i]:
        # Highlight current node in red
        steps.append((arr.copy(), set(sorted_indices), i, "red"))
        arr[i], arr[parent] = arr[parent], arr[i]
        i = parent
        parent = (i - 1) // 2
    
    # Highlight current node in green when settled
    steps.append((arr.copy(), set(sorted_indices), i, "green"))

def topDownHeapSort(arr):
    n = len(arr)
    steps = [(arr.copy(), set(), -1, "")]  # Initial state, no node highlighted
    sorted_indices = set()

    # Build a maxheap using top-down approach
    for i in range(n):
        sift_up(arr, i, steps, sorted_indices)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        sorted_indices.add(i)  # Mark the element as sorted
        steps.append((arr.copy(), set(sorted_indices), 0, "green"))  # Finalize node in green
        heapify(arr, i, 0, steps, sorted_indices)
    
    return steps

def heapify(arr, n, i, steps, sorted_indices):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        steps.append((arr.copy(), set(sorted_indices), i, "red"))  # Highlight current node in red
        heapify(arr, n, largest, steps, sorted_indices)

def visualize_heap(arr, sorted_indices, current_index, current_color):
    dot = graphviz.Digraph()
    n = len(arr)
    for i in range(n):
        color = "green" if i in sorted_indices else "black"
        label = str(arr[i])
        if i == current_index:
            color = current_color
        dot.node(str(i), label, color=color)
        if 2 * i + 1 < n and 2 * i + 1 not in sorted_indices:
            dot.edge(str(i), str(2 * i + 1), color="black")
        if 2 * i + 2 not in sorted_indices and 2 * i + 2 < n:
            dot.edge(str(i), str(2 * i + 2), color="black")
    return dot

def highlight_array(arr, sorted_indices):
    highlighted_arr = []
    for i in range(len(arr)):
        if i in sorted_indices:
            highlighted_arr.append(f'<span style="color:green">{arr[i]}</span>')
        else:
            highlighted_arr.append(f'<span style="color:black">{arr[i]}</span>')
    return highlighted_arr

def main():
    st.title("Creative Heap Sort Visualization")
    st.write("## An interactive visualization of the heap sort algorithm with creative highlighting")

    uploaded_file = st.file_uploader("Upload a text file containing an array", type=["txt"])
    if uploaded_file is not None:
        # Read file content
        content = uploaded_file.read().decode("utf-8")
        arr = list(map(int, content.split()))
        
        # Display the original array
        st.write("### Original Array")
        st.write(arr)
        
        # Perform heap sort
        steps = topDownHeapSort(arr)
        
        # Display the sorted array
        st.write("### Sorted Array")
        st.write(arr)
        
        # Visualize the steps
        st.write("### Heap Sort Steps")
        slide_index = st.slider("Select step", 0, len(steps)-1, 0)
        step_arr, sorted_until, current_index, current_color = steps[slide_index]
        highlighted_arr = highlight_array(step_arr, sorted_until)
        st.markdown(f"Step {slide_index + 1}: {' '.join(highlighted_arr)}", unsafe_allow_html=True)
        dot = visualize_heap(step_arr, sorted_until, current_index, current_color)
        st.graphviz_chart(dot)
        
        # Animation option
        if st.checkbox("Show animation of heap sort"):
            for step in steps:
                step_arr, sorted_until, current_index, current_color = step
                highlighted_arr = highlight_array(step_arr, sorted_until)
                st.markdown(f"Step {steps.index(step) + 1}: {' '.join(highlighted_arr)}", unsafe_allow_html=True)
                
                dot = visualize_heap(step_arr, sorted_until, current_index, current_color)
                st.graphviz_chart(dot)
                
                time.sleep(1)
        
        # Create a downloadable file with the sorted array
        sorted_file = "sorted_array.txt"
        np.savetxt(sorted_file, arr, fmt='%d')
        
        with open(sorted_file, "rb") as file:
            st.download_button(
                label="Download Sorted Array",
                data=file,
                file_name=sorted_file,
                mime="text/plain"
            )

if __name__ == "__main__":
    main()
