from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import check_password
from .models import Account
from django.contrib.auth import get_user_model

# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.core.mail import EmailMessage
# from .tokens import account_activation_token
# from django.utils.encoding import force_bytes, force_text

# def signup(request):
#     if request.method == 'POST':
#         #signup.html에서 넘어온 정보를 등록하는 과정
#         user_id = request.POST.get('user_id')
#         pw1 = request.POST.get('password1') 
#         pw2 = request.POST.get('password2')
#         email = request.POST.get('email')
#         nickname = request.POST.get('nickname')
#         #모든 정보를 입력하였는지, 비밀번호와 비밀번호확인이 잘 맞게 이루어졌는지
#         if user_id == "" or pw1 == "" or pw2 == "" or email == "" or nickname == "":
#             messages.info(request, "빈칸을 채워주시오!")
#             return redirect('signup')

#         if pw1 != pw2:
#             messages.info(request, '비밀번호가 달라요!')
#             return redirect('signup')
#         # 지금까지 과정은 유저가 정보를 제대로 입력했으면 그걸 다 가져오는 과정
#         # 정보를 받았으니까 그거를 db에저장

#         # username, password 장고에서 제공해주는 db에있는 column내용
#         if pw1 == pw2:        
#             user = User.objects.create_user(username=user_id, password=pw1) 
#             user.is_active = False
#             user.save()
#             account = Account(user=user, email=email, nickname=nickname)  # user는 외래키(참조키)
#             account.save()
#             current_site = get_current_site(request) 
#             # localhost:8000
#             message = render_to_string('user_activate_email.html',{
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
#                 'token': account_activation_token.make_token(user),
#             })
#             mail_subject = "[CakeWalk] 회원가입 인증 메일입니다."
#             user_email = account.email
#             email = EmailMessage(mail_subject, message, to=[user_email])
#             email.send()
#             return HttpResponse(
#                 '<div style="font-size: 40px; width: 100%; height:100%; display:flex; text-align:center; '
#                 'justify-content: center; align-items: center;">'
#                 '입력하신 이메일<span>로 인증 링크가 전송되었습니다.</span>'
#                 '</div>'
#             )            
#         return redirect('blog')
#     else:
#         return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['password']
        #Login html에서 입력한 정보랑 user DB랑 비교하는 과정
        user = auth.authenticate(request, username=user_id, password=password)
        # 유저 인증 결과에 따라 로그인 하거나, 에러 메세지를 전달
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, '회원정보가 없습니다.')
            return redirect('index')
    else:
        return render(request, 'index.html')

    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

# def activate(request, uid64, token):
#     uid = force_text(urlsafe_base64_decode(uid64))
#     user = User.objects.get(pk=uid)

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         auth.login(request, user)
#         return redirect('blog')
#     else:
#         return HttpResponse('비정상적인 접근입니다.')    

# Create your views here.
