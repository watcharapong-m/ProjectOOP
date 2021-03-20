from django.shortcuts import render
# from beach import models
from beach.models import top25travel

def index(request):
    data = top25travel.objects.all()
    return render(request, 'index.html',{'data':data})

def data1(request):
    data = top25travel.objects.filter(names="หาดลูกลม เกาะแสมสาร")
    return render(request, 'data1.html',{'data':data})

def data2(request):
    data = top25travel.objects.filter(names="เกาะขาม สัตหีบ ชลบุรี")
    return render(request, 'data2.html',{'data':data})
def data3(request):
    data = top25travel.objects.filter(names="หาดทรายรี เกาะเต่า สุราษฎร์ธานี")
    return render(request, 'data3.html',{'data':data})

def data4(request):
    data = top25travel.objects.filter(names="หมู่เกาะกำ ระนอง")
    return render(request, 'data4.html',{'data':data})

def data5(request):
    data = top25travel.objects.filter(names="อ่าวใหญ่ เกาะพยาม ระนอง")
    return render(request, 'data5.html',{'data':data})

def data6(request):
    data = top25travel.objects.filter(names="อ่าวหินวง เกาะเต่า สุราษฎร์ธานี")
    return render(request, 'data6.html',{'data':data})

def data7(request):
    data = top25travel.objects.filter(names="แหลมเทียน เกาะเต่า สุราษฎร์ธานี")
    return render(request, 'data7.html',{'data':data})

def data8(request):
    data = top25travel.objects.filter(names="เกาะนางยวน สุราษฎร์ธานี")
    return render(request, 'data8.html',{'data':data})

def data9(request):
    data = top25travel.objects.filter(names="เกาะรอก ตรัง")
    return render(request, 'data9.html',{'data':data})

def data10(request):
    data = top25travel.objects.filter(names="หาดพัทยา เกาะหลีเป๊ะ สตูล")
    return render(request, 'data10.html',{'data':data})

def data11(request):
    data = top25travel.objects.filter(names="หาดทรายแก้ว เกาะเสม็ด ระยอง")
    return render(request, 'data11.html',{'data':data})

def data12(request):
    data = top25travel.objects.filter(names="อ่าวนวล เกาะเสม็ด ระยอง")
    return render(request, 'data12.html',{'data':data})

def data13(request):
    data = top25travel.objects.filter(names="อ่าวแสงเทียน และ อ่าวลุงดำ เกาะเสม็ด  ระยอง")
    return render(request, 'data13.html',{'data':data})

def data14(request):
    data = top25travel.objects.filter(names="ลานหินสีชมพู จันทบุรี")
    return render(request, 'data14.html',{'data':data})

def data15(request):
    data = top25travel.objects.filter(names="Lonely Beach เกาะช้าง ตราด")
    return render(request, 'data15.html',{'data':data})

def data16(request):
    data = top25travel.objects.filter(names="หาดคลองพร้าว เกาะช้าง ตราด")
    return render(request, 'data16.html',{'data':data})

def data17(request):
    data = top25travel.objects.filter(names="อ่าวขาว เกาะหมาก ตราด  ")
    return render(request, 'data17.html',{'data':data})

def data18(request):
    data = top25travel.objects.filter(names="อ่าวสวนใหญ่ เกาะหมาก ตราด")
    return render(request, 'data18.html',{'data':data})

def data19(request):
    data = top25travel.objects.filter(names="หาดบางเบ้า เกาะกูด ตราด")
    return render(request, 'data19.html',{'data':data})

def data20(request):
    data = top25travel.objects.filter(names=" อ่าวพร้าว เกาะกูด ตราด")
    return render(request, 'data20.html',{'data':data})

def viewbase(request):
    return render(request,'base.html')