import gpt_2_simple as gpt2
import os
import requests

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

f = open("generated.txt", "a")

for i in range(0,100):
    
    print("SPLIT_CHARACTERS")
    f.write("SPLIT_CHARACTERS")
    f.flush()
    f.write(str(gpt2.generate(sess)))
    f.flush()
