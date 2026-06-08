To run these code snippets locally instead of in Google Colab, you don't need to change a single line of the actual Python code. However, you do need to set up your local environment so your computer knows where to find those libraries.

Here is the exact step-by-step process to get everything running locally using Python 3.

---

### Step 1: Install the Libraries via your Terminal

Google Colab comes with these libraries pre-installed. Locally, you have to install them yourself using `pip` (Python's package installer).

Open your terminal (**Command Prompt/PowerShell** on Windows, or **Terminal** on Mac/Linux) and run the following command to install all of them at once:

```bash
pip install numpy pandas scikit-learn torch transformers tf-keras
```

> 💡 **A Quick Note on Hugging Face (transformers):** When running the Hugging Face snippet for the first time locally, it will automatically download the required model files (usually a few hundred megabytes) to your computer. It might take a minute or two to start up the first time, but it will run instantly on subsequent runs.

---

### Step 2: Choose How to Run the Code

You have two main options for running the code locally, depending on how you like to work:

#### Option A: Use Jupyter Notebooks (Closest to Colab)
If you like the "cell-by-cell" interface of Colab, you can install Jupyter Notebooks locally.

1. Run `pip install notebook` in your terminal.
2. Launch it by running `jupyter notebook`.
3. This will open a browser window where you can create a new notebook, paste the code, and run it exactly like Colab.

#### Option B: Use a Text Editor / IDE (Standard Software Engineering)
1. Download a code editor like **Visual Studio Code (VS Code)**.
2. Create a new file and save it with a `.py` extension (e.g., `ai_test.py`).
3. Paste any of the code snippets into the file.
4. Run the file from your terminal using Python 3:
   ```bash
   python ai_test.py
   ```

---

### Step 3: Understand the Output Differences

When you run the code locally, everything will behave exactly the same with two minor log differences:

* **GPU vs. CPU (torch snippet):** Unless you have a dedicated NVIDIA graphics card with CUDA configured on your local machine, `torch.cuda.is_available()` will output `False` locally (whereas Colab often provides a free cloud GPU which outputs `True`). Don't worry—the code will still run perfectly fine on your CPU.
* **Hugging Face Progress Bars:** The first time you run the `transformers` code, you will see a download progress bar in your terminal as it fetches the model.

---

### 🚀 Interview Pro-Tip: Virtual Environments

If a technical interviewer asks how you manage your local Python projects, **never** say you just install everything globally.

Instead, mention that you use **Virtual Environments** (`venv` or `conda`) to keep your project dependencies isolated. It shows great engineering hygiene.

Before running the `pip install` command above, a pro developer would do this:

```bash
# 1. Create an isolated environment named 'ai_env'
python -m venv ai_env

# 2. Activate it (Windows)
ai_env\Scripts\activate

# ...or Activate it (Mac/Linux)
source ai_env/bin/activate

# 3. Now install your libraries safely inside this environment!
```