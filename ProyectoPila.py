import time
from queue import Queue
import tkinter as tk
from tkinter import messagebox

class BankQueueSimulator:
    def __init__(self):
        self.queue = Queue()
        self.root = tk.Tk()
        self.root.title("Simulador de Atención en una Cola de Banco")
        self.label = tk.Label(self.root, text="Cola de clientes:")
        self.label.pack()
        self.listbox = tk.Listbox(self.root, width=40)
        self.listbox.pack()
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack()
        self.add_button = tk.Button(self.root, text="Agregar cliente", command=self.add_client)
        self.add_button.pack()
        self.serve_button = tk.Button(self.root, text="Atender cliente", command=self.serve_client)
        self.serve_button.pack()

    def add_client(self):
        client_name = self.entry.get()
        if client_name:
            self.queue.put(client_name)
            self.listbox.insert(tk.END, client_name)
            self.entry.delete(0, tk.END)

    def serve_client(self):
        if not self.queue.empty():
            client_name = self.queue.get()
            self.listbox.delete(0, tk.END)
            for client in list(self.queue.queue):
                self.listbox.insert(tk.END, client)
            messagebox.showinfo("Atención", f"Cliente {client_name} atendido")
            time.sleep(5)  
        else:
            messagebox.showinfo("Error", "No hay clientes en la cola")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    simulator = BankQueueSimulator()
    simulator.run()