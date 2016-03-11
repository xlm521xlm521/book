#coding=utf-8
from django import forms
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile

class CategoryForm( forms. ModelForm) :
	name = forms.CharField( max_length=128, help_text="Please enter the category name. ")
	views = forms.IntegerField( widget=forms.HiddenInput( ) , initial=0)
	likes = forms.IntegerField( widget=forms.HiddenInput( ) , initial=0)
	slug = forms.CharField( widget=forms. HiddenInput( ) , required=False)
# 内部类
	class Meta:
# model建立表单和模型类的关联， fields里包含表单显示出来的字段
		model = Category
		fields = ( 'name' , )
class PageForm( forms.ModelForm) :
	page_id = forms.IntegerField(help_text="Please enter the id of the page. ")
	stage = forms.CharField( max_length=128, help_text="请输入所属阶段（选项）")
	mytype = forms.CharField( max_length=128, help_text="请输入#题目类型（选项单选、多选、判断、填空、简答、代码、实操）")
	key = forms.CharField( max_length=128, help_text="请输入关键字")
	level = forms.CharField( max_length=128, help_text="请输入难度等级（选项ABCD） ")
	body = forms.CharField( max_length=128, help_text="请输入题干")
	option_A = forms.CharField( max_length=128, help_text="请输入A 选项 ")
	option_B = forms.CharField( max_length=128, help_text="请输入B 选项")
	option_C = forms.CharField( max_length=128, help_text="请输入C 选项")
	option_D = forms.CharField( max_length=128, help_text="请输入D 选项")
	option_E = forms.CharField( max_length=128, help_text="请输入E 选项 ")
	option_F = forms.CharField( max_length=128, help_text="请输入F 选项")
	information = forms.CharField( max_length=128, help_text="请输入所属知识点（读关联  分隔;）")	
    	answer = forms.CharField(max_length=128,help_text="请输入答案 ")
	explain = forms.CharField(max_length=128,help_text="请输入答案说明")
	author = forms.CharField(max_length=128,help_text="请输入出题人")
	class Meta:
# model建立表单和模型类的关联， 排除exclude里包含的字段， 其它字段显示
		model = Page
		exclude = ( 'category' , )
		#fields = ( ' title' , ' url' , ' views' )

class UserForm(forms.ModelForm) :
	password = forms.CharField(widget=forms.PasswordInput( ) )
	class Meta:
		model = User
		fields = ( 'username' , 'email' , 'password' )
class UserProfileForm( forms.ModelForm) :
	class Meta:
		model = UserProfile
		fields = ( 'website' , 'picture' )