import os
import subprocess
import threading
import tkinter as tk
from tkinter import ttk

process_is_running = False
process_thread = None


def run_process(video_id: str, tts_type: str, line_callback: callable = None):
    def _run_process():
        global process_is_running
        process_is_running = True
        try:
            curr_env = os.environ.copy()
            proc = subprocess.Popen(['python', 'run.py', "--video_id", video_id, "--tts_type", tts_type],
                                    stdout=subprocess.PIPE, shell=True, env=curr_env)
            while process_is_running:
                line = proc.stdout.readline()
                if not line:
                    break
                if line_callback is not None:
                    line_callback(line)
                print(f"Process: {line.decode('utf-8').rstrip()}")
            proc.kill()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"Error: {e}")
        print("Process killed.")

    global process_thread
    process_thread = threading.Thread(target=_run_process)
    process_thread.start()


def stop_process():
    global process_is_running, process_thread
    if not process_is_running or process_thread is None:
        print("Process is not running.")
        return
    process_is_running = False

    process_thread.join()
    print("Process stopped.")


class RunGUI:
    """
    Run GUI class
    """

    def __init__(self, debug: bool = False):
        """
        Initialize the Run GUI class
        """
        self.debug = debug
        root = tk.Tk()
        root.title("Run GUI")
        style = ttk.Style()
        style.theme_use("vista")
        root.geometry("400x400")

        frame = ttk.Frame(root)
        frame.pack(fill=tk.BOTH, expand=True)

        video_id_label = ttk.Label(frame, text="Video ID")
        video_id_label.grid(row=0, column=0, padx=5, pady=5)
        video_id_entry = ttk.Entry(frame)
        video_id_entry.insert(0, "Your video ID here")
        video_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tts_type_label = ttk.Label(frame, text="TTS Type")
        tts_type_label.grid(row=1, column=0, padx=5, pady=5)
        tts_type_dropdown = ttk.Combobox(frame, values=["pyttsx3", "EL"])
        tts_type_dropdown.current(0)
        tts_type_dropdown.grid(row=1, column=1, padx=5, pady=5)

        run_button = ttk.Button(frame, text="Run",
                                command=lambda: run_process(video_id_entry.get(), tts_type_dropdown.get(),
                                                            lambda line: console.insert(tk.END, line)))
        run_button.grid(row=2, column=0, padx=5, pady=5)
        stop_button = ttk.Button(frame, text="Stop", command=stop_process)
        stop_button.grid(row=2, column=1, padx=5, pady=5)

        console = tk.Text(frame, height=10, width=50)
        console.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.root = root

    def run(self):
        """
        Run the Run GUI
        """
        self.log_d("Running the Run GUI...")
        self.root.mainloop()

    def log_d(self, message):
        if self.debug:
            print(message)


if __name__ == "__main__":
    RunGUI().run()
