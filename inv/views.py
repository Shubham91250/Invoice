from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from .forms import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return redirect('database')
        
    loginForm_obj = UserLogin
    return render(request, 'login.html', {'loginForm_obj': loginForm_obj})

def logout_view(request):
    logout(request)
    return redirect('/')

def database(request):
    if request.user.is_authenticated:
        return render(request, 'database.html')
    else:
        return redirect('login_view')

def add_invoice1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            clientFm_obj=ClientForm(request.POST)
            if clientFm_obj.is_valid():
                comp=clientFm_obj.cleaned_data['company_name']
                gst=clientFm_obj.cleaned_data['gst_number']
                coun=clientFm_obj.cleaned_data['country']
                sta=clientFm_obj.cleaned_data['state']
                add=clientFm_obj.cleaned_data['address']
                

            obj=Client_detail(company_name=comp,gst_number=gst,country=coun,state=sta,address=add)
            obj.save()

            messages.success(request,"Your client form has been saved successfully")

            clientFm_obj=ClientForm()
        else:
            clientFm_obj=ClientForm()

        #return render(request,'add_invoice.html',{'clientFm_obj':clientFm_obj})
    else:
        return HttpResponseRedirect('/')
    return render(request,'add_invoice.html',{'clientFm_obj':clientFm_obj})

def add_invoice2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            seriviceFm_obj = ServicesForm(request.POST)
            if seriviceFm_obj.is_valid():
                #cname=seriviceFm_obj.cleaned_data['client']
                #ser=seriviceFm_obj.cleaned_data['description']
                #qun=seriviceFm_obj.cleaned_data['quantity']
                #aout=seriviceFm_obj.cleaned_data['amount']
                service_instance = seriviceFm_obj.save(commit=False)
                service_instance.save()

           # obj=Add_Service(client=cname, description=ser,quantity=qun ,amount=aout)
            #obj.save()

            messages.success(request,"Your service ")

            seriviceFm_obj=ServicesForm()
        else:
            seriviceFm_obj=ServicesForm()
        #return render(request,'add_invoice.html',{'seriviceFm_obj':seriviceFm_obj})
    else:
        return HttpResponseRedirect('/')
    return render(request,'add_invoice.html',{'seriviceFm_obj':seriviceFm_obj})


# service provider

def add_provider(request):
    obj=AddService.objects.all()
    if request.user.is_authenticated:
        if request.method=='POST':
            providerFm_obj=ServiceProviderForm(request.POST)
            if providerFm_obj.is_valid():
                cname=providerFm_obj.cleaned_data['client']
                comp=providerFm_obj.cleaned_data['company_name']
                by=providerFm_obj.cleaned_data['handle_by']
                emai=providerFm_obj.cleaned_data['email']
                pho=providerFm_obj.cleaned_data['phone']
                anum=providerFm_obj.cleaned_data['account_number']
                inum=providerFm_obj.cleaned_data['ifsc_code']
                ban=providerFm_obj.cleaned_data['bank']
                gst=providerFm_obj.cleaned_data['gst_number']

            obj=AddService(client=cname,company_name=comp,handle_by=by,email=emai,phone=pho,account_number=anum,ifsc_code=inum,bank=ban,gst_number=gst)
            obj.save()

            messages.success(request,"AddService provider!")

            providerFm_obj=ServiceProviderForm()
        else:
            providerFm_obj=ServiceProviderForm()
            # providerFm_obj=AddService.objects.all()
        return render(request,'provider.html',{'providerFm_obj':providerFm_obj,'data':obj})
    else:
        return HttpResponseRedirect('/')     
    return render(request,'provider.html',{'providerFm_obj':providerFm_obj})


# def  show_provider(request):
#     providerFm_obj=AddService.objects.all()
#     return render(request,'provider.html',{'providerFm_obj':providerFm_obj})


def update_company(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj=AddService.objects.get(pk=id)
            fm=ServiceProviderForm(request.POST,instance=obj)
            if fm.is_valid():
                fm.save()
                messages.success(request,"sucessfully Updated")
        else:
            obj=AddService.objects.get(pk=id)
            fm=ServiceProviderForm(instance=obj)
        return render(request,'update.html',{'form':fm})
    else:
        return HttpResponseRedirect('/')

def delete(request,id):    
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = AddService.objects.filter(pk=id)
            obj.delete()
        return HttpResponseRedirect('add_provider')
    else:
        return render('/')    

def delete_client(request,pk):
    client=Client_detail.objects.get(id=pk)
    client.delete()
    return redirect('allList') 

def edit_client(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            obj=Client_detail.objects.get(id=id)
            fm=ClientForm(request.POST,instance=obj)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Client data is updated successfully !")
        else:
            obj=Client_detail.objects.get(id=id)
            fm=ClientForm(instance=obj)
        return render(request,'edit_client.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/')

def allList(request):
    if request.user.is_authenticated:

        allClient = Client_detail.objects.all()
        return render(request,'all_list.html',{'allClient':allClient})
    else:
        return HttpResponseRedirect('/')
    

def review(request,pk):
    if request.user.is_authenticated:
        clientData =Client_detail.objects.get(id=pk)
        try:
            companyData=AddService.objects.filter(client_id=pk).first()

        except AddService.DoesNotExist:
            companyData ={'key':'val'}
        
        try:
            servicesData =Add_Service.objects.filter(client_id=pk)
        except Add_Service.DoesNotExist:
            servicesData ={'key':'val'}
        
        context ={'clientData':clientData,
                 'companyData':companyData,'servicesData':servicesData}
        return render(request, 'review.html', context)
    
    else:
        return HttpResponseRedirect('/')
    

def report_list(request):
    if request.user.is_authenticated:
        allClient =Client_detail.objects.all()

        return render(request, 'reportlist.html', {'allClient': allClient})
    else:
        return HttpResponseRedirect('/')
    

def pdf_report(request, pk):
    if request.user.is_authenticated:

        clientData = Client_detail.objects.get(id=pk)
        try:
            companyData = AddService.objects.filter(client_id=pk).first()
        except AddService.DoesNotExist:
            companyData = {'Key': 'Val'}

        try:
            servicesData = Add_Service.objects.filter(client_id=pk)
        except Add_Service.DoesNotExist:
            servicesData = {'Key': 'Val'}

        try:
            total_amt = []
            for i in servicesData:
                val = i.amount * i.quantity
                total_amt.append(val)

            total_amt2 = sum(total_amt)
            gst = 0.18  # GST 18%
            gst_amt = total_amt2 * gst
            price_with_gst = total_amt2 + (total_amt2 * gst)

            # word_amt = num2words(price_with_gst, lang="en_IN")
            #print(num2words(price_with_gst, lang="en_IN"))

        except Exception as e:
            pass

        context = {'clientData': clientData, 'companyData': companyData, 'servicesData': servicesData, 'gst_amt': gst_amt, 'price_with_gst': price_with_gst,  'total_amt2':total_amt2}
# 'word_amt': word_amt,
        return render(request, 'pdf_report.html', context)

    else:
        return HttpResponseRedirect('/')