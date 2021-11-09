#Exception Handling

animals = ['man','bear','pig','dog','elephant']

try:
    cat_index = animals.index('cat')
except:
    cat_index = 'No cat found in animals list'
print(cat_index)    
