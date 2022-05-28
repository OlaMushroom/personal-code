program for_to_long_nhau;
uses crt;
var i,k:integer;j:char;
begin
clrscr;
for i := 1 to 2 do
for j := 'a' to 'b' do
for k := 5 to 7 do
begin
write(i:2,j:2,k:2);writeln;
end;
readln;
end.