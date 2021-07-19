from django.urls import path
from . import views

app_name = 'intranet'
urlpatterns = [
	path('', views.index, name="index"),
	path('alumno', views.alumno, name="alumno"),
	path('docente', views.docente, name="docente"),
	path('admin', views.admin, name="admin"),

	# Docente
	path('docente/grados', views.TeacherGradeList.as_view(), name="dc_grados"),
	path('docente/grados/<int:pk>/', views.TeacherGradeDetail.as_view(), name="dc_grado_detail"),
	path('docente/grados/<int:grado>/curso/<int:pk>/', views.TeacherGradeCursoDetail.as_view(), name="dc_gradocurso_detail"),
	path('docente/alumnos/', views.TeacherStudentList.as_view(), name="dc_registroalumnos"),
	path('docente/horario/', views.TeacherClasesList.as_view(), name="dc_clasesschedule"),
	path('docente/capacitaciones/', views.TeacherCapacitacionList.as_view(), name="dc_capacitaciones"),
	path('docente/class/<int:pk>/', views.TeacherClassDetail.as_view(), name="dc_class_detail"),

	# Student

	# Admin

	# Terceros
	path('docente/<int:pk>/', views.TeacherDetail.as_view(), name="tc_detail"),
	path('alumno/<int:pk>/', views.StudentDetail.as_view(), name="st_detail"),

	# Extra
	path('_/noview/logout/', views.logout_view, name="logout"),
	path('_/noview/gdrive/create/class/<int:pk>/', views.gdrive_create, name="gdrive_create"),
	path('_/noview/gdrive/upload/class/<int:pk>/', views.gdrive_upload, name="gdrive_upload"),
	path('_/noview/gdrive/delete/class/<int:pk>/', views.gdrive_delete, name="gdrive_delete"),
	path('_/noview/excel/student/<int:student_pk>/', views.ReporteComprobantes, name="report_student"),
]
