import ir_datasets
dataset = ir_datasets.load("beir/arguana")
for query in dataset.docs_iter():
    print (query)