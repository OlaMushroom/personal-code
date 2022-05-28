program Tinh_giai_thua;
var n:integer;i,s:longint;
begin
writeln('Tinh giai thua cua N');
writeln('-----------------------');
write ('Nhap so nguyen duong N: ');readln(N);
S:=1;
for i:=1 to N do 
begin
S:=S*i;
end;
writeln('Giai thua cua ',N,' la ',S);readln;
end.