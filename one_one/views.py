from django.shortcuts import render

def example_view(request):
    #one_one/templates/one_one/example.html and is nothing but an example of how to render templates in django so it saves our time
    return render (request,'one_one/example.html')
def variable_view(request):
    my_var ={ 
        'first':'Rosaland',
        'last':'Franklin',
        'some_list':[1,2,3],
        'some_dict':{ 'inside_key':'inside_value' },
        'user_logged_in':True,
        
    }
     # tHe context has to be a dictionary always 
    return render(request,'one_one/variables.html',context =my_var)
    # to transfer the my_var to the html file we use context keyword and supply it with the data 
