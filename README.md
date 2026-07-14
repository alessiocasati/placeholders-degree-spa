# 🎓 Graduation Day - Dynamic Personalized Placeholders

![License](https://img.shields.io/badge/license-MIT-green)
![No Dependencies](https://img.shields.io/badge/dependencies-zero-blue)
![Made with](https://img.shields.io/badge/made%20with-HTML5%20%7C%20CSS3%20%7C%20JS%20%7C%20Python-orange)
![Status](https://img.shields.io/badge/status-completed-brightgreen)

A lightweight, mobile-first Single Page Application (SPA) designed to welcome graduation guests with personalized dynamic content. Built entirely in **Vanilla JS (ES6+)** and **pure CSS3**, this project showcases how to deliver an engaging, app-like user experience without the overhead of heavy modern frameworks.

<p align="center">
  <img src="./resources/img/avatar/alessio-avatar.png" alt="Alessio - Caricature" width="100" style="filter: drop-shadow(0px 10px 15px rgba(0,0,0,0.3));">
</p>

---

## 💡 Why I Built This

For my graduation party, I wanted table placeholders that felt personal rather than printed name cards. Each guest scans a QR code and lands on a page built just for them: a personalized greeting, followed by a short explanation of a topic tailored to how well they know the subject.

It was also a chance to prove to myself that I could deliver a polished, app-like mobile experience using **only core web technologies** — no framework, no build step, no dependencies — while still following solid software engineering practices (separation of concerns, componentized rendering, clean routing).

---

## ✨ Features

- 🔗 **Personalized deep links** — each guest gets a unique URL that renders their own greeting and content
- 🎨 **Light & dark theme support** with CSS variables for easy customization
- ⚡ **Hash-based SPA routing** — instant transitions, no full page reloads
- 🎬 **Two-phase hardware-accelerated animations** (elastic intro → content reveal)
- 🖨️ **Batch QR code generation** via a Python automation script, ready for print
- 📱 **Mobile-first**, zero-dependency front end

---

## 📸 Preview

<p align="center">
  <img src="./resources/img/preview/demo-welcome.jfif" alt="Demo Welcome" width="200" style="filter: drop-shadow(0px 10px 15px rgba(0,0,0,0.3));">
  <img src="./resources/img/preview/demo-topic.jfif" alt="Demo Welcome" width="200" style="filter: drop-shadow(0px 10px 15px rgba(0,0,0,0.3));">
</p>

---

## 🚀 Live Demo

The application is deployed and accessible on mobile devices via GitHub Pages.
👉 **[Link to Live Demo](https://alessiocasati.github.io/placeholders-degree-spa/)**

---

## 🛠️ Tech Stack & Philosophy

This project was built with a strict **zero-dependency** approach to demonstrate mastery over core Web APIs and browser performance optimization:

* **HTML5 & CSS3:** Responsive layouts using Flexbox, CSS Variables for easy theming, and optimized hardware-accelerated animations.
* **Vanilla JavaScript (ES6+):** Dynamic DOM manipulation, template literals for modular component rendering, and custom state management.
* **Python 3:** Automation scripting for batch generation of print-ready QR codes.
* **No Frameworks:** No React, Vue, or Tailwind. Just clean, raw, and performant web technologies.

---

## 📦 Project Structure

```text
├── index.html              # Main entry point (minimal layout)
├── src/
│   ├── home.js             # Core app logic & Hash-based SPA routing controller
│   └── pages/
│       ├── welcome.js      # Dynamic welcome stage component
│       └── topic.js        # Topic explanation component
├── resources/
│   ├── data/
│   │   ├── content.json    # Centralized text content for UI (i18n ready)
│   │   └── guests.json     # Centralized database of guests and topic associations
│   ├── css/
│   │   ├── dark-style.css  # Dark theme styling, resets and animations
│   │   └── light-style.css # Light theme styling, resets and animations
│   └── img/
│       ├── avatar/         # Avatar and profile assets
│       ├── logo/           # Laurel logo for qr code decoration
│       └── topics/         # Topic-specific visual assets
├── utils/
│   └── qr_generator.py     # Python automation script for batch QR code generation
├── .env.example            # Example environment variables template
├── .gitignore              # Git ignore file (excludes venv and generated QR codes)
└── LICENSE                 # MIT License
```

---

## 🔧 Local Setup

To run this project locally, you don't need `npm` or any build tools. Simply clone the repository and spin up a local development server.

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
2. Enter the directory:
   ```bash
   cd your-repo-name
   ```
3. Start a lightweight Python local server:
   ```bash
   python3 -m http.server 8000
   ```
4. Open your browser and navigate to:
   ```text
   http://localhost:8000/#<guest-id>
   ```

---

## 🖨️ QR Code Automation

To facilitate the creation of physical placeholders for the tables, the project includes a Python automation script inside the `utils/` folder. It reads the `guests.json` database and batch-generates high-resolution, print-ready QR codes for each guest.

### Setup & Execution

1. **Configure Environment Variables:**
   Copy the example environment file to create your local configuration:
   ```bash
   cp .env.example .env.local
   ```
   Edit `.env.local` and set your `BASE_URL` (e.g., your GitHub Pages URL). Ensure it ends with a trailing slash (`/`).

2. **Create a Virtual Environment (Recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install qrcode python-dotenv Pillow
   ```

4. **Run the Script:**
   ```bash
   python3 utils/qr_generator.py
   ```

Upon successful execution, the script will create a `resources/img/qrcodes/` directory containing all the generated `.png` files, ready for typography printing.

**Requirements:** Python 3.9+

---

## 📐 Software Architecture & Design Patterns

The codebase is structured around key software engineering principles to ensure maintainability, scalability, and clean execution:

### 1. Separation of Concerns (SoC)
* **JavaScript** is strictly responsible for **logic and data orchestration**. HTML templates are injected dynamically based on the guest's unique identifier.
* **CSS** is strictly responsible for **presentation, responsiveness, and timing**. No inline styles are injected via JS; instead, UI states are triggered by toggling CSS classes.

### 2. Hash-Based Client-Side Routing
To deliver a true Single Page Application (SPA) experience on mobile, the app utilizes native window hash monitoring:

```javascript
window.addEventListener('hashchange', router);
```

This allows deep-linking and personalized routing without triggering full page reloads, ensuring instant transitions.

### 3. Hardware-Accelerated 2-Phase CSS Animations
To optimize performance on low-end mobile devices, animations rely exclusively on `transform` and `opacity` properties, which run directly on the GPU:
* **Phase 1 (Intro):** An elastic, spring-like scale entrance that puts the avatar and a personalized greeting at the center of the screen.
* **Phase 2 (Collapse & Content Reveal):** A smooth height adjustment that seamlessly scales down the avatar to make room for the main graduation topic explanation, maintaining vertical rhythm without scroll overflow.

---

## 🔭 Lessons Learned & Possible Improvements

Building this without a framework was a deliberate constraint to sharpen my understanding of core browser APIs. Looking back, a few things I'd explore next:

- Add a small suite of unit tests for the routing and data-loading logic
- Evaluate TypeScript for stronger type safety in the state management layer
- Extract the QR generation script into a small CLI with configurable output formats (SVG in addition to PNG)
- Add automated accessibility checks (contrast, focus order) for the light/dark themes

---

## 📄 License
This project is open-source and available under the **MIT License**.

---

## 👤 Author

**Alessio Casati**

_Feel free to reach out if you have questions about the project or want to collaborate!_
