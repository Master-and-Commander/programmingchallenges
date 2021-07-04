command to run
py compiledocuments.py [structure] [subject]


filestructures (name of structure is passed to find file here)
     {entails the ordering of a new file which may include many templates}
     {fields: templatename repeatable 
subjecttypedata
     > Persons
      sampleperson
        data.csv 
        {fields - templatename templatefield content}
     > Studies
     > etc.
the name of a template is repeated in drawings and fields and both are used to
correctly render subject type data
templatedrawings
     {entails the lines and figures drawn on the template}
     {fields: drawtype - slot1 - slot2 - slot3 - slot4 - slot5 - code}
templatefields
     {entails fields on the documents}
     {fields: templatefield - font - size

Given structure
    and subjecttypedata

structuredf = pd.read_csv(structure)
# now you have the required templates and the order of them
subjecttypdatadf = pd.read_csv(subjecttypedata)
# now you have the data to enter into the templates 
canvas = Canvas("document name")
for structuredfrow in structuredf.index:
    # each row is a reference to a template 
    canvas = renderfromtemplate(structuredf.loc[index]["templatename"]) 
    # here we get data relevant to the template file on hand
    relevantsection = subjecttypedatadf[subjecttypedatadf[templatename] == structuredf.loc[index]["templatename"] ]
    canvas = populateTemplate(canvas, relevantsection)
    canvas.showPage() 





py compiledocuments.py [structure] [subject]





