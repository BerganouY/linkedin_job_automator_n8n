# LinkedIn Job Automator

This project is a web-based interface for a LinkedIn job automation workflow. It allows users to scrape job postings from LinkedIn, generate personalized email drafts for job applications using an AI agent, and send them.

## Table of Contents

- [LinkedIn Job Automator](#linkedin-job-automator)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [To-Do](#to-do)
  - [Architecture](#architecture)
    - [Data Flow](#data-flow)
  - [Workflow](#workflow)
  - [Technical Stack](#technical-stack)
  - [Setup and Installation](#setup-and-installation)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [n8n Workflow Setup](#n8n-workflow-setup)
    - [Running the Application](#running-the-application)
  - [Usage](#usage)
  - [Security Note](#security-note)
  - [Contributing](#contributing)
  - [License](#license)

## Features

*   **Job Scraping:** Scrape job postings from a LinkedIn Jobs search URL.
*   **AI-Powered Email Generation:** Automatically generate personalized email drafts for job applications using a Google Gemini model.
*   **Interactive UI:** A user-friendly web interface to manage the job application process.
*   **n8n Workflow Integration:** The application is powered by an n8n workflow that automates the scraping and email generation process.

## To-Do

- [ ] **Improve the UI:** The current UI is functional but could be improved with a more modern design.
- [ ] **Add more AI providers:** Add support for other AI providers like OpenAI's GPT-3.
- [ ] **Add more job boards:** Add support for other job boards like Indeed, Glassdoor, etc.
- [ ] **Add a database:** Add a database to store the job postings and application status.
- [ ] **Add user authentication:** Add user authentication to allow users to save their job applications.

## Architecture

The application consists of three main components:

1.  **Frontend:** A single-page application built with HTML, Bootstrap, and vanilla JavaScript that provides the user interface.
2.  **Backend:** A Python Flask application that serves the frontend and acts as a proxy between the frontend and the n8n workflow.
3.  **n8n Workflow:** An n8n workflow that orchestrates the job scraping, email generation, and email sending processes.

### Data Flow

Frontend -> Flask Backend -> n8n Webhook -> Flask Backend -> Frontend

## Workflow

1.  The user enters a LinkedIn job search URL in the frontend and clicks "Start Search".
2.  The frontend sends the URL to the Flask backend's `/api/search` endpoint.
3.  The Flask backend forwards the URL to the n8n "search-jobs" webhook.
4.  The n8n workflow triggers an Apify actor to scrape the LinkedIn jobs.
5.  The job data is returned to the frontend and displayed as job cards.
6.  The user clicks "Generate Draft" on a job card.
7.  The frontend sends the job title, company name, and job description to the Flask backend's `/api/generate-email` endpoint.
8.  The Flask backend forwards the data to the n8n "generate-draft" webhook.
9.  The n8n workflow uses a Google Gemini model to generate a personalized email draft.
10. The draft is displayed in a modal in the frontend.
11. The user can edit the draft and click "Send Application".
12. The frontend sends the edited email body, job title, and company name to the Flask backend's `/api/send-email` endpoint.
13. The Flask backend forwards the data to the n8n "send-email" webhook.
14. The n8n workflow sends the email using the Gmail API.

## Technical Stack

*   **Backend:** Python, Flask
*   **Frontend:** HTML, Bootstrap 5, Vanilla JavaScript
*   **Automation:** n8n
*   **AI:** Google Gemini
*   **Scraping:** Apify

## Setup and Installation

### Prerequisites

*   Python 3.x
*   n8n instance (local or cloud)
*   Apify account and API token
*   Google Gemini API key
*   Gmail account connected to n8n

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/BerganouY/linkedin_job_automator_n8n.get
    cd linkedin_job_automator_n8n
    ```

2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### n8n Workflow Setup

1.  **Import the workflow:**
    *   Open your n8n instance.
    *   Go to "Workflows" and click "Import from File".
    *   Select the `LinkedInJobautomationInterface.json` file.

2.  **Configure the workflow:**
    *   **N8N_BASE_URL:** Set the `N8N_BASE_URL` environment variable to your n8n instance URL (e.g., `http://localhost:5678`). The application will use this to construct the webhook URLs.
    *   **Apify API Token:** In the "HTTP Request4" node, replace the hardcoded Apify token in the URL with your own Apify API token.
    *   **Google Gemini API Key:** In the "Google Gemini Chat Model1" and "Google Gemini Chat Model2" nodes, create new credentials and add your Google Gemini API key.
    *   **Gmail Credentials:** In the "Send a message" node, create new credentials and connect your Gmail account.

### Running the Application

1.  **Start the Flask application:**
    ```bash
    python3 app.py
    ```
    The application will be running at `http://localhost:5001`.

2.  **Activate the n8n workflow:**
    *   Open the imported workflow in n8n.
    *   Click the "Active" toggle to activate the workflow.

## Usage

1.  Open your web browser and go to `http://localhost:5001`.
2.  Enter a LinkedIn job search URL in the search bar and click "Start Search".
3.  The scraped jobs will be displayed as cards.
4.  Click the "Generate Draft" button on a job card to generate an email draft.
5.  The AI-generated draft will be displayed in a modal. You can edit the text in the modal.
6.  Click the "Send Application" button to send the email.

## Security Note

> [!WARNING]
> The Apify API token is currently hardcoded in the n8n workflow (`LinkedInJobautomationInterface.json`). It is recommended to store the token in a secure way, for example as an n8n credential or an environment variable.