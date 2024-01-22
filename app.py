from flask import Flask, render_template, request
from transformers import pipeline
import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Load POS tagging model
pos_model = pipeline('token-classification', model='CAMeL-Lab/bert-base-arabic-camelbert-ca-pos-egy')

def generate_network_graph(pos_tags):
    G = nx.DiGraph()

    for i in range(len(pos_tags)):
        word = pos_tags[i]['word']
        pos_tag = pos_tags[i]['entity']

        G.add_node(word, pos=pos_tag)

        if i > 0:
            prev_word = pos_tags[i - 1]['word']
            G.add_edge(prev_word, word)

    pos_layout = nx.spring_layout(G)
    nx.draw(G, pos_layout, with_labels=True, font_weight='bold', node_size=1000, node_color='skyblue')
    plt.axis('off')

    img_stream = BytesIO()
    plt.savefig(img_stream, format='png')
    img_stream.seek(0)
    img_data = base64.b64encode(img_stream.read()).decode('utf-8')

    return f"data:image/png;base64,{img_data}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_sentence', methods=['POST'])
def process_sentence():
    sentence = request.form['sentence']
    pos_tags = pos_model(sentence)
    network_graph = generate_network_graph(pos_tags)
    return render_template('result.html', sentence=sentence, pos_tags=pos_tags, network_graph=network_graph)

if __name__ == '__main__':
    app.run(debug=True)
