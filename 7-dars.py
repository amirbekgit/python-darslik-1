#Turtle orqali suratlar chizish
#Toshbaqa chizish

from turtle import Turtle, Screen

window = Screen()
window.title('7-dars')

toshbaqa = Turtle()
toshbaqa.shape('turtle')
toshbaqa.goto(0, 0)
toshbaqa.penup()
toshbaqa.color('green')
toshbaqa.shapesize(20)





window.mainloop()



#window = Screen() ushbu kod rasm chizishimiz  uchun oyna yoki oq katta muhit yaratib beradi
#window.title esa biz rasm chizdigan muhitning ismi 
#window.mainloop() esa biz chizidigan muhitni doimo ko`rishimizga yordam beradi
#toshbaqa = Turtle() codi orqali yaratib olingan muhitda biror bir shaklni vujudga keltirish mumkin
#toshbaqa.shape esa bizning vujdaga kelgan shaklimizni istalgan boshqa shaklga o`zgartirish uchun
#toshbaqa.goto(0, 0) ushbu kod vujudga kelgan shaklni muhit bo`ylab, muhitning istalgan joyiga yo`naltirish uchun hizmat qiladi
#toshbaqa.penup() bu kod orqali vujudga kelgan shaklga biror bir kordinata berilganda ortidan chiziq qoldirish imkoniyatini beradi men penup() deb yozganman menda chiziq ko`rinmaydi
#pendown() bo`lganda ortidan chiziq qoldirar edi
#toshbaqa.color('green') bu kod vujudga kelgan shaklga rang berishda yordam beradi
#toshbaqa.shapesize(20) bu kod esa vujudga kelgan shaklni katta yoki kichik qilishda yordam beradi