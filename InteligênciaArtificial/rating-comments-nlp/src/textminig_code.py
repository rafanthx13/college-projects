import torch
from torch.utils.data import TensorDataset, DataLoader
import torch.nn as nn
import numpy as np
import pandas as pd
from string import punctuation

def classifica(test_review):
	
	vocab_to_int = pd.read_pickle('src/vocab_to_int')
	
	train_on_gpu = False
	
	dados= {'Inferencia':None , 'Resposta':None}
	
	
	class SentimentRNN(nn.Module):
	    """
	    The RNN model that will be used to perform Sentiment analysis.
	    """
	
	    def __init__(self, vocab_size, output_size, embedding_dim, hidden_dim, n_layers, drop_prob=0.5):
	        """
	        Initialize the model by setting up the layers.
	        """
	        super(SentimentRNN, self).__init__()
	
	        self.output_size = output_size
	        self.n_layers = n_layers
	        self.hidden_dim = hidden_dim
	        
	        # embedding and LSTM layers
	        self.embedding = nn.Embedding(vocab_size, embedding_dim)
	        self.lstm = nn.LSTM(embedding_dim, hidden_dim, n_layers, 
	                            dropout=drop_prob, batch_first=True)
	        
	        # dropout layer
	        self.dropout = nn.Dropout(0.5)
	        
	        # linear and sigmoid layers
	        self.fc = nn.Linear(hidden_dim, output_size)
	        self.sig = nn.Sigmoid()
	        
	
	    def forward(self, x, hidden):
	        """
	        Perform a forward pass of our model on some input and hidden state.
	        """
	        batch_sizes = x.size(0)
	
	        # embeddings and lstm_out
	        embeds = self.embedding(x)
	        lstm_out, hidden = self.lstm(embeds, hidden)
	    
	        # stack up lstm outputs
	        lstm_out = lstm_out.contiguous().view(-1, self.hidden_dim)
	        
	        # dropout and fully-connected layer
	        out = self.dropout(lstm_out)
	        out = self.fc(out)
	        # sigmoid function
	        sig_out = self.sig(out)
	        
	        # reshape to be batch_size first
	        sig_out = sig_out.view(batch_sizes, -1)
	        sig_out = sig_out[:, -1] # get last batch of labels
	        
	        # return last sigmoid output and hidden state
	        return sig_out, hidden
	    
	    
	    def init_hidden(self, batch_size):
	        ''' Initializes hidden state '''
	        # Create two new tensors with sizes n_layers x batch_size x hidden_dim,
	        # initialized to zero, for hidden state and cell state of LSTM
	        weight = next(self.parameters()).data
	        
	        if (train_on_gpu):
	            hidden = (weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().cuda(),
	                  weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().cuda())
	        else:
	            hidden = (weight.new(self.n_layers, batch_size, self.hidden_dim).zero_(),
	                      weight.new(self.n_layers, batch_size, self.hidden_dim).zero_())
	        
	        return hidden
	        
	#  Instancia o modelo com os parâmetros
	vocab_size = len(vocab_to_int) + 1
	output_size = 1
	embedding_dim = 200
	hidden_dim = 256
	n_layers = 2
	
	net = SentimentRNN(vocab_size, output_size, embedding_dim, hidden_dim, n_layers)
	
	
	
	#carrega o modelo treinado
	net.load_state_dict(torch.load('src/model.pt',map_location='cpu') )
	
	def pad_features(reviews_ints, seq_length):
	
	    features = np.zeros((len(reviews_ints), seq_length), dtype=int)
	
	    for i, row in enumerate(reviews_ints):
	        features[i, -len(row):] = np.array(row)[:seq_length]
	    
	    return features
	
	def tokenize_review(test_review):
	    test_review = test_review.lower() # lowercase
	    # get rid of punctuation
	    test_text = ''.join([c for c in test_review if c not in punctuation])
	
	    # splitting by spaces
	    test_words = test_text.split()
		

	    # tokens
	    test_ints = []
	    test_ints.append([vocab_to_int.get(word) for word in test_words if vocab_to_int.get(word) != None ])
	    
	
	    return test_ints
	
	def predict(net, test_review, sequence_length=20):
	    
	    net.eval()
	    
	    # tokenize review
	    test_ints = tokenize_review(test_review)
	    
	    # pad tokenized sequence
	    seq_length=sequence_length
	    features = pad_features(test_ints, seq_length)
	    
	    # convert to tensor to pass into your model
	    feature_tensor = torch.from_numpy(features)
	    
	    batch_size = feature_tensor.size(0)
	    
	    # initialize hidden state
	    h = net.init_hidden(batch_size)
	    
	    
	    # get the output from the model
	    output, h = net(feature_tensor.long(), h)
	    
	    
	    # convert output probabilities to predicted class (0 or 1)
	    pred = torch.round(output.squeeze()) 
	    # printing output value, before rounding
	    #print('Inferencia: {:.6f}'.format(output.item()))
	    
	    dados['Inferencia'] = output.item()
		
	    # print custom response
	    if(pred.item()==1):
	        #print("Comentario positivo detectado")
	        dados['Resposta'] = "Comentario positivo detectado"
	    else:
	        #print("Comentario negativo detectado")
	        dados['Resposta'] = "Comentario negativo detectado"
			
	    return dados
	        
	return	predict(net,test_review)
