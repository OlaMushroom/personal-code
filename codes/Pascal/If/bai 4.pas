uses crt;
var tuoi:integer;
begin
clrscr;
write('Nhap tuoi cua ban: ');
readln(tuoi);
if (tuoi <=18) then
begin
writeln('Ban con o do tuoi',tuoi);
writeln('Ban con la vi thanh nien.');
writeln('Ban chua di bau cu duoc');
end
else
begin
write('Ban da truong thanh.');
writeln('Hay di lam can cuoc');
writeln('Ban co the cuoi vo, lay chong!');
end;
readln;
end.