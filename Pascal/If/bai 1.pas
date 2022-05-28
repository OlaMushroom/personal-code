program If1;
uses crt;
var N: integer;
begin
  clrscr;
  write('Nhap so N=');
  readln(N);
  if (N >= 0) then
    writeln('Can bac 2 cua N la: ', sqrt(N):3:2);
  writeln;
  write('Bam phim Enter de tiep tuc!');
  readln;
end.