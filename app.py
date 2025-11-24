import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- CONFIGURATION ---
# Replace with your local or cloud n8n URL
N8N_BASE_URL = "http://localhost:5678/webhook"

# Map to the specific paths we defined in the instructions above
N8N_WEBHOOKS = {
    "SEARCH": "http://localhost:5678/webhook-test/search-jobs",
    "GENERATE": "http://localhost:5678/webhook-test/generate-draft",
    "SEND": "http://localhost:5678/webhook-test/send-email"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search_jobs():
    linkedin_url = request.json.get('url') # The frontend sends 'url'
    
    if not linkedin_url:
        return jsonify({"error": "URL is required"}), 400

    try:
        # We send 'url' to n8n. 
        # The n8n HTTP Request node will wrap this into the Apify format.
        response = requests.post(N8N_WEBHOOKS['SEARCH'], json={
            "url": linkedin_url
        })
        response.raise_for_status()
        return jsonify(response.json())
        
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/generate-email', methods=['POST'])
def generate_email():
    """
    Triggers 'Webhook1' -> 'AI Agent1'.
    """
    data = request.json
    
    payload = {
        "Title": data.get("Title"),
        "Company Name": data.get("CompanyName"), 
        "Job description": data.get("JobDescription")
    }

    try:
        response = requests.post(N8N_WEBHOOKS['GENERATE'], json=payload)
        response.raise_for_status()
        
        # --- FIX: UNWRAP N8N LIST ---
        n8n_data = response.json()
        
        # If n8n returns a list like [{"output": "..."}], grab the first item
        if isinstance(n8n_data, list) and len(n8n_data) > 0:
            return jsonify(n8n_data[0])
            
        # Otherwise return as is
        return jsonify(n8n_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/send-email', methods=['POST'])
def send_email():
    """
    Triggers 'Webhook2'.
    IMPORTANT: Connect Webhook2 directly to Gmail node in n8n to send the edited text.
    """
    data = request.json
    
    payload = {
        "output": data.get("emailBody"),    # The edited text from UI
        "Title": data.get("Title"),         # Used for Subject line in Gmail node
        "Company Name": data.get("CompanyName"),
        "Company Email": data.get("companyEmail") # NEW: Sending the extracted email
    }
    
    try:
        response = requests.post(N8N_WEBHOOKS['SEND'], json=payload)
        response.raise_for_status()
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)