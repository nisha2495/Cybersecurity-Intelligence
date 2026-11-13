import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import datetime, time

BG = "#0f172a"
CARD = "#1e293b"
BLUE = "#38bdf8"
ORANGE = "#f97316"
DARK_BLUE = "#0c4a6e"

def get_demo_report(topic):
    return f"""
🛡️ MULTI-AI AGENT SYSTEM - LIVE DEMO REPORT
Topic: {topic} | Date: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}
Status: ✅ LIVE DEMO SUCCESSFUL

🤖 AGENT 1 - THREAT DETECTION EXPERT
- {topic} ek boht khatarnaak cyber attack hai.
- Types: Email Phishing, Spear Phishing, Smishing, Vishing
- Example: Bank ka fake SMS, Fake Job Offer, Fake JazzCash link

🤖 AGENT 2 - VULNERABILITY ANALYST
🔴 HIGH RISK: Kamzor Password, 2FA Off hona
🟡 MEDIUM RISK: Public WiFi, Software update nahi karna
🟢 LOW RISK: Browser me password save karna

🤖 AGENT 3 - INCIDENT RESPONSE & SOLUTION
STEP 1: Turant password change karo
STEP 2: Bank ko call karke card block karwao
STEP 3: FIA Cyber Crime ko report karo
PREVENTION: Strong password, 2FA ON, Kabhi OTP mat batao
TOOLS: Google Authenticator, Bitwarden, VirusTotal.com
✅ FINAL VERDICT: Upar wale steps follow karo, system SECURE ho jayega!
Made by Nisha | Multi-AI Agent System
"""

def run_live_demo():
    topic = entry.get() or "Phishing Attack"
    result_box.delete("1.0", tk.END)
    status_label.config(text="⏳ LIVE DEMO chal rahi hai...")
    root.update()
    result_box.insert(tk.END, "🤖 Agent 1 kaam kar raha hai...\n"); root.update(); time.sleep(0.5)
    result_box.insert(tk.END, "🤖 Agent 2 kaam kar raha hai...\n"); root.update(); time.sleep(0.5)
    result_box.insert(tk.END, "🤖 Agent 3 Report bana raha hai...\n\n"); root.update(); time.sleep(0.5)
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, get_demo_report(topic))
    status_label.config(text="✅ LIVE DEMO HO GAYI! Report ready hai!")

def save_report():
    text = result_box.get("1.0", tk.END)
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt")])
    if file:
        open(file, "w", encoding="utf-8").write(text)
        messagebox.showinfo("Saved", "Report save ho gayi!")

root = tk.Tk()
root.title("Multi-AI Agent - Cybersecurity Intelligence")
root.geometry("820x900")
root.configure(bg=BG)

# --- YAHAN AB CODE WALA BANNER HAI, PHOTO KI ZAROORAT NAHI ---
banner = tk.Frame(root, bg=DARK_BLUE, padx=10, pady=15)
banner.pack(fill="x", padx=10, pady=10)
tk.Label(banner, text="🛡️", font=("Arial", 35), bg=DARK_BLUE, fg="white").pack()
tk.Label(banner, text="MULTI-AI AGENT SYSTEM", font=("Arial", 22, "bold"), bg=DARK_BLUE, fg="#7dd3fc").pack()
tk.Label(banner, text="Cybersecurity Intelligence Report", font=("Arial", 14, "bold"), bg=DARK_BLUE, fg="white").pack()
tk.Label(banner, text="Phishing  |  Ransomware  |  Malware Detection", font=("Arial", 10), bg=DARK_BLUE, fg="#bae6fd").pack()

tk.Label(root, text="For Cybersecurity Intelligence | 3 AI Agents Working Together", font=("Arial", 11), bg=BG, fg=BLUE).pack()
frame = tk.Frame(root, bg=CARD, padx=15, pady=15)
frame.pack(padx=20, pady=10, fill="x")
tk.Label(frame, text="Groq API Key (Optional):", bg=CARD, fg="white", font=("Arial", 10, "bold")).pack(anchor="w")
key_entry = tk.Entry(frame, width=55, font=("Arial", 11), show="*")
key_entry.pack(pady=5)
tk.Label(frame, text="Kis attack ka check karna hai?", bg=CARD, fg="white", font=("Arial", 11, "bold")).pack(anchor="w")
entry = tk.Entry(frame, width=55, font=("Arial", 13))
entry.pack(pady=5)
entry.insert(0, "Phishing Attack")
btn_frame = tk.Frame(frame, bg=CARD)
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="🎬 LIVE DEMO Report", command=run_live_demo, bg=ORANGE, fg="white", font=("Arial", 12, "bold"), width=20).pack(side="left", padx=5)
tk.Button(btn_frame, text="💾 Save", command=save_report, bg=BLUE, fg="white", font=("Arial", 12, "bold"), width=10).pack(side="left", padx=5)
status_label = tk.Label(root, text="Ready ho! LIVE DEMO dabao!", bg=BG, fg="yellow", font=("Arial", 11))
status_label.pack()
result_box = scrolledtext.ScrolledText(root, width=90, height=20, font=("Arial", 10), bg="white")
result_box.pack(padx=20, pady=10)
tk.Label(root, text="Made by Nisha | Python + Multi-Agent System", bg=BG, fg="gray", font=("Arial", 9)).pack()
root.mainloop()