# Handwritten Bengali Alphabets, Compound Characters, and Numerals Recognition Using CNN

[![DOI](https://img.shields.io/badge/DOI-10.33166/AETiC.2023.03.003-blue)](http://aetic.theiaer.org/archive/v7/v7n3/p3.html)

## Overview
Recognizing **user-independent handwritten Bengali characters and numerals** is a challenging task due to:
- Complex-shaped compound characters.
- Variations in writing styles from different authors.
- Large number of character classes.

This project proposes a **lightweight Convolutional Neural Network (CNN)** approach for accurate classification of:
- Simple Bengali characters  
- Compound Bengali characters  
- Bengali numerals  

Our model outperforms many existing frameworks, delivering **higher accuracy, faster execution, and fewer training epochs**. It has been evaluated on **three datasets**.

## Features
- **Lightweight CNN architecture** for high accuracy and low computational cost.
- Works with multiple datasets without major modifications.
- Supports **84-character**, **60-character**, and **50-character** classification tasks.
- Achieves high validation accuracy with fewer epochs.

## Datasets Used
1. **BanglaLekha Isolated**
   - 84-character classes  
   - Validation Accuracy: **92.48%**
2. **Ekush**
   - 60-character classes  
   - Validation Accuracy: **97.24%**
3. **Custom Dataset**
   - 50-character classes  
   - Validation Accuracy: **97.03%**

## Methodology
- **Model Type:** Convolutional Neural Network (CNN)
- **Approach:**
  - Preprocessing: Grayscale conversion, normalization, and resizing.
  - CNN Layers: Stacked convolution + pooling layers.
  - Fully connected layers for classification.
- **Loss Function:** Categorical Crossentropy
- **Optimizer:** Adam
- **Metrics:** Accuracy

## Installation
```bash
git clone https://github.com/your-username/bangla-handwritten-recognition.git
cd bangla-handwritten-recognition
pip install -r requirements.txt
