import os
import treetaggerwrapper

tagger = treetaggerwrapper.TreeTagger(TAGLANG="en", TAGDIR="/mnt/c/users/Dom/Desktop/inf8225-lyrics/lemmatization/tree-tagger")

for root, dirs, files in os.walk("../lyrics-master/database"):
    for name in files:
        if "_lemmatized_lemmatized" in name:
            os.remove(root + "/" + name)
        if "_lemmatized" not in name:
            infile = open(root + "/" + name, "r")

            outfile_substructure = "../lemmatized_lyrics/"
            if not os.path.exists(outfile_substructure):
                os.mkdir(outfile_substructure)
            for substring in root.split("/")[2:]:
                outfile_substructure = outfile_substructure + substring + "/"
                if not os.path.exists(outfile_substructure):
                    os.mkdir(outfile_substructure)

            outfile = open(outfile_substructure  +"/" + name, "w")
            tags = tagger.tag_text(infile.readlines())
            lem = ""
            for tag in tags:
                tag = tag.split("\t")[-1]
                lem = lem + " " + tag
            outfile.writelines(lem[1:])
        


