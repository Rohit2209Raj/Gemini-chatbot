---

title: Gemini Chatbot
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: streamlit
app_file: app.py
pinned: false
---

# 🤖 Gemini Chatbot

A full-stack AI chatbot application built using **Streamlit + FastAPI + Google Gemini API**, featuring authentication flow, API validation, and a clean chat interface.

## 🚀 Live Demo

👉 Add your Hugging Face Space URL here

Example:

https://huggingface.co/spaces/YudiCadini/Gemini-Chatbot

# ✨ Features

* 🔐 User login and verification flow
* 🤖 AI-powered conversations using Gemini
* ⚡ FastAPI backend for API handling
* 🎨 Streamlit frontend for interactive UI
* 🔑 Secure API key management using environment variables / secrets
* ☁️ Deployable on Hugging Face Spaces

---

# 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* Uvicorn

### AI

* Google Gemini API

### Utilities

* Python
* Requests
* Python Dotenv

---

# 📂 Project Structure

```plaintext
Gemini-Chatbot/
│
├── app.py
├── main.py
├── chat.py
├── verify.py
├── requirements.txt
│
├── pages/
│   ├── streamlit_login.py
│   └── streamlit_chat.py
```

---

# ⚙️ Installation

Clone repository:

```bash
git clone <your-repository-url>
cd Gemini-Chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env`:

```env
GEMINI_API_KEY=your_api_key_here
```

Run application:

```bash
streamlit run app.py
```

---

# 🎯 What I Learned

* Full-stack AI application architecture
* Integrating Gemini APIs
* Streamlit multi-page applications
* FastAPI backend integration
* Deployment and environment management
* Debugging production deployment issues

---

# 📌 Future Improvements

* Conversation history
* Chat memory
* Better authentication
* File upload support
* Responsive UI enhancements

---

# 👨‍💻 Author

YudiCadini

If you found this project useful, consider starring the repository ⭐
