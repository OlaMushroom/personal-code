program LuyThua;
var A,x:real;N,i:integer;
begin
  write('Nhap so a: ');readln(a);
  write('Nhap so n: ');readln(n);
  i:=1;x:=a;
  while i < n do
  begin
    a := a*x;inc(i);
  end;
  writeln('Luy thua cua a la: ',a);readln;
end.