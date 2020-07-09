import tracery
from tracery.modifiers import base_english
import json
import random

words = {}
with open("wordsmix.json", "r") as f:
    words = json.load(f)

# print(words["art"]["nouns"][:10])
#This will not be a static expo, more a playful research lab that mixes scientific approaches to art with creative approaches to science, for all ages and audiences. The researchers work from personal inspiration and create physical works to explore concepts and engage the visitor to evoke ideas or questions. Many installations are interactive, some are early studies and prototypes, others will be more polished end products. The creative researchers will be around to discuss the concepts, inspiration, ideas and methods behind their work, and even hack some more on the fly. 

def shuffle(art_value = 1, sci_value = 1, tech_value = 9):
    sums = art_value + sci_value + tech_value

    art_nouns_choose = random.sample(words["art"]["nouns"], int(round(100 * (art_value/sums))))
    art_adjs_choose = random.sample(words["art"]["adjs"], int(round(100 * (art_value/sums))))
    art_advs_choose = random.sample(words["art"]["advs"], int(round(100 * (art_value/sums))))

    sci_nouns_choose = random.sample(words["sci"]["nouns"], int(round(100 * (sci_value/sums))))
    sci_adjs_choose = random.sample(words["sci"]["adjs"], int(round(100 * (sci_value/sums))))
    sci_advs_choose = random.sample(words["sci"]["advs"], int(round(100 * (sci_value/sums))))

    tech_nouns_choose = random.sample(words["tech"]["nouns"], int(round(100 * (tech_value/sums))))
    tech_adjs_choose = random.sample(words["tech"]["adjs"], int(round(100 * (tech_value/sums))))
    tech_advs_choose = random.sample(words["tech"]["advs"], int(round(100 * (tech_value/sums))))

    nouns = art_nouns_choose + sci_nouns_choose + tech_nouns_choose
    adjs = art_adjs_choose + sci_adjs_choose + tech_adjs_choose
    advs = art_advs_choose + sci_advs_choose + tech_advs_choose


    rules = {
        "origin" : [
            "This will not be #ADJS.a# expo, more #ADJS.a# #NOUNS# lab that mixes #ADJS# #NOUNS.s# to art with #ADJS# #NOUNS.s# to science, for all #NOUNS.s# and #NOUNS#. The researchers work from #ADJS# #NOUNS# and create #ADJS# #NOUNS.s# to explore #NOUNS.s# and engage the visitor to evoke #NOUNS.s# or #NOUNS.s#. Many #NOUNS.s# are #ADJS#, some are #ADJS# #NOUNS.s# and #NOUNS.s#, others will be #ADV# #ADJS# #NOUNS# #NOUNS#. The #ADJS# researchers will be #ADJS# to discuss the #NOUNS.s#, #NOUNS.s#, #NOUNS.s# and #NOUNS.s# behind their #NOUNS.s#, and #ADV# hack some #ADV# on the #NOUNS#."
        ],
        "ADJS" : adjs,
        "NOUNS" : nouns,
        "ADV" : advs,
        "sentence" : ["#[NOUNS1:#NOUNS#][NOUNS2:#NOUNS#][NOUNS3:#NOUNS#][NOUNS4:#NOUNS#][NOUNS5:#NOUNS#][ADJS1:#ADJS#]origin#"]
    }

    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)

    sentence = grammar.flatten("#sentence#")
    return sentence 

print(shuffle())