
<p align="center">
  <img src="https://img.shields.io/badge/Project-Garbage%20Classifier-black?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/github/license/AditixAnand/Garbage_Classification?style=for-the-badge">
  <img src="https://img.shields.io/badge/Accuracy-98%25-brightgreen?style=for-the-badge">
</p>

<h1 align="center">♻️ Garbage Classifier with Transfer Learning</h1>

<p align="center">
  A smart, AI-powered waste classification system that sees trash... and thinks clean!  
  Built to sort six types of waste using powerful transfer learning models.  
</p>

<p align="center">
  <img src="https://repository-images.githubusercontent.com/196177966/c3c40900-a326-11e9-9d7e-0d25b66490ff" width="80%" alt="Model Preview">
</p>

---

## 📚 Table of Contents

- [🧭 Why This Project?](#-why-this-project)
- [🔍 What Can It Detect?](#-what-can-it-detect)
- [🧠 Inside the Model](#-inside-the-model)
- [📂 Project Layout](#-project-layout)
- [🚀 Live Demo](#-live-demo)
- [💡 Features At A Glance](#-features-at-a-glance)
- [🛠 Built With](#-built-with)
- [💬 Community & Feedback](#-community--feedback)
- [🤝 How to Contribute](#-how-to-contribute)
- [📄 License](#-license)
- [🏆 Recognition](#-recognition)

---

## 🧭 Why This Project?

Every piece of garbage matters.  
Improper sorting leads to overflowing landfills and wasted recyclables.  
This project brings **machine learning** to the front lines of sustainability, helping automate and **simplify waste classification**.

🧠 Built during the **Shell-Edunet Skills4Future Internship (June–July 2025)**.

---

## 🔍 What Can It Detect?

The AI model classifies any uploaded garbage image into:

| Category   | Example Items               |
|------------|-----------------------------|
| 🟫 Cardboard | Boxes, cartons               |
| 🟡 Plastic   | Bottles, containers          |
| 📰 Paper     | Newspapers, wrappers         |
| 🔩 Metal     | Cans, utensils               |
| 🟢 Glass     | Jars, shattered pieces       |
| 🗑️ Trash     | Everything else non-recyclable |

---

## 🧠 Inside the Model

| Feature              | Description                                      |
|----------------------|--------------------------------------------------|
| 📦 Architecture       | **EfficientNetV2B2** (state-of-the-art)         |
| 🔄 Transfer Learning | Pretrained on ImageNet, fine-tuned for trash     |
| 📱 Interface         | Gradio / Streamlit for live predictions          |
| 📈 Accuracy          | **98%** on validation                            |
| 🆚 Baseline          | Compared against **MobileNetV2**                 |

---

## 📂 Project Layout

```bash
Garbage_Classification/
├── Week1/                 # Research & setup
├── Week2/                 # Model experimentation
├── Week3/                 # Evaluation & UI
├── Dataset/               # Preprocessed images
├── app.py                 # Gradio or Streamlit app
├── model_efficientnet.h5  # Trained weights
└── README.md
```

---

## 🚀 Live Demo

🎯 **Try It Out Yourself**  

Run locally:

```bash
# Install required libraries
pip install -r requirements.txt

# Launch the app
streamlit run app.py
```

---

## 💡 Features At A Glance

✅ Real-time garbage prediction  
🌍 Contributes to smart waste segregation  
⚙️ Based on clean modular code  
📊 Great for learning CNN + Transfer Learning  
🚮 Encourages environmental awareness

---

## 🛠 Built With

| Tool        | Role                         |
|-------------|------------------------------|
| 🐍 Python   | Core scripting language       |
| 🔬 TensorFlow | Model training + inference   |
| 🧰 Keras     | Transfer learning pipelines   |
| 💬 Gradio/Streamlit | Web deployment & UI        |

---

## 💬 Community & Feedback

Got feedback? Found a bug? Want to contribute?

| 📌 Platform | Use Case                      |
|------------|-------------------------------|
| [GitHub Issues](https://github.com/AditixAnand/Garbage_Classification/issues) | Bug reports, feature requests |
| [Discussions](https://github.com/AditixAnand/Garbage_Classification/discussions) | Ideas, questions, suggestions |

---

## 🤝 How to Contribute

We love meaningful contributions!

```bash
# 1. Fork it
# 2. Create a new branch
git checkout -b feature/amazing-feature

# 3. Make your changes
git commit -m "✨ Add amazing feature"

# 4. Push & submit PR
git push origin feature/amazing-feature
```

📘 Check out [`CONTRIBUTING.md`](./CONTRIBUTING.md) for more.

---

## 📄 License

📜 Open-source under the **MIT License** — free to use, improve, and distribute.

---

## 🏆 Recognition

This project was proudly developed as part of the:

> 🛢️ **Shell-Edunet Skills4Future Internship**  
> Supporting real-world AI innovation for sustainability.

<p align="center">
  <img src="https://img.shields.io/badge/Sustainability-Focused-green?style=for-the-badge">
</p>

---



<p align="center">
  Made with 🧠 and ♻️ by <a href="https://github.com/AditixAnand">Aditix Anand</a> & Contributors
</p>


<p align="center">
  <a href="#top" style="font-size: 16px; padding: 8px 16px; border: 1px solid #ccc; border-radius: 6px; text-decoration: none;">
    ⬆️ Back to Top
  </a>
</p>
