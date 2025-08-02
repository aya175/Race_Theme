# 🏎️ Formula 1 Engineering Challenges – Python Edition

Welcome to the **F1 Engineering Mini-Projects**!
This repo includes **three exciting Python challenges** inspired by real Formula 1 race engineering tasks.
Each task is designed to level up your coding skills while simulating real-world F1 tech features.

---

## 🚦 **Task 1.1 – Steering Wheel Digital Gear Indicator**

### 📜 **Description**

Every F1 car’s steering wheel has a **gear indicator** that shows which gear the driver is currently in.
Your task is to **program a Python script that simulates this gear display** using a **7-segment ASCII output** in the console.

### 🛠️ **Features**

* Takes **gear input (0–8)** where `0 = Neutral`.
* Displays the gear visually using a **5x4 grid made of `#` characters**.
* Prompts the user dynamically to **enter a gear number**.
* **Bonus:**

  * Handles invalid inputs like letters or numbers outside `0-8`.
  * Adds a **gear shift animation** to simulate real-time gear changes.

---

## 📡 **Task 1.2 – Secure Race Radio Transmission Protocol**

### 📜 **Description**

Race engineers send **critical commands** to drivers (like `"Push now"` or `"Box, box"`) via radio during a race.
Your task is to create a **data transmission protocol** to **encode and decode** these commands safely.

### 🛠️ **Features**

* Implements a **Codec class** with:

  * `encode()` → Converts a list of commands into a single transmittable string.
  * `decode()` → Converts the encoded string back into the **original list** perfectly.
* Works with **any type of command string**, including:

  * Empty strings
  * Numbers
  * Special characters
* Interactive input format:

```bash
Input: ["Push","Box,box","Push","Overtake"]
Output: ["Push","Box,box","Push","Overtake"]
```

* Guarantees **no data loss** in transmission.

---

## 🏁 **Task 1.3 – The Final Race: Verstappen vs Mostafa**

### 📜 **Description**

Step into the **Silverstone Circuit** where **Max Verstappen and Hassan Mostafa** face off in a head-to-head Formula 1 showdown.
Your mission is to build a **turn-based race simulator** using **Object-Oriented Programming (OOP)** principles.

### 🛠️ **Core Features**

* Each racer has:

  * **Tire Health** (0–100)
  * **Fuel** (0–500)
  * **Unique offensive and defensive moves** with different costs and effects.
* Players take turns attacking or defending until one racer’s tires reach `0`.
* Uses **OOP concepts**:

  * Abstraction
  * Inheritance
  * Polymorphism
  * Encapsulation

### 🎤 **Bonus Feature – Voice Control (STT Integration)**

* Hassan Mostafa’s moves are **controlled by your voice** using:

  * `SpeechRecognition` for mic input
  * **Groq API (Whisper model)** for real-time speech-to-text conversion
* Speak commands like:

  * `"Turbo Start"`
  * `"Mercedes Charge"`
  * `"Corner Mastery"`
* Watch your spoken words **trigger race actions live in the console**.

---

## ⚙️ **How to Run**

1. Clone this repo:

```bash
git clone https://github.com/aya175/Race_Theme.git
cd Race_Theme
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run each task:

```bash
python T1,1.py
python T1,2.py
python T1,3.py
```

4. For voice control in Task 1.3:

   * Plug in your mic 🎙️
   * Replace `"your_API_key"` in the script with your actual key
   * Run:

   ```bash
   python T1,3.py
   ```

---

## 🏆 **Skills You’ll Practice**

* Python scripting
* Data encoding/decoding
* Object-Oriented Programming
* Speech-to-Text integration with APIs
* Real-world problem-solving in F1 racing tech


