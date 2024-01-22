# POS-tagging-Task

# Project Documentation

# Arabic Part-of-Speech Tagging with CAMeL-BERT

## Overview

This project focuses on Part-of-Speech (POS) tagging in Arabic text using the CAMeL-BERT model. POS tagging is a crucial step in natural language processing that involves assigning grammatical categories (such as nouns, verbs, or adjectives) to each word in a sentence. The CAMeL-BERT model is a pre-trained language model designed specifically for Arabic language processing.

## Purpose

The primary purpose of this project is to analyze the syntactic structure of Arabic sentences through POS tagging. By leveraging the capabilities of CAMeL-BERT, we aim to provide accurate and contextually meaningful POS tags for each word in a given text. This information can be valuable for various downstream NLP tasks, such as information extraction, sentiment analysis, and machine translation.

## Methodology

The project utilizes the CAMeL-BERT model through the Hugging Face Transformers library to perform POS tagging. The model is trained on a diverse range of Arabic language data, enabling it to capture intricate linguistic nuances and variations.

## POS Tagging Network Graph

One aspect of the project involves visualizing the relationships between words in a sentence through network graphs. This graphical representation showcases the syntactic connections between words and provides insights into the overall sentence structure. These graphs are generated based on the POS tags assigned by the CAMeL-BERT model.

## Sample Article Analysis

To demonstrate the effectiveness of CAMeL-BERT in a real-world scenario, the project includes an analysis of a sample Arabic article. The article is processed sentence by sentence, and the corresponding POS tags are extracted to showcase the model's performance on longer text segments.

## I have used both matplotlib and graphviz to make the network graph of the pos tagging

## Conclusion

Arabic Part-of-Speech Tagging with CAMeL-BERT contributes to the broader field of Arabic NLP by leveraging advanced pre-trained models. The project aims to enhance our understanding of Arabic language structures and facilitate more accurate language processing applications.







# Deployment
## The project was deployed through flask and containerized through using docker containers 

![lading page](https://github.com/Ma7moudYasser/POS-tagging-Task/assets/57537704/351bfedb-2436-4406-8314-691f03eb805d)


# Resources 
1. [Research Paper: CAMeLBERT - Arabic Language Model](https://arxiv.org/abs/2103.06678)
   - Access the research paper that introduces CAMeLBERT, the Arabic language model used in this project.

2. [CAMeLBERT GitHub Repository](https://github.com/CAMeL-Lab/CAMeLBERT/blob/master/text-classification/run_text_classification.py)
   - Explore the official GitHub repository for CAMeLBERT. The repository includes code examples, such as `run_text_classification.py`, demonstrating text classification using CAMeLBERT.

3. [CAMeL-Lab BERT-based Arabic POS Tagging Model](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-ca-pos-egy)
   - Check out the Hugging Face Model Hub page for the BERT-based Arabic POS tagging model by CAMeL-Lab. The page provides information on the model, its capabilities, and how to use it.


# Challenges
### The main in challenges in this project was the following
#### 1- Difficulty in finding the suitable dataset for the task and preprocessing it
#### 2- Lack of Resources as I have limited disk in google colab
#### 3- Lack of arabic resources to read solving this task



## Somethings new which I have learned 
### 1- The usage of graphviz 

## Tools 

1- [![Docker Logo](https://www.docker.com/sites/default/files/d8/2019-07/vertical-logo-monochromatic.png)](https://www.docker.com/)
2- [![Graphviz Logo](https://www.graphviz.org/Gallery/gradient_to.png)](https://www.graphviz.org/)
3- [![Matplotlib Logo](https://matplotlib.org/stable/_images/sphx_glr_logos2_003.png)](https://matplotlib.org/)
4- Hugging Face 



![result](https://github.com/Ma7moudYasser/POS-tagging-Task/assets/57537704/b5d299dd-cd6b-466c-b4c1-f9b07c8bde27)
