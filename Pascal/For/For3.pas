program Fortodo3;
uses crt;
var i:char;
begin
clrscr;
for i := 'a' to 'z' do
write (i:3);writeln;
for i:='A' to 'Z' do
write(i:3);writeln;
for i:= 'z' downto 'a' do
write(i:3);writeln;
for i:='Z' downto 'A' do
write(i:3);writeln;
write ('So thu tu trong bang ASCII cua A la ', ORD('A'));writeln;
write ('So thu tu trong bang ASCII cua a la ', ORD('a'));writeln;
write ('Ki tu tuong ung voi STT 65 trong bang ma ASCII la ', CHR(65));writeln;
write ('Ki tu tuong ung voi STT 97 trong bang ma ASCII la ', CHR(97));readln;
end.