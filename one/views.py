from django.shortcuts import render

def custom_error_page(request,exception):
    # take in exception, because if we reach this place there is some error
    return render(request,'error_view.html',status=404)
