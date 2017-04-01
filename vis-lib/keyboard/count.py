#!/usr/bin/env python
# -*- coding:utf-8 -*-
import codecs

class count(object):
    def __init__(self):
        self.OriginalFile=codecs.open('diagnose.txt','r','utf-8')
        self.BodyPartFile=codecs.open('bodypart.txt','r','utf-8')
        self.CharacterFile=codecs.open('character.txt','r','utf-8')
        self.DiseaseFile=codecs.open('disease.txt','r','utf-8')
        self.DrugFile=codecs.open('drug.txt','r','utf-8')
        self.ConjFile=codecs.open('conjunction.txt','r','utf-8')
        self.BodyReactionFile=codecs.open('BodyReaction.txt','r','utf-8')
        self.ActionFile=codecs.open('action.txt','r','utf-8')
        self.NewFile=codecs.open('test.html','w','utf-8')

        #7fc97f
#beaed4
#fdc086
#ffff99
#386cb0
#f0027f
#bf5b17

        self.NewFile.write('<html>'+'\n'+'<style>'+'\n'+'span.disease {color:#7fc97f;}'+'\n'+'span.Character {color:#bf5b17;}'+'\n'+'span.BodyPart {color:#beaed4;}'+'\n'+'span.drug {color:#fdc086;}'+'\n'+'span.Conjunction {color:#ffff99;}'+'\n'+'span.Action {color:#386cb0;}'+'\n'+'span.BodyReaction {color:#f0027f;}'+'\n'+'</style>'+'\n'+'<body>'+'\n')

        self.BodyPartWords = []
        AllBodyPartWords = self.BodyPartFile.readlines()
        for SingleBodyPartWord in AllBodyPartWords:
            SingleBodyPartWord = SingleBodyPartWord.strip('\n')
            self.BodyPartWords.append(SingleBodyPartWord)

        self.DrugWords = []
        AllDrugWords = self.DrugFile.readlines()
        for SingleDrugWord in AllDrugWords:
            SingleDrugWord = SingleDrugWord.strip('\n')
            self.DrugWords.append(SingleDrugWord)

        self.CharacterWords = []
        AllCharacterWords = self.CharacterFile.readlines()
        for SingleCharacterWord in AllCharacterWords:
            SingleCharacterWord = SingleCharacterWord.strip('\n')
            self.CharacterWords.append(SingleCharacterWord)

        self.DiseaseWords = []
        AllDiseaseWords = self.DiseaseFile.readlines()
        for SingleDiseaseWord in AllDiseaseWords:
            SingleDiseaseWord = SingleDiseaseWord.strip('\n')
            self.DiseaseWords.append(SingleDiseaseWord)

        self.ConjWords = []
        AllConjWords = self.ConjFile.readlines()
        for SingleConjWord in AllConjWords:
            SingleConjWord = SingleConjWord.strip('\n')
            self.ConjWords.append(SingleConjWord)

        self.BodyReactionWords = []
        AllBodyReactionWords = self.BodyReactionFile.readlines()
        for SingleBodyReactionWord in AllBodyReactionWords:
            SingleBodyReactionWord = SingleBodyReactionWord.strip('\n')
            self.BodyReactionWords.append(SingleBodyReactionWord)

        self.ActionWords = []
        AllActionWords = self.ActionFile.readlines()
        for SingleActionWord in AllActionWords:
            SingleActionWord = SingleActionWord.strip('\n')
            self.ActionWords.append(SingleActionWord)



        self.DiseaseString = ''
        for i in range(len(self.DiseaseWords)):

            self.DiseaseString = self.DiseaseString + self.DiseaseWords[i]+' '



        for sentence in self.OriginalFile.readlines():
            #print sentence
            for i in range(len(self.DiseaseWords)):
                
                while self.DiseaseWords[i]+' '  in sentence:
                    #print self.DiseaseWords[i]
                    sentence = sentence.replace(self.DiseaseWords[i],'<span class="Disease">'+self.DiseaseWords[i]+'</span>')
                while self.DiseaseWords[i]+','  in sentence:
                    #print self.DiseaseWords[i]
                    sentence = sentence.replace(self.DiseaseWords[i]+',','<span class="Disease">'+self.DiseaseWords[i]+'SIGN,</span>')
                while self.DiseaseWords[i]+'.'  in sentence:
                    #print self.DiseaseWords[i]
                    sentence = sentence.replace(self.DiseaseWords[i]+'.','<span class="Disease">'+self.DiseaseWords[i]+'SIGN.</span>')
                while '['+self.DiseaseWords[i]+']'  in sentence:
                    #print self.DiseaseWords[i]
                    sentence = sentence.replace('['+self.DiseaseWords[i]+']','<span class="Disease">SIGN['+self.DiseaseWords[i]+'SIGN]</span>')

            # if word in diseasestring, do not replace add a simple string
            # add 
            for i in range(len(self.CharacterWords)):
                if ' '+self.CharacterWords[i]+' ' not in self.DiseaseString:
            
            
                    while self.CharacterWords[i]+' ' in sentence:
                        
                            #print self.CharacterWords[i]
                            sentence = sentence.replace(self.CharacterWords[i],'<span class="Character">'+self.CharacterWords[i]+'</span>')
                        
                    while self.CharacterWords[i]+'.' in sentence:
                        
                            sentence = sentence.replace(self.CharacterWords[i]+'.','<span class="Character">'+self.CharacterWords[i]+'SIGN.</span>')
                    

                    while self.CharacterWords[i]+',' in sentence:
                        
                            sentence = sentence.replace(self.CharacterWords[i]+',','<span class="Character">'+self.CharacterWords[i]+'SIGN,</span>')
                        

                    while '('+self.CharacterWords[i]+')' in sentence:
                            sentence = sentence.replace('('+self.CharacterWords[i]+')','<span class="Character">(SIGN'+self.CharacterWords[i]+'SIGN)</span>')
                else:
                    for j in range(len(self.DiseaseWords)):
                        if self.CharacterWords[i] in self.DiseaseWords[j] and self.DiseaseWords[j] in sentence:
                            sentence = sentence.replace(self.CharacterWords[i],self.CharacterWords[i]+'SIGN')
                        else:
                            while self.CharacterWords[i]+' ' in sentence:
                        
                            #print self.CharacterWords[i]
                                sentence = sentence.replace(self.CharacterWords[i],'<span class="Character">'+self.CharacterWords[i]+'</span>')
                        
                            while self.CharacterWords[i]+'.' in sentence:
                                
                                    sentence = sentence.replace(self.CharacterWords[i]+'.','<span class="Character">'+self.CharacterWords[i]+'SIGN.</span>')
                            

                            while self.CharacterWords[i]+',' in sentence:
                                
                                    sentence = sentence.replace(self.CharacterWords[i]+',','<span class="Character">'+self.CharacterWords[i]+'SIGN,</span>')
                                

                            while '('+self.CharacterWords[i]+')' in sentence:
                                    sentence = sentence.replace('('+self.CharacterWords[i]+')','<span class="Character">(SIGN'+self.CharacterWords[i]+'SIGN)</span>')


            
                #print sentence,self.CharacterWords[i]
                    
            
            for i in range(len(self.BodyPartWords)):
                if ' '+self.BodyPartWords[i]+' ' not in self.DiseaseString:
                

                    while self.BodyPartWords[i]+' ' in sentence:
                        
                        sentence = sentence.replace(self.BodyPartWords[i],'<span class="BodyPart">'+self.BodyPartWords[i]+'</span>')
                        
                    while self.BodyPartWords[i]+'.' in sentence:
                        
                        sentence = sentence.replace(self.BodyPartWords[i]+'.','<span class="BodyPart">'+self.BodyPartWords[i]+'SIGN.</span>')
                        
                    while 'span>'+self.BodyPartWords[i] in sentence:

                        sentence = sentence.replace(self.BodyPartWords[i],'<span class="BodyPart">'+self.BodyPartWords[i]+'SIGN</span>')

                    while self.BodyPartWords[i]+',' in sentence:
                        sentence = sentence.replace(self.BodyPartWords[i]+',','<span class="BodyPart">'+self.BodyPartWords[i]+'SIGN,</span>')
                else:
                    for j in range(len(self.DiseaseWords)):
                        if self.BodyPartWords[i] in self.DiseaseWords[j] and self.DiseaseWords[j] in sentence:

                            sentence = sentence.replace(self.BodyPartWords[i],self.BodyPartWords[i]+'SIGN')
                        else:
                

                            while self.BodyPartWords[i]+' ' in sentence:
                                
                                sentence = sentence.replace(self.BodyPartWords[i],'<span class="BodyPart">'+self.BodyPartWords[i]+'</span>')
                                
                            while self.BodyPartWords[i]+'.' in sentence:

                                sentence = sentence.replace(self.BodyPartWords[i]+'.','<span class="BodyPart">'+self.BodyPartWords[i]+'SIGN.</span>')
                                
                            while 'span>'+self.BodyPartWords[i] in sentence:

                                sentence = sentence.replace(self.BodyPartWords[i],'<span class="BodyPart">'+self.BodyPartWords[i]+'SIGN.</span>')

                            while self.BodyPartWords[i]+',' in sentence:
                                sentence = sentence.replace(self.BodyPartWords[i]+',','<span class="BodyPart">'+self.BodyPartWords[i]+'SIGN,</span>')



                for i in range(len(self.DrugWords)):
                    if self.DrugWords[i]+' ' not in self.DiseaseString:

                        while self.DrugWords[i]+' ' in sentence:
                            # the first part of replace is for 
                            sentence = sentence.replace(self.DrugWords[i]+' ','<span class="Drug">'+self.DrugWords[i]+'SIGN </span> ')


                        while self.DrugWords[i]+'-' in sentence:
                            sentence = sentence.replace(self.DrugWords[i]+'-',self.DrugWords[i]+'SIGN-')

                        while self.DrugWords[i]+'.' in sentence:
                            sentence = sentence.replace(self.DrugWords[i]+'.','<span class="Drug">'+self.DrugWords[i]+'SIGN.</span>')
                  
                        while self.DrugWords[i]+',' in sentence:
                       
                            sentence = sentence.replace(self.DrugWords[i]+',','<span class="Drug">'+self.DrugWords[i]+'SIGN,</span>')
                    else:
                        sentence = sentence.replace(self.DrugWords[i],self.DrugWords[i]+'SIGN')
                      

                for i in range(len(self.BodyReactionWords)):
                    while self.BodyReactionWords[i]+' ' in sentence:
                        sentence = sentence.replace(self.BodyReactionWords[i],'<span class="BodyReaction">'+self.BodyReactionWords[i]+'</span>')
                    while self.BodyReactionWords[i]+'.' in sentence:
                        sentence = sentence.replace(self.BodyReactionWords[i]+'.','<span class="BodyReaction">'+self.BodyReactionWords[i]+'SIGN.</span>')
                    while 'span>'+self.BodyReactionWords[i] in sentence:
                        sentence = sentence.replace(self.BodyReactionWords[i],'<span class="BodyReaction">'+self.BodyReactionWords[i]+'</span>')
                    while self.BodyReactionWords[i]+',' in sentence:
                        sentence = sentence.replace(self.BodyReactionWords[i]+',','<span class="BodyReaction">'+self.BodyReactionWords[i]+'SIGN,</span>')

                

                for i in range(len(self.ConjWords)):
                    #print sentence
                    while ' '+self.ConjWords[i]+' ' in sentence:
                        sentence = sentence.replace(' '+self.ConjWords[i]+' ',' <span class="Conjunction"> SIGN'+self.ConjWords[i]+'SIGN</span>')
                    while 'span>'+self.ConjWords[i]+' ' in sentence:
                        sentence = sentence.replace(self.ConjWords[i],'<span class="Conjunction">'+self.ConjWords[i]+'</span>')
                    while self.ConjWords[i]+',' in sentence:
                        sentence = sentence.replace(self.ConjWords[i]+',',' <span class="Conjunction">'+self.ConjWords[i]+'SIGN,</span>')

                    # while ','+self.ConjWords[i]+' ' in sentence:#solve behavi or question
                    #     #print self.ConjWords[i]
                    #     sentence = sentence.replace(','+self.ConjWords[i]+' ','<span class="Conjunction">,SIGN'+self.ConjWords[i]+'SIGN </span>')

                    while '('+self.ConjWords[i]+')' in sentence:#solve behavi or question
                        #FIRST PART OF REPLACE FOR (DUE TO)
                        sentence = sentence.replace('('+self.ConjWords[i]+')','<span class="Conjunction">(SIGN'+self.ConjWords[i]+')SIGN</span>')

                for i in range(len(self.ActionWords)):
                
                    if ' '+self.ActionWords[i]+' ' not in self.DiseaseString:

                        while 'span>'+self.ActionWords[i] in sentence:
                            # for drug + actionword
                            sentence = sentence.replace(self.ActionWords[i],'<span class="Action">'+self.ActionWords[i]+'</span>')
                        while self.ActionWords[i]+'<span' in sentence:
                            # for drug + actionword
                            sentence = sentence.replace(self.ActionWords[i],'<span class="Action">'+self.ActionWords[i]+'</span>')

                        while self.ActionWords[i]+' ' in sentence:
                            sentence = sentence.replace(self.ActionWords[i]+' ','<span class="Action">SIGN'+self.ActionWords[i]+'SIGN </span> ')
                 
                        while '('+self.ActionWords[i]+')' in sentence:
                            
                            sentence = sentence.replace('('+self.ActionWords[i]+')','<span class="Action">(SIGN'+self.ActionWords[i]+'SIGN)</span>')
                else:
                    #print self.ActionWords[i]
                    sentence = sentence.replace(self.ActionWords[i],self.ActionWords[i]+'SIGN')


            if '<span' in sentence:
                sentence = sentence.replace('<span',' <span')
                sentence = sentence.replace('span>','span> ')
            sentence = sentence + '<br>'

            sentence = sentence.replace('SIGN','')

            #print sentence
            self.NewFile.write(sentence)

        self.NewFile.write('\n'+'</body>'+'\n'+'</html>')




if __name__ == '__main__':
    count()


