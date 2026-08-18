# NumGuesser: Number Guessing Game Application

A full-stack web application featuring an interactive number guessing game where players try to guess a randomly generated number between 1 and 50 within a limited number of attempts.

Live Demo: https://numguesser-demo.com  
Frontend Repo: https://github.com/your-username/numguesser-frontend  
Backend Repo: https://github.com/your-username/numguesser-backend  

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Database Design](#database-design)
- [API Endpoints](#api-endpoints)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Deployment](#deployment)
- [Future Improvements](#future-improvements)
- [Credits](#credits)
- [License](#license)

---

## Overview

### Motivation
Built as a fun, lightweight logic challenge, this project transforms a classic console guessing game into a full-featured web experience complete with progress tracking and persistent leaderboards.

### Objective
To provide an engaging interactive platform where users guess a secret number between 1 and 50, receive real-time "too high" or "too low" hints, and track their best attempt scores.

### Learning Outcomes
- Built full authentication system with JWT
- Designed RESTful API endpoints for game sessions and score submissions
- Implemented core game logic controllers for random number generation and validation checks
- Connected a React frontend to a Node/Express backend API
- Deployed a full-stack web application

---

## Features

- **Interactive Number Guesser:** Real-time feedback ("Too High!", "Too Low!", or "Correct!") for guesses between 1 and 50.
- **Attempt Tracker:** Counts and displays the number of tries taken to find the correct number.
- **User Authentication:** Secure registration, login, and logout functionality.
- **Score History & Leaderboard:** Track personal best scores and compete on a global high-score board.
- **Fully Responsive Design:** Optimized for mobile touchscreens, tablets, and desktop browsers.

---

## Tech Stack

### Core Language

Python 3

Machine Learning & Data Science Libraries
scikit-learn 1.4.2 pandas numpy matplotlib joblib

### Specific ML Components (from scikit-learn)

gradientboostingregressor columntransformer selectpercentile

### Web Framework

streamlit

### Development Environment

jupyter notebook venv (virtual environment)

### Storage & Infrastructure
Azurite Queue Storage

### Data

CSV files
---

### Folder Structure

```text
client/
server/
  ├── controllers/
  │         └── gameController.js
  ├── routes/
  │         └── gameRoutes.js
  ├── models/
  │         └── Score.js
  ├── middleware/
  │         └── authMiddleware.js
  └── config/
            └── db.js
