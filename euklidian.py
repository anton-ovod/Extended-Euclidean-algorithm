import tkinter as tk
from tkinter import ttk

def euclidian_extended(a, b):
    list_of_values = []
    if a < b:
        a, b = b, a
    if a == 0 or b == 0:
        return -1
    d = a
    d_prim = b
    s = 1
    s_prim = 0
    t = 0
    t_prim = 1
    q = d // d_prim
    list_of_values.append((d, q, s, t))
    while d_prim != 0:
        q = d // d_prim
        d, d_prim = d_prim, d - q * d_prim
        s, s_prim = s_prim, s - q * s_prim
        t, t_prim = t_prim, t - q * t_prim
        list_of_values.append((d, q, s, t))
    return list_of_values


def create_tkinter_gui():
    window = tk.Tk()
    window.geometry("500x370")
    window.title("Extended euclidean algorithm GUI")
    window.resizable(False, False)
    a_label = tk.Label(window, text="Enter first number: ")
    a_label.grid(row=0, column=0, padx=10, pady=5)
    a_entry = tk.Entry(window, width=20)
    a_entry.grid(row=0, column=1, padx=10, pady=5)
    b_label = tk.Label(window, text="Enter second number: ")
    b_label.grid(row=1, column=0, padx=10, pady=5)
    b_entry = tk.Entry(window, width=20)
    b_entry.grid(row=1, column=1, padx=10, pady=5)
    error_label = tk.Label(window, text="", font="Arial 10")
    error_label.grid(row=2, column=0, padx=10, pady=5)
    #making table
    list = ttk.Treeview(window)
    list.grid(row=4, column=0, columnspan=2, padx=10)
    list['columns'] = ('d', 'q', 's', 't')
    # make columns
    list.column("#0", width=0, stretch=tk.NO)
    list.column("d", anchor=tk.CENTER, width=120)
    list.column("q", anchor=tk.CENTER, width=120)
    list.column("s", anchor=tk.CENTER, width=120)
    list.column("t", anchor=tk.CENTER, width=120)
    # make headings
    list.heading("#0", text="", anchor=tk.CENTER)
    list.heading("d", text="d", anchor=tk.CENTER)
    list.heading("q", text="q", anchor=tk.CENTER)
    list.heading("s", text="s", anchor=tk.CENTER)
    list.heading("t", text="t", anchor=tk.CENTER)
    def insert_values():
        for item in list.get_children():
            list.delete(item)
        try:
            euclidian_extended(int(a_entry.get()), int(b_entry.get()))
        except ValueError:
            error_label.config(text="Your input is incorrect", fg="red")
            return -1
        error_label.config(text="Your input is correct", fg="green")
        list_of_values = euclidian_extended(int(a_entry.get()), int(b_entry.get()))
        iid = 0
        for item in list_of_values:
            list.insert(parent='', index='end', iid=iid, text="", values=(item[0], item[1], item[2], item[3]))
            iid += 1
        gcd_label = tk.Label(window, text=f"GCD({max(int(a_entry.get()), int(b_entry.get()))}, {min(int(a_entry.get()), int(b_entry.get()))}) = {list_of_values[-1][0]} = {list_of_values[-1][2]} * {max(int(a_entry.get()), int(b_entry.get()))} + {list_of_values[-1][3]} * {min(int(a_entry.get()), int(b_entry.get()))} ", font="Arial 10")
        gcd_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
    run_button = tk.Button(window, text="Run the algorithm", command=lambda: insert_values())
    run_button.grid(row=2, column=1, padx=10, pady=5)
    window.mainloop()


def main():
    create_tkinter_gui()


if __name__ == "__main__":
    main()


