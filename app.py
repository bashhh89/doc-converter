import os
import pypandoc
from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime
import re

# Create the Flask web server application
app = Flask(__name__)

# Define a directory to save the output files
OUTPUT_DIR = '/app/output'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# This function takes the raw SOW markdown and extracts the title
def extract_title(markdown_text):
    match = re.search(r'^#\s*(.*)', markdown_text, re.MULTILINE)
    return match.group(1) if match else "Scope of Work"

@app.route('/create-docx', methods=['POST'])
def create_docx():
    try:
        # Get the raw markdown text from the request body
        markdown_text = request.data.decode('utf-8')
        if not markdown_text:
            return jsonify({"error": "No markdown content provided"}), 400

        # Define the output filename with a timestamp to make it unique
        timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        output_filename = f'SOW-{timestamp}.docx'
        output_filepath = os.path.join(OUTPUT_DIR, output_filename)
        
        # --- This is where the placeholder replacement will happen ---
        # In a future step, we will parse the markdown and replace the placeholders.
        # For now, we will just do a simple conversion.
        
        # This is the core pandoc conversion command.
        pypandoc.convert_text(
            markdown_text,
            'docx',
            format='md',
            outputfile=output_filepath,
            extra_args=[f'--reference-doc=/app/brand_template.docx']
        )

        # In the next step, we will return a real download link.
        # For now, we confirm creation.
        return jsonify({
            "status": "success",
            "message": f"DOCX file created successfully: {output_filename}",
        })

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)