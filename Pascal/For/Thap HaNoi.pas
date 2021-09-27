program thap;
uses crt;
var i,j,N:integer;
begin
clrscr;
write('Nhap so hang: ');readln(N);
for i:=1 to N do
begin
for j:=1 to (N-i) do write(CHR(32));
for j:=1 to (2*i-1) do
begin
textcolor(2);
textbackground(6);
write(' ');
textbackground(0);
end;
writeln;
end;
readln;
end.