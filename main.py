import json
import heapq
import pyttsx3
import threading
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from node_manager import NodeManager 
from edge_manager import EdgeManager 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

engine = pyttsx3.init()


def speak(text):
    engine.setProperty('rate', 160)  
    engine.setProperty('volume', 1)  
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    engine.say(text)
    engine.runAndWait()


def speak_async(text):
    thread = threading.Thread(target=speak, args=(text,))
    thread.start()


node_manager = NodeManager(r'C:\PlayGround\Project\Smart Campus navigation System\nodes.json')
edge_manager = EdgeManager(r'C:\PlayGround\Project\Smart Campus navigation System\edges.json')


with open(r'C:\PlayGround\Project\Smart Campus navigation System\locations.json', 'r') as file:
    kist_location = json.load(file)

def dijkstra(graph, start, end):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    paths = {node: [] for node in graph}
    paths[start] = [start]
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue        

        for neighbor in graph.get(current_node, {}):
            weight = edge_manager.get_weight(current_node, neighbor)
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(queue, (distance, neighbor))

    return distances[end], paths[end]


def plot_map(ax):
    img = mpimg.imread(r'C:\PlayGround\Project\Smart Campus navigation System\map_img.png') 
    ax.axis('off')
    ax.imshow(img)


def run_dijkstra():
    start_node = start_input.get()
    end_node = end_input.get()

    try:
        distance, shortest_path = dijkstra(edge_manager.get_edges(), start_node, end_node)

        ax.clear()
        plot_map(ax)

        for i in range(len(shortest_path) - 1):
            node1 = shortest_path[i]
            node2 = shortest_path[i + 1]
            pos1 = node_manager.get_position(node1)
            pos2 = node_manager.get_position(node2)
            if pos1 and pos2:
                x_values = [pos1[0], pos2[0]]
                y_values = [pos1[1], pos2[1]]
                ax.plot(x_values, y_values, 'r-', lw=3) 

        start_pos = node_manager.get_position(start_node)
        end_pos = node_manager.get_position(end_node)

        if start_pos:
            ax.plot(start_pos[0], start_pos[1], 'bo', markersize=8) 

        if end_pos:
            ax.plot(end_pos[0], end_pos[1], 'bo', markersize=8) 

        ax.set_title(f"Path from {kist_location.get(start_node)} to {kist_location.get(end_node)} (Distance: {distance})")
        canvas.draw()
        error_label.config(text="")

        route_info = f"Path from {kist_location.get(start_node)} to {kist_location.get(end_node)} is {distance} meter long."
        speak_async(route_info)

    except KeyError:
        error_label.config(text="Invalid start or end node.")

    except Exception as e:
        error_label.config(text=f"Error: {str(e)}")

root = tk.Tk()
root.title("Campus Navigation System")
root.geometry("1536x960")  

map_frame = tk.Frame(root)
map_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)

location_frame = tk.Frame(right_frame)
location_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)

input_frame = tk.Frame(right_frame)
input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

location_label = tk.Label(location_frame, text="Locations", font=("Arial", 17, "bold"))
location_label.pack()

location_list = tk.Text(location_frame, font=(13), width=40, height=27)
location_list.pack(side=tk.TOP)

for key, name in kist_location.items():
    location_list.insert(tk.END, f" {key}   :   {name}\n")
location_list.config(state=tk.DISABLED)

tk.Label(input_frame, text="Start Node:", font=(15)).grid(row=0, column=0, padx=15, pady=5)
start_input = tk.Entry(input_frame, font=(15))
start_input.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="End Node:", font=(15)).grid(row=1, column=0, padx=5, pady=5)
end_input = tk.Entry(input_frame, font=(15))
end_input.grid(row=1, column=1, padx=5, pady=5)

run_button = tk.Button(input_frame, text="Find Path", font=(15), command=run_dijkstra)
run_button.grid(row=2, columnspan=2, pady=10)

error_label = tk.Label(input_frame, text="", fg="red", font=(20))
error_label.grid(row=3, columnspan=2)

fig, ax = plt.subplots(figsize=(8, 8))
plot_map(ax)

canvas = FigureCanvasTkAgg(fig, master=map_frame)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

root.mainloop()
