# LinkedIn Job Automator

This project is a web-based interface for a LinkedIn job automation workflow. It allows users to scrape job postings from LinkedIn, generate personalized email drafts for job applications using an AI agent, and send them.

## Features

*   **Job Scraping:** Scrape job postings from a LinkedIn Jobs search URL.
*   **AI-Powered Email Generation:** Automatically generate personalized email drafts for job applications using a Google Gemini model.
*   **Interactive UI:** A user-friendly web interface to manage the job application process.
*   **n8n Workflow Integration:** The application is powered by an n8n workflow that automates the scraping and email generation process.

## Architecture

The application consists of three main components:

1.  **Frontend:** A single-page application built with HTML, Bootstrap, and vanilla JavaScript that provides the user interface.
2.  **Backend:** A Python Flask application that serves the frontend and acts as a proxy between the frontend and the n8n workflow.
3.  **n8n Workflow:** An n8n workflow that orchestrates the job scraping, email generation, and email sending processes.

The data flow is as follows:

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
    git clone <repository-url>
    cd JobAutomation_Interface
    ```

2.  **Install Python dependencies:**
    ```bash
    pip install -r linkedin_job_automator/requirements.txt
    ```

### n8n Workflow Setup

1.  **Import the workflow:**
    *   Open your n8n instance.
    *   Go to "Workflows" and click "Import from File".
    *   Select the `linkedin_job_automator/LinkedInJobautomationInterface.json` file.

2.  **Configure the workflow:**
    *   **Apify API Token:** In the "HTTP Request4" node, replace the hardcoded Apify token in the URL with your own Apify API token.
    *   **Google Gemini API Key:** In the "Google Gemini Chat Model1" and "Google Gemini Chat Model2" nodes, create new credentials and add your Google Gemini API key.
    *   **Gmail Credentials:** In the "Send a message" node, create new credentials and connect your Gmail account.

### Running the Application

1.  **Start the Flask application:**
    ```bash
    python3 linkedin_job_automator/app.py
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

The Apify API token is currently hardcoded in the n8n workflow (`linkedin_job_automator/LinkedInJobautomationInterface.json`). It is recommended to store the token in a secure way, for example as an n8n credential or an environment variable.
