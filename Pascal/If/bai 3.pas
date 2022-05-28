Program IF3;
uses crt;
var tuoi:integer;
begin
clrscr;
write('Nhap tuoi cua ban: '); readln (tuoi);
if (tuoi<=18) then
writeln('Ban con o do tuoi vi thanh nien…')
else
write('Ban da truong thanh, hay di lam can cuoc!');
readln;
end.
