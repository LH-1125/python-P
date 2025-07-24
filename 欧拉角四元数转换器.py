import numpy as np
import numpy.typing as npt
import math
import tkinter as tk
from tkinter import ttk, messagebox
from typing import List


class QuaternionEulerConverter:
    def __init__(self, root_1: tk.Tk) -> None:
        self.root_1 = root_1
        self.root = root
        self.root.title("欧拉角与四元数转换器")
        self.root.geometry("470x560")
        self.root.resizable(False, False)

        # 设置 ttk 主题
        style = ttk.Style()
        style.theme_use('clam')

        # 主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 标题
        ttk.Label(main_frame, text="欧拉角与四元数转换", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2,
                                                                                          pady=10)

        # 欧拉角输入区域
        euler_frame = ttk.LabelFrame(main_frame, text="欧拉角输入（度）", padding="10")
        euler_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(euler_frame, text="Roll:").grid(row=0, column=0, padx=5, pady=5)
        self.roll_entry = ttk.Entry(euler_frame, width=15)
        self.roll_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(euler_frame, text="Pitch:").grid(row=1, column=0, padx=5, pady=5)
        self.pitch_entry = ttk.Entry(euler_frame, width=15)
        self.pitch_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(euler_frame, text="Yaw:").grid(row=2, column=0, padx=5, pady=5)
        self.yaw_entry = ttk.Entry(euler_frame, width=15)
        self.yaw_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(euler_frame, text="转换为四元数", command=self.euler_to_quaternion_gui).grid(row=3, column=0,
                                                                                                columnspan=2, pady=10)

        # 四元数输入区域
        quat_frame = ttk.LabelFrame(main_frame, text="四元数输入", padding="10")
        quat_frame.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(quat_frame, text="w:").grid(row=0, column=0, padx=5, pady=5)
        self.w_entry = ttk.Entry(quat_frame, width=15)
        self.w_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(quat_frame, text="x:").grid(row=1, column=0, padx=5, pady=5)
        self.x_entry = ttk.Entry(quat_frame, width=15)
        self.x_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(quat_frame, text="y:").grid(row=2, column=0, padx=5, pady=5)
        self.y_entry = ttk.Entry(quat_frame, width=15)
        self.y_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(quat_frame, text="z:").grid(row=3, column=0, padx=5, pady=5)
        self.z_entry = ttk.Entry(quat_frame, width=15)
        self.z_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(quat_frame, text="转换为欧拉角", command=self.quaternion_to_euler_gui).grid(row=4, column=0,
                                                                                               columnspan=2, pady=10)

        # 结果显示区域
        result_frame = ttk.LabelFrame(main_frame, text="转换结果", padding="10")
        result_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)

        self.result_text = tk.Text(result_frame, height=8, width=60, font=("Arial", 10))
        self.result_text.grid(row=0, column=0, padx=5, pady=5)
        self.result_text.config(state='disabled')

        # 按钮区域 - 使用更明显的样式
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        # 清空按钮 - 使用更大的字体和颜色
        clear_button = ttk.Button(button_frame, text="清空数据", command=self.clear_all)
        clear_button.grid(row=0, column=0, padx=30)

        # 退出按钮 - 使用更大的字体和颜色
        exit_button = ttk.Button(button_frame, text="退出程序", command=self.exit_program)
        exit_button.grid(row=0, column=1, padx=30)

    @staticmethod
    def euler_to_quaternion(roll: float, pitch: float, yaw: float) -> npt.NDArray[np.float64]:
        """将欧拉角（弧度）转换为四元数"""
        cr = math.cos(roll / 2)
        sr = math.sin(roll / 2)
        cp = math.cos(pitch / 2)
        sp = math.sin(pitch / 2)
        cy = math.cos(yaw / 2)
        sy = math.sin(yaw / 2)

        w = cr * cp * cy + sr * sp * sy
        x = sr * cp * cy - cr * sp * sy
        y = cr * sp * cy + sr * cp * sy
        z = cr * cp * sy - sr * sp * cy

        return np.array([w, x, y, z])

    @staticmethod
    def quaternion_to_euler(q: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        """将四元数转换为欧拉角（弧度）"""
        w, x, y, z = q
        norm = np.sqrt(w ** 2 + x ** 2 + y ** 2 + z ** 2)
        if norm == 0:
            raise ValueError("四元数不能全为零")
        w, x, y, z = w / norm, x / norm, y / norm, z / norm

        sinr_cos = 2 * (w * x + y * z)
        cos_cost = 1 - 2 * (x ** 2 + y ** 2)
        roll = math.atan2(sinr_cos, cos_cost)

        sin = 2 * (w * y - z * x)
        if abs(sin) >= 1:
            pitch = math.copysign(math.pi / 2, sin)
        else:
            pitch = math.asin(sin)

        sin_cop = 2 * (w * z + x * y)
        cosy_cos = 1 - 2 * (y ** 2 + z ** 2)
        yaw = math.atan2(sin_cop, cosy_cos)

        return np.array([roll, pitch, yaw])

    @staticmethod
    def degrees_to_radians(degrees: List[float]) -> npt.NDArray[np.float64]:
        """将角度转换为弧度"""
        return np.array(degrees) * math.pi / 180

    @staticmethod
    def radians_to_degrees(radians: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        """将弧度转换为角度"""
        return np.array(radians) * 180 / math.pi

    def euler_to_quaternion_gui(self) -> None:
        """处理欧拉角到四元数的转换"""
        try:
            roll: float = float(self.roll_entry.get())
            pitch: float = float(self.pitch_entry.get())
            yaw: float = float(self.yaw_entry.get())
            euler_rad: npt.NDArray[np.float64] = self.degrees_to_radians([roll, pitch, yaw])
            quaternion: npt.NDArray[np.float64] = self.euler_to_quaternion(*euler_rad)
            euler_converted: npt.NDArray[np.float64] = self.radians_to_degrees(self.quaternion_to_euler(quaternion))

            result = (f"输入的欧拉角（度）：\n"
                      f"Roll: {roll:.2f}, Pitch: {pitch:.2f}, Yaw: {yaw:.2f}\n\n"
                      f"转换得到的四元数 [w, x, y, z]：\n"
                      f"{quaternion[0]:.6f}, {quaternion[1]:.6f}, {quaternion[2]:.6f}, {quaternion[3]:.6f}\n\n"
                      f"验证：转换回的欧拉角（度）：\n"
                      f"Roll: {euler_converted[0]:.2f}, Pitch: {euler_converted[1]:.2f}, Yaw: {euler_converted[2]:.2f}")

            self.result_text.config(state='normal')
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)
            self.result_text.config(state='disabled')
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字！")

    def quaternion_to_euler_gui(self) -> None:
        """处理四元数到欧拉角的转换"""
        try:
            w: float = float(self.w_entry.get())
            x: float = float(self.x_entry.get())
            y: float = float(self.y_entry.get())
            z: float = float(self.z_entry.get())
            quaternion: npt.NDArray[np.float64] = np.array([w, x, y, z])
            if np.all(quaternion == 0):
                messagebox.showerror("错误", "四元数不能全为零！")
                return
            euler_rad: npt.NDArray[np.float64] = self.quaternion_to_euler(quaternion)
            euler_deg: npt.NDArray[np.float64] = self.radians_to_degrees(euler_rad)
            quaternion_converted: npt.NDArray[np.float64] = self.euler_to_quaternion(*euler_rad)

            result = (f"输入的四元数 [w, x, y, z]：\n"
                      f"{w:.6f}, {x:.6f}, {y:.6f}, {z:.6f}\n\n"
                      f"转换得到的欧拉角（度）：\n"
                      f"Roll: {euler_deg[0]:.2f}, Pitch: {euler_deg[1]:.2f}, Yaw: {euler_deg[2]:.2f}\n\n"
                      f"验证：转换回的四元数 [w, x, y, z]：\n"
                      f"{quaternion_converted[0]:.6f}, {quaternion_converted[1]:.6f}, "
                      f"{quaternion_converted[2]:.6f}, {quaternion_converted[3]:.6f}")

            self.result_text.config(state='normal')
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)
            self.result_text.config(state='disabled')
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字！")

    def clear_all(self) -> None:
        """清空所有输入字段和结果显示区域"""
        # 清空欧拉角输入
        self.roll_entry.delete(0, tk.END)
        self.pitch_entry.delete(0, tk.END)
        self.yaw_entry.delete(0, tk.END)

        # 清空四元数输入
        self.w_entry.delete(0, tk.END)
        self.x_entry.delete(0, tk.END)
        self.y_entry.delete(0, tk.END)
        self.z_entry.delete(0, tk.END)

        # 清空结果显示区域
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state='disabled')

    def exit_program(self) -> None:
        """退出程序"""
        if messagebox.askyesno("确认退出", "确定要退出程序吗？"):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuaternionEulerConverter(root)
    root.mainloop()