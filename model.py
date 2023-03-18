# from pathlib import Path

from utils import TransformACP,TransformAMP,TransformDNA
import pickle

import argparse

def predict(sequence, protein="ANY"):

    sequence = sequence.upper()
    protein = protein.upper()
    
    if len(sequence) <= 1:
        return
    
    result = None
     
    if protein in ['ACP', 'ANY']: # ACP
        model = pickle.load(open('xgb_acp_model.sav', 'rb'))
        sample = TransformACP(sequence)
        if model.predict(sample) == 1:
            return 'Classified as Anticancer Peptide.'
        else:
            if protein != 'ANY':
                return 'Negative for Anticancer Peptide'
            
    if protein in ['DNA', 'ANY']: # DNA
        model = pickle.load(open('xgb_dna_binding_model.sav', 'rb'))
        sample = TransformDNA(sequence)
        if model.predict(sample) == 1:
            return 'Classified as a DNA Binding Protein.'
        else:        
            if protein != 'ANY':
                return 'Negative for DNA Binding Protein'   
            
    if protein in ['AMP', 'ANY']: # AMP
        model = pickle.load(open('xgb_amp_model.sav', 'rb'))
        sample = TransformAMP(sequence)
        if model.predict(sample) == 1:
            return 'Classified as Antimicrobial Peptide.'
        else:
            if protein != 'ANY':
                return 'Negative for Antimicrobial Peptide'      
        
    return 'Negative for DNA Binding, Anticancer Peptide, and Antimicrobial Peptide.'
                                     

def convert(prediction):
    output = {}
    output['classification'] = prediction
        
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Predict')
    parser.add_argument('--sequence', type=str, default=None, help='Protein sequence')
    parser.add_argument('--protein', type=str, default='ANY', help='Class of proteins - DNA, ACP, AMP, or ANY')
    args = parser.parse_args()
    
    prediction = predict(sequence=args.sequence, protein=args.protein)
    output = convert(prediction)
    print(output)