from flask import Flask

# Create the Flask web server application
app = Flask(__name__)

# A simple test route to confirm the service is running
@app.route('/')
def health_check():
    return "Document Converter service is running."

# The endpoint that will receive the Markdown and create the DOCX file later
@app.route('/create-docx', methods=['POST'])
def create_docx():
    # We will add the conversion logic in our next step
    return "Request received. DOCX generation is coming soon!"

# This runs the server and makes it accessible
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)