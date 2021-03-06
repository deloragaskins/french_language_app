executor_name='sample_runner'
import nltk
import random
import numpy as np
#nltk.download()

import methods.web_tools as web_tools

import strategies.inputs_file as InF

import strategies.wordgroups_analysis.sentence_analysis as SA
import strategies.wordgroups_analysis.bulktext_analysis as BTA

import methods.Guided_noticing as GN






#######################################################################
#AZ_lyrics
#URL='https://lyrics.az/stromae/racine-carrie/papaoutai.html'
#URL='https://lyrics.az/stromae/racine-carree/batard.html'

#journal_en_francais_facile links
#URL='https://savoirs.rfi.fr/fr/apprendre-enseigner/langue-fran%C3%A7aise/journal-en-francais-facile-03072020-20h00-gmt'
#URL='https://savoirs.rfi.fr/fr/apprendre-enseigner/langue-fran%C3%A7aise/journal-en-francais-facile-08072020-20h00-gmt'
URL='https://savoirs.rfi.fr/fr/apprendre-enseigner/langue-francaise/journal-en-francais-facile-09072020-20h00-gmt'

#database builders
filename=web_tools.journal_en_francais_facile_puller(URL)
#filename=web_tools.AZ_lyrics_puller(URL)

######################################################################
#obtain whole text and meaningful subsets from the indicated file
bulk_text=InF.read_resource(filename)
total_paragraphs=len(bulk_text)
#
# #meaningful compositional subsets
# paragraph_number=2
# sentence_number=0

# paragraph=bulk_text[paragraph_number]
# sentence=BTA.return_sentence(bulk_text,paragraph_number,sentence_number)

# # ########################################################################
# #looking_up words
# # dictionary_choice='Linguee'
# # dictionary_choice='wordreference'
# # web_tools.lookup_words(dictionary_choice)
# ##########################################################################
#simple tools for sentence
SA.parts_of_speech_finder(sentence)
SA.recreate_sentence(sentence)

#from outide
# # #https://www.stat4decision.com/fr/traitement-langage-naturel-francais-tal-nlp/
# # import strategies.stat4decision as ST4D
# # outputs=ST4D.return_POS(sentence)
# #  outputs=ST4D.return_stem(sentence)




#for bulk text
BTA.word_finder(bulk_text)
BTA.phrase_finder(bulk_text)
BTA.printbulk_paragraphs(bulk_text)
BTA.return_sentence(bulk_text,paragraph_number,sentence_number)
# ########################################################################
# #Guided Noticing Tools
# ##Tool 1:
# #GN.print_sentences_containing_word(bulk_text)
#
# ##Tool 2:
# #GN.recreate_sentences_containing_word(bulk_text)
#
# #Tools3/4
#
# #SA.recreate_sentence(sentence)

#
# #########################################################################
#Work in Progress

#organisation
function_to_be_done=SA.parts_of_speech_finder
BTA.function_doer_for_all_sentences(bulk_text,function_to_be_done)

