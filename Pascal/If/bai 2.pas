program If1;
uses crt;
var N:integer;
begin
clrscr;
write('Nhap 1 so nguyen duong N= ');readln(N);
if (N>=0) then
begin
writeln('Can bac 2 cua N la: ',sqrt(N):3:2);
writeln('Binh phuong cua N la: ',sqr(N):2);
writeln('Gia tri cua bieu thuc f(N): ',1/N + 1/(N*N) + 1/(N*N*N):3:2);
end;
writeln;
write('Bam phim Enter de tiep tuc!');
readln;
end.