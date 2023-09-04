import tkinter as tk
from tkinter import messagebox

def calculate_required_average_damage():
    try:
        current_battles = int(entry_current_battles.get())
        current_avg_damage = int(entry_current_avg_damage.get())
        desired_avg_damage = int(entry_desired_avg_damage.get())
        total_battles = int(entry_total_battles.get())

        current_total_damage = current_battles * current_avg_damage
        desired_total_damage = desired_avg_damage * total_battles
        required_total_damage = desired_total_damage - current_total_damage
        required_avg_damage = required_total_damage / (total_battles - current_battles)

        result_label.config(text=f"Чтобы достичь среднего урона {desired_avg_damage} за {total_battles} боев, "
                                 f"вам нужно наносить средний урон {required_avg_damage:.2f} за каждый из оставшихся "
                                 f"{total_battles - current_battles} боев.")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовые значения.")

# Графический интерфейс
root = tk.Tk()
root.title("Расчет среднего урона")

label_current_battles = tk.Label(root, text="Количество сыгранных боев:")
label_current_battles.pack()

entry_current_battles = tk.Entry(root)
entry_current_battles.pack()

label_current_avg_damage = tk.Label(root, text="Средний урон за бой:")
label_current_avg_damage.pack()

entry_current_avg_damage = tk.Entry(root)
entry_current_avg_damage.pack()

label_desired_avg_damage = tk.Label(root, text="Желаемый средний урон за новые бои:")
label_desired_avg_damage.pack()

entry_desired_avg_damage = tk.Entry(root)
entry_desired_avg_damage.pack()

label_total_battles = tk.Label(root, text="Общее количество боев, которое вы хотите достичь:")
label_total_battles.pack()

entry_total_battles = tk.Entry(root)
entry_total_battles.pack()

calculate_button = tk.Button(root, text="Рассчитать", command=calculate_required_average_damage)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
