Program Xeploai;
uses crt;
var
A,L,M,P:real;
begin
repeat
clrscr;
write('Nhap diem Van: ');readln(L);
write('Nhap diem Toan: ');readln(M);
write('Nhap diem Ly: ');readln(P);
writeln('');
writeln('Nhan phim bat ki de tiep tuc!');readln;
until (10>=A) and (10>=L) and (10>=M) and (10>=P) and (0<=A) and (0<=L) and (0<=M) and (0<=P);
A:=((L*2)+(M*2)+P)/5;writeln('Diem trung binh: ',A);
if (A>=0) and (A<5) then
writeln('Xep loai: Yeu');
if (A>=5) and (A<7) then
writeln('Xep loai: Trung binh');
if (A>=7) and (A<9) then
writeln('Xep loai: Kha');
if (A>=9) and (A<=10) then
writeln('Xep loai: Gioi');
writeln('Nhan phim bat ki de ket thuc!');
end.