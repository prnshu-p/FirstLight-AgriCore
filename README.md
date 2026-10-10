# FirstLight-AgriCore 🌾🛰️

Core computational engine, satellite data ingestion pipeline, and predictive agricultural models for **Project First Light**.

---

## 🚀 Overview

`FirstLight-AgriCore` powers satellite telemetry ingestion, vegetation index analytics (NDVI), and predictive agricultural decision models.

## 🛠️ Project Structure (Target)

```text
FirstLight-AgriCore/
├── main.py              # Application entrypoint
├── nasa_api.py          # NASA / Satellite earth observation telemetry (Backend)
├── ndvi_calc.py         # Normalized Difference Vegetation Index calculations (Math)
├── assets/              # UI branding, color schemes, and design tokens
│   └── colors.txt
└── README.md
```

---

## ⚡ Git Workflow Rules (Trial by Fire)

1. **Never commit directly to `main`**: All features must go through a dedicated feature branch.
2. **Branch Naming Standard**:
   - `backend-<feature>` (e.g., `backend-init`)
   - `math-<feature>` (e.g., `math-models`)
   - `ui-<feature>` (e.g., `ui-assets`)
3. **Pull Requests (PR)**:
   - Always open a PR against `main`.
   - The Captain reviews and merges live.
   - Pull the latest `main` locally after every merge: `git pull origin main`.

---

## 👥 Core Team & Assignments

| Contributor | Role | Assigned Branch | Deliverable |
|-------------|------|-----------------|-------------|
| **Captain (Lead)** | System Architecture & Review | `main` | Base repo setup & PR Approvals |
| **Dharmik** | Backend & Satellite Telemetry | `backend-init` | `nasa_api.py` |
| **Pratham** | Mathematical & Agronomic Models | `math-models` | `ndvi_calc.py` |
| **Grecy** | UI/UX & Design Assets | `ui-assets` | Logo / `colors.txt` |

---

## 💻 Quickstart

```bash
# Clone the repository
git clone https://github.com/prnshu-p/FirstLight-AgriCore.git
cd FirstLight-AgriCore

# Run entry point
python main.py
```
