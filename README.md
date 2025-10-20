# UniMERT (Unified Multimodal Emotion Recognition Transformer)

Overview : 



UniMERT is an experimental research project aimed at recreating and extending the Dynamic Fusion Graph (DFG) architecture for multimodal emotion and sentiment recognition using the CMU-MOSEI dataset. Since the original DFG implementation is not open-source, this project builds it from scratch, leveraging the pre-extracted and transformed features for text (BERT), audio (COVAREP), and visual (OpenFace2) modalities. The ultimate goal is to train a machine learning model that dynamically selects and fuses the most informative modalities for a given utterance, thereby improving the accuracy and robustness of emotion and sentiment classification.



Past :



-> The CMU-MOSEI dataset is a benchmark dataset for multimodal sentiment and emotion recognition, containing synchronized text, audio, and visual features for over 23,000 video utterances.

-> The Dynamic Fusion Graph (DFG) architecture, introduced in research papers, achieves state-of-the-art performance by dynamically deciding which modalities to fuse for each prediction.

-> The original DFG implementation was not open-source, making replication and experimentation difficult.



Present :



-> We have obtained preprocessed .csd files containing feature representations for each modality:
    
    <1> Text -> Timestamped BERT embeddings
    
    <2> Audio -> COVAREP acoustic features

    <3> Visual -> OpenFace2 facial feature embeddings


-> We are writing our own HDF5 to CSV extraction pipeline to make the data easy to load into PyTorch/TensorFlow.

-> The DFG architecture is being rebuilt locally using LSTM-based multimodal modules and a graph-based fusion layer.

-> The system will be trained to predict both emotion categories and sentiment polarity.



Future :

-> Full DFG implementation with trainable fusion gates that learn which modality combinations yield the best performance per utterance.

-> End-to-end training pipeline on CMU-MOSEI with our custom DFG model.

-> Performance comparison with other multimodal fusion methods such as Late Fusion and Tensor Fusion Network.

-> Potential extension to real-time emotion recognition for human-compute interaction applications. 

-> Publication of a fully documented, open-source repository for researchers and    developers to build upon.


Current Status :

1) CSD feature extraction to CSV in progress

2) Implementing DFG LSTM Modules and graph fusion logic

3) Preparing training and evaluation pipelines

Planned Output : 

1) Emotion classification -> Anger, Disgust, Fear, Happiness, Sadness, Surprise

2) Sentiment classification -> Negative, Neutral, Positive

3) Modular architecture for easy experimentation


