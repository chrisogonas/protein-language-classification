import numpy as np
import pandas as pd


def splitchain(dataframe):
    x1 = dataframe[0]
    c1 = x1[0:1];c2 = x1[1:2];c3 = x1[2:3];c4 = x1[3:4];c5 = x1[4:5]
    c6 = x1[5:6];c7 = x1[6:7];c8 = x1[7:8];c9 = x1[8:9];c10 = x1[9:10]
    c11 = x1[10:11];c12 = x1[11:12];c13 = x1[12:13];c14 = x1[13:14];c15 = x1[14:15]
    c16 = x1[15:16];c17 = x1[16:17];c18 = x1[17:18];c19 = x1[18:19];c20 = x1[19:20]
    c21 = x1[20:21];c22 = x1[21:22];c23 = x1[22:23];c24 = x1[23:24];c25 = x1[24:25]
    c26 = x1[25:26];c27 = x1[26:27];c28 = x1[27:28];c29 = x1[28:29];c30 = x1[29:30]
    c31 = x1[30:31];c32 = x1[31:32];c33 = x1[32:33];c34 = x1[33:34];c35 = x1[34:35]
    c36 = x1[35:36];c37 = x1[36:37];c38 = x1[37:38];c39 = x1[38:39];c40 = x1[39:40]
    c41 = x1[40:41];c42 = x1[41:42];c43 = x1[42:43];c44 = x1[43:44];c45 = x1[44:45]
    c46 = x1[45:46];c47 = x1[46:47];c48 = x1[47:48];c49 = x1[48:49];c50 = x1[49:50]
    return pd.Series([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,
        c21,c22,c23,c24,c25,c26,c27,c28,c29,c30,c31,c32,c33,c34,c35,c36,c37,c38,c39,c40,
           c41,c42,c43,c44,c45,c46,c47,c48,c49,c50])

# function to check the chain
def contains_specific_letters(s):
    specific_letters = ['B', 'J', 'O', 'U', 'X', 'Z']
    for letter in s:
        if letter.upper() in specific_letters:
            return True
    return False

def TransformACP(x):
        data = {'sequences': [x], 'label': [0]}
        df = pd.DataFrame(data)
        df[['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10',
        'c11','c12','c13','c14','c15','c16','c17','c18','c19','c20',
        'c21','c22','c23','c24','c25','c26','c27','c28','c29','c30',
        'c31','c32','c33','c34','c35','c36','c37','c38','c39','c40',
        'c41','c42','c43','c44','c45','c46','c47','c48','c49',
        'c50']] = df.apply(splitchain,axis=1)
        letter_2num = {
            s: i for i, s in enumerate(
            ['','A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
                    }
        for column in df.columns[2:]:
            df[column] = df[column].replace(letter_2num)
        df.fillna(0)
        X_sample = df.drop(columns=['sequences','label']).values
        X_sample = X_sample.astype(np.float64)
        return X_sample

##### AMP AMP AMP AMP ##############
def TransformAMP(x):
        data = {'SequenceID': [x], 'label': [0]}
        df = pd.DataFrame(data)
        df_split = df['SequenceID'].str.split(pat="", expand=True)
        df2 = df[['SequenceID','label']].join(df_split) 
        letter_2num = {
        s: i for i, s in enumerate(
        ['','A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J','K','L','M',
         'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
            }
        for column in df2.columns[3:]:
            df2[column] = df2[column].replace(letter_2num)  
        df2.to_csv('toto.csv') 
        df3 = pd.read_csv('toto.csv')
        df4=df3.fillna(0)
        X_sample= df4.drop(columns=['Unnamed: 0','SequenceID','label']).values
        b = np.zeros((1, 183-X_sample.shape[1]))
        X_sample2 = np.hstack((X_sample, b))
        X_sample2 = X_sample2.astype(np.float64)
        return X_sample2

##### DNA DNA DNA DNA ##############
def TransformDNA(x):
        data = {'sequence': [x], 'label': [0]}
        df = pd.DataFrame(data)
        df_split = df['sequence'].str.split(pat="", expand=True)
        df2 = df[['sequence','label']].join(df_split) 
        letter_2num = {
        s: i for i, s in enumerate(
            ['','A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
            }
        for column in df2.columns[3:]:
            df2[column] = df2[column].replace(letter_2num) 
        df2.to_csv('toto.csv') 
        df3 = pd.read_csv('toto.csv')
        df4=df3.fillna(0)
        X_sample= df4.drop(columns=['Unnamed: 0','sequence','label']).values
        b = np.zeros((1, 4913-X_sample.shape[1]))
        X_sample2 = np.hstack((X_sample, b))
        X_sample2 = X_sample2.astype(np.float64)
        return X_sample2