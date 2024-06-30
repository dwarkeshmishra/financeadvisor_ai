from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import LlamaForCausalLM, LlamaTokenizer
import torch

app = Flask(__name__)
CORS(app)

# Load model and tokenizer
tokenizer = LlamaTokenizer.from_pretrained("huggyllama/llama-7b")
model = LlamaForCausalLM.from_pretrained("huggyllama/llama-7b")

@app.route('/api/getAdvice', methods=['POST'])
def get_advice():
    input_data = request.json
    input_text = input_data.get('input', '')
    if not input_text:
        return jsonify({'error': 'Input is required'}), 400

    inputs = tokenizer(input_text, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=150)

    advice = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({'advice': advice})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
